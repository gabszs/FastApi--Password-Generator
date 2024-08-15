from fastapi import FastAPI
from uvicorn import run

from app.router.password_routes import router


app = FastAPI(
    title="Password Generator",
    version="1.0.0",
    description="Password api to generate random pins and passwords",
    contact={
        "name": "GabrielCarvalho",
        "email": "gabrielcarvalho.workk@gmail.com",
        "url": "https://www.linkedin.com/in/gabzsz",
    },
)
app.include_router(router=router)

if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=6543, reload=True)
