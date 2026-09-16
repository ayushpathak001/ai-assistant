from fastapi import FastAPI

from routes.ai_assistant import router as ai_router


app = FastAPI()


app.include_router(ai_router)