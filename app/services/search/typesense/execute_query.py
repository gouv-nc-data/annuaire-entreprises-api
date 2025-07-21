from typesense import Client

from app.controllers.search_params_model import SearchParams
from app.controllers.field_validation import VALID_FIELD_VALUES


def execute_typesense_query(client: Client, search_client, search_params: SearchParams):
    page = search_params.page
    per_page = search_params.per_page

    filter_by_array = []

    print("search_params", search_params)

    search_options = {
        "page": page,
        "per_page": per_page,
    }

    if search_client is not None:
        if search_client["q"] is not None:
            search_options["q"] = search_client["q"]

        if search_client["query_by"] is not None:
            search_options["query_by"] = search_client["query_by"]

        if search_client["sort_by"] is not None:
            search_options["sort_by"] = search_client["sort_by"]

    else:
        search_options["q"] = "*"

    for key, value in search_params:

        field = VALID_FIELD_VALUES.get(key)

        if isinstance(field, dict):
            alias = field["alias"]
            if alias is not None:
                if value is not None:
                    if len(filter_by_array) == 0:
                        filter_by_array.append(f"{alias}:{value}")
                    else:
                        filter_by_array.append(f"&&{alias}:{value}")

                    if alias == "ville_physique":
                        filter_by_array.append(f"||etablissements.{alias}:{value}")

    if len(filter_by_array) != 0:
        search_options["filter_by"] = "".join(filter_by_array)

    result = client.collections["entreprises"].documents.search(search_options)
    total_results = result["found"]

    return {"total_results": total_results, "results": result["hits"]}
