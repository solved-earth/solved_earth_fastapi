#!/nin/bash

echo "cd dir"

cd FastAPI

echo "run server"

uvicorn main:app --reload --host=0.0.0.0 --port=8000