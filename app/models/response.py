from pydantic import BaseModel

from app.models.entreprise import EntrepriseResponse


class ResponseModel(BaseModel):
    results: list[EntrepriseResponse] | None = None
    total_results: int = None
    page: int = None
    per_page: int = None
    total_pages: int = None
    execution_time: int | None = None
