from fastapi import FastAPI
from app.router.password_routes import router 


app = FastAPI(title="Password Generator")
app.include_router(router=router)


