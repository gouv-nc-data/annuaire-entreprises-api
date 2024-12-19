def search_by_rid(rid: str):

    search_parameters = {
        "q": rid,
        "query_by": "rid",
    }

    return search_parameters
