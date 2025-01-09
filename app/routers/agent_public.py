from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

from app.services.agent_public.signup import signup

router = APIRouter()


# Define the request body schema
class EmailRequest(BaseModel):
    email: EmailStr
    reason: str


@router.post("/agent-public/signup")
async def agent_plubic_signup(email_request: EmailRequest):

    print('agent publique', email_request)

    try:
        email = email_request.email
        reason = email_request.reason

        signup(email, reason)

        return {"success": True}
    except Exception:
        return {"success": False}
