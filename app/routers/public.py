from fastapi import APIRouter, Request
from app.controllers.search import search

router = APIRouter()


@router.get("/recherche")
async def search_text_endpoint(request: Request):
    print("request :", request)

    results = search(request)

    print('results : ', results)

    return {"result": "ok"}
