from fastapi.responses import ORJSONResponse

from app.controllers.search_params_builder import SearchParamsBuilder
from app.services.search.search_results import SearchResult
from app.models.response_builder import ResponseBuilder


def build_api_response(
    request,
) -> dict[str, int]:
    """Create and format API response.

    Args:
        request: HTTP request.
    Returns:
        response in json format (results, total_results, page, per_page,
        total_pages)
    """

    search_params = SearchParamsBuilder.get_search_params(request)
    search_results = SearchResult(search_params)
    formatted_response = ResponseBuilder(search_params, search_results)
    return ORJSONResponse(content=formatted_response.response)
