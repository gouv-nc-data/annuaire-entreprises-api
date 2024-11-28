from app.services.search.parsers.rid import is_rid
from app.services.search.parsers.ridet import is_ridet
from app.services.search.queries.search_by_rid import search_by_rid
from app.services.search.queries.search_by_text import search_by_text


def build_search(search_build):
    query_terms = search_build.search_params.terms

    if is_rid(query_terms):
        search_build.search_client = search_by_rid(query_terms)
    elif is_ridet(query_terms):
        # We're doing a rid search for a ridet like term
        # We will return the enterprise associated with the `établissement` rid | et
        search_build.search_client = search_by_rid(query_terms[0:7])
    elif query_terms is not None:
        search_build.search_client = search_by_text(search_build.search_params)
    else:
        search_build.search_client = None
