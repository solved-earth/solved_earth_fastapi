from typing import Optional, Annotated
from fastapi import FastAPI, UploadFile, Body
from sqlmodel import Session, SQLModel, create_engine, select
from pathlib import Path
import datetime
import os, sys
from dotenv import load_dotenv
from api_models import User, Photo, Challenge
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from yolov5 import detect

PROJECT_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = os.path.join(BASE_DIR,'static')
IMG_DIR = os.path.join(STATIC_DIR,'images')

load_dotenv(os.path.join(PROJECT_DIR, '.env'))
mysql_user = os.getenv("MYSQL_USER")
mysql_password = os.getenv("MYSQL_PASSWORD")
base_url = os.getenv("BASE_URL")

# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"
db_url = "mysql+pymysql://"+str(mysql_user)+":"+str(mysql_password)+"@"+str(base_url)+":3306/solved_earth"
print(db_url)

connect_args = {"check_same_thread": False}
# engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)
engine = create_engine(db_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


"""
Test DB
"""
# with Session(engine) as session:
#     challenge = Challenge(challenge_name="recycle", answer="metal, cardboard")
#     session.add(challenge)
#     session.commit()
#     session.refresh(challenge)

"""
Function Defination
"""

def create_folder(root) -> None:
    try:
        if not os.path.exists(root):
            os.makedirs(root)
    except OSError:
        print("ERROR: Create Folder Failed :"+root)

def _get_or_create_user_by_username(username:str) -> User:
    with Session(engine) as session:
        statement = select(User).where(User.username == username)
        user = session.exec(statement).first()

        if user == None:
            user = User(username=username)
            session.add(user)
            session.commit()
            session.refresh(user)
    return user

def _create_photo(user:User, challenge:Challenge, photo_url:str):
    with Session(engine) as session:
        photo = Photo(user_id=user.id, challenge_id=challenge.id, photo_url=photo_url)
        session.add(photo)
        session.commit()
        session.refresh(photo)
    return photo

def _get_challenge_by_challenge_name(challenge_name:str) -> Challenge:
    with Session(engine) as session:
        statement = select(Challenge).where(Challenge.challenge_name == challenge_name)
        challenge = session.exec(statement).first()
    return challenge

def _get_challenge_by_challenge_id(challenge_id:int) -> Challenge:
    with Session(engine) as session:
        challenge = session.get(Challenge, challenge_id)
    return challenge

def check_challenge(photo_location: str, challenge: Challenge) -> dict:
    photo_location = Path(photo_location)
    objects:set = detect.run(
        weights=['../yolov5/runs/train/result_trash/weights/best.pt'], 
        source=photo_location, 
        data=os.path.join(PROJECT_DIR, 'yolov5/data/coco128.yaml'), 
        imgsz=[640, 640], conf_thres=0.25, iou_thres=0.45, max_det=1000, device='', 
        view_img=False, save_txt=False, save_conf=False, save_crop=False, 
        nosave=False, classes=None, agnostic_nms=False, augment=False, visualize=False, update=False, 
        project=os.path.join(PROJECT_DIR, 'yolov5/runs/detect'), 
        name='exp', exist_ok=False, line_thickness=3, hide_labels=False, hide_conf=False, half=False, dnn=False, vid_stride=1
    )

    answers = challenge.answer.split(", ")
    answers = set(answers)
    founded = answers.intersection(objects)
    missing = answers.difference(objects)
    print(objects)
    if(founded):
        result = {
            "success":True,
            "founded":list(founded)
        }
    else:
        result = {
            "success":False,
            "reason":"missing values",
            "missing":list(missing)
        }

    return result

# for Test
@app.get("/data")
async def data():
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        challenges = session.exec(select(Challenge)).all()
        photos = session.exec(select(Photo)).all()
        result = {
            "users": users,
            "challenges": challenges,
            "photos": photos
        }
        return result
    

@app.post('/upload-image')
async def upload_image(username:str, challenge_id:int, file:UploadFile):
    root = os.path.join(IMG_DIR, username, str(challenge_id))
    print(root)
    create_folder(root)
    
    """ 
    Save Image 
    """
    saved_file_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".png"
    photo_url = os.path.join(root, saved_file_name)

    with open(photo_url, "wb+") as file_object:
        file_object.write(file.file.read())

    """
    Create Photo
    """
    user = _get_or_create_user_by_username(username)
    challenge = _get_challenge_by_challenge_id(challenge_id)
    _create_photo(user, challenge, photo_url)

    """
    Check Challenge
    """

    result=check_challenge(photo_url, challenge)
    return result

