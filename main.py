from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.ai_assistant import router as ai_router

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://honey-assist.vercel.app" ,
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ai_router)
