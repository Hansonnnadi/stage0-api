from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import pytz

app = FastAPI()  # This should be here!

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins; you can restrict this later if needed
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods like GET, POST, etc.
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def get_info():
    current_datetime = datetime.now(pytz.UTC).isoformat()
    return {
        "email": "hanson2510@gmail.com",  # Replace with your actual email
        "current_datetime": current_datetime + 'Z',
        "github_url": "https://github.com/Hansonnnadi/stage0-api"  # Replace with your GitHub URL
    }    