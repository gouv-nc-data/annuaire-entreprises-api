from typesense import Client

from app.controllers.search_params_model import SearchParams


def execute_typesense_query(client: Client, search_client, search_params: SearchParams):
    print("RIDET TO LOOK FOR ", search_params.terms)

    page = search_params.page
    per_page = search_params.per_page
    offset = 0

    if page > 1:
        offset = (page - 1) * per_page

    search_parameters = {
        "q": search_params.terms,
        "query_by": "rid",
        "per_page": per_page,
        "page": page,
    }

    result = client.collections["entreprise"].documents.search(search_parameters)
    total_results = result["found"]

    print("---RESULT---", result["hits"])
    print("---RESULT FOUND ---", result["found"])

    return {"total_results": total_results, "results": result["hits"]}
