
# Solved.Earth_FastAPI<br/> (Support Mobile App to provide strong motivation for environmental protection)

<br/>

> Solved.Earth is designed based on the idea that applying the quest-reward method to environmental protection activities would provide strong motivation for environmental protection. <br/>
> Solved.Earth는 퀘스트-보상 방식을 환경 보호 활동에 접목하면 더 강력한 환경 보호 활동에 대한 동기를 부여할 수 있을 것이라는 아이디어를 바탕으로 하는 모바일 앱 개발 프로젝트입니다.

<br/>

> Solved.Earth_FastAPI receives image from the app and analysis image with AI. Based on the analysis results, it returns whether the challenge was successful or not. 
<br/>
> Solved.Earth_FastAPI에서는 앱으로부터 전송된 이미지를 받고 AI를 이용해 이미지 분석을 진행합니다. 이미지 분석 결과를 토대로 challenge 성공 여부를 Solved.Earth 앱에 반환합니다.

<br/>
<br/>

## ✔ SPECIFIC INFORMATIONS ABOUT SOLVED.EARTH

This README.md is only about API of Solved.Earth project.

Main ReadME has more specific informations!

본 README.md는 Solved.Earth 프로젝트의 API 부분만 다룹니다.
  
Main ReadME에는 더 세부적인 정보가 기록되어 있습니다!

ex)

    📷 Demonstration Video(시연영상)

    📌 Introducing Solved.Earth (프로젝트 소개)

    ⚙️ System Configuration and Architecture (시스템 구성 및 아키텍처)

[Go to Solved.Earth Main repository](https://github.com/solved-earth/Solved.Earth)

<br/>
<br/>
<br/>
<br/>

## 🔑 GUIDES

<h4>License : <a href="LICENSE">MIT</a> / <a href="./lib/oss_licenses.dart">Third Party</a> </h4>

<br/>
<br/>
<br/>
<br/>

## ✔ NOTICE

This is still ongoing project. Please contact us(ecotreegrowing@gmail.com) to discuss how we can work together.</b><br/>

이 프로젝트는 아직 완전히 배포되지 않은 상태입니다. 이 프로젝트에 참여하시고자 한다면 저희 팀 이메일을 통해 연락주시길 바랍니다.(ecotreegrowing@gmail.com)


## ⚙️ System Configuration and Architecture (시스템 구성 및 아키텍처)

# Solved.Earth <br/> (Mobile App to provide strong motivation for environmental protection)


<br/>
<br/>

## ⚙️ System Configuration and Architecture (시스템 구성 및 아키텍처)

### 1. Solved.Earth System Structure (Solved.Earth 시스템 구조)

   <p align="center"><img src=./report/struct1.jpg alt="struct1" width="800"/></p>

<br/>
<br/>
   
### 2. Solved.Earth App Client Application Structure (Solved.Earth 앱 클라이언트 어플리케이션 구조)

   <p align="center"><img src=./report/struct2.jpg alt="struct2" width="800"/></p>

<br/>
   
### 3. API Detail View (API 상세 구조)

   <p align="center"><img src=./report/struct3.jpg alt="struct3" width = "800"/></p>

#### 3-1. API Endpoint

**`/upload-images`**

- request: POST
- Query Parameters
    
    username: str, 
    
    challenge_name: str
    
- Request Body
    
    file: multipart/form-data
    

- Response:
    - challenge passed
    
    ```json
    {
    	"success": True,
    }
    ```
    
    - challenge didn't passed
    
    Variable missing is objects not in photo.
    
    ```json
    {
        "success":False,
        "reason":"missing values",
        "missing":missing
    }
    ```

#### 3-2. AI Image Analysis

~

<br/>



<details>
<summary><b>AAAAAAAAAAAAAAAAA</b></summary>
<div markdown="1">       
&nbsp;&nbsp; aaaaaaaaaaaaaaaaaaaaaaaaaaa
</div>
</details>

<br/>
<br/>

## 🔧 Applied Technology (적용 기술)

FastAPI is a user-friendly and fast framework. It is attractive because it not only improves development speed but also has very fast operation speed, which is why we chose fastapi.

FastAPI는 사용자 친화적이며 빠른 프레임워크입니다. 개발 속도의 향상과 함께 작동 속도도 매우 빠른다는 점이 매력적인 친구이고, 이것이 우리가 fastapi를 선택한 이유입니다.

We applied CI/CD(Continuous Integration/Continuout Deloyment) with Github-Actions.New changes are built and tested regularly and integrates into a API Server.

github-actions를 이용한 CI/CD를 적용하여 새로운 변경사항이 정기적으로 빌드 및 테스트 되어 API 서버에 통합됩니다.

### - Dev. Environment (개발 환경) 

![Windows 11](https://img.shields.io/badge/Windows%2011-0078D4?style=for-the-badge&logo=windows11&logoColor=white)
![Linux Ubuntu](https://img.shields.io/badge/Linux_Ubuntu-FCC624?style=for-the-badge&logo=linux&logoColor=black)

### - Dev. Tool (개발 도구)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)

### - Framework (프레임워크)

![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
![OpenCV](https://img.shields.io/badge/opencv-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![YOLOv5](https://img.shields.io/badge/YOLOv5-00FFFF?style=for-the-badge&logo=YOLOv5&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)
![Github-Actions](https://img.shields.io/badge/Github_Actions-181717.svg?style=for-the-badge&logo=github&logoColor=white)

### - Programming Language (개발 언어)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

<br/>
<br/>