from fastapi import FastAPI
from app.router.password_routes import router 


app = FastAPI()
app.include_router(router=router)

@app.get('/')
def hello_world():
    return {"message": "HelloWOrld"}
