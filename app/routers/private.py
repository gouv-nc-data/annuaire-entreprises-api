from fastapi import APIRouter, Request

from app.typesense.create_collections_and_documents import (
    create_collections_and_documents,
)

router = APIRouter()


@router.post("/typesense/init", status_code=201)
async def typesense_init(request: Request):
    create_collections_and_documents()
    return {"status": "ok"}
