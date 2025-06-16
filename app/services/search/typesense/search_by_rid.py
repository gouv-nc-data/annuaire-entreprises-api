def search_by_rid(rid: str):

    search_parameters = {
        "q": rid,
        "query_by": "rid",
        "sort_by": "etat_rid:asc",
    }

    return search_parameters
