from dotenv import load_dotenv
from fastapi import FastAPI
from app.api.common import router as sample_router
from app.api import users
from app.api.auth import router as auth_router
from app.database.connection import conn
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  
    allow_headers=["*"],  
)

@app.get("/")
def get_sample():
    return {"message": "API is running!"}

@app.get("/test-connection-mysql")
async def get_sample():
    cursor = conn.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    cursor.close()
    return {"message": f"Connection to MySQL is successful! {data}"}

app.include_router(sample_router)
app.include_router(users.router, prefix="/api/v1")
app.include_router(auth_router, prefix="/api/v1")
