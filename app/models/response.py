from pydantic import BaseModel

from app.models.unite_legale import UniteLegaleResponse


class ResponseModel(BaseModel):
    results: list[UniteLegaleResponse] | None = None
    total_results: int = None
    page: int = None
    per_page: int = None
    total_pages: int = None
    execution_time: int | None = None
