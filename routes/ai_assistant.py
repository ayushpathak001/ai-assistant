from fastapi import APIRouter
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

from system_instruction import system_instruction


load_dotenv()


router = APIRouter(
    prefix="/ai",
    tags=["AI Assistant"]
)


NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY", "")


client = OpenAI(
    api_key=NVIDIA_API_KEY,
    base_url="https://integrate.api.nvidia.com/v1"
)


class ChatRequest(BaseModel):
    user_id: str
    message: str


# Temporary memory
user_sessions = {}


@router.post("/chat")
async def chat(request: ChatRequest):

    user_id = request.user_id

    # --------------------------------
    # Create conversation for user
    # --------------------------------

    if user_id not in user_sessions:

        user_sessions[user_id] = [
            {
                "role": "system",
                "content": system_instruction
            }
        ]


    conversation = user_sessions[user_id]


    # --------------------------------
    # Add current user context
    # --------------------------------

    user_message = f"""
Current beekeeper ID: {user_id}

User question:
{request.message}

Answer according to the data available
for {user_id} in the system instruction.
"""


    conversation.append({
        "role": "user",
        "content": user_message
    })


    # --------------------------------
    # Call NVIDIA model
    # --------------------------------

    try:

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=conversation
        )


        answer = response.choices[0].message.content


        # Remember AI response
        conversation.append({
            "role": "assistant",
            "content": answer
        })


        return {
            "user_id": user_id,
            "response": answer
        }


    except Exception as e:

        # Remove failed message
        conversation.pop()

        return {
            "error": str(e)
        }