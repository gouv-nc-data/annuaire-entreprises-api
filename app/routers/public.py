from fastapi import APIRouter, Request

from app.services.build_api_response import build_api_response

router = APIRouter()


@router.get("/recherche")
async def search_endpoint(request: Request):
    return build_api_response(request)


@router.get("/health")
def health_check():
    return {"status": "healthy"}
