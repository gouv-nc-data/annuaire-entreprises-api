from fastapi import APIRouter, Request
from pydantic import BaseModel, EmailStr

router = APIRouter()


# Define the request body schema
class EmailRequest(BaseModel):
    email: EmailStr


@router.post("/agent-public/signup")
async def agent_plubic_signup(email_request: EmailRequest):
    try:
        email = email_request.email

        with open("emails.txt", "a") as file:
            file.write(email + "\n")

        return {"success": True}
    except Exception as e:
        return {"success": False}
