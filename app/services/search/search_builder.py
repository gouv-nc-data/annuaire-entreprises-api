from app.services.formatters.clean_rid import clean_rid
from app.services.search.parsers.rid import is_rid
from app.services.search.parsers.ridet import is_ridet
from app.services.search.queries.search_by_rid import search_by_rid
from app.services.search.typesense.search_by_text import search_by_text
from app.services.search.typesense.search_person import search_person


def build_search(search_build):
    query_terms = search_build.search_params.terms

    # We're cleaning the query terms to make sure they are in the correct format
    # to verify if it's a rid or a ridet
    clean_ridet_query_terms = clean_rid(query_terms)

    if is_rid(clean_ridet_query_terms):
        search_build.search_client = "sqlalchemy"
        search_build.search_query = search_by_rid(clean_ridet_query_terms)
    elif is_ridet(clean_ridet_query_terms):
        search_build.search_client = "sqlalchemy"
        search_build.search_query = search_by_rid(clean_ridet_query_terms)
    elif search_build.search_params.dirigeant:
        search_build.search_client = "typesense"
        search_build.search_query = search_person(search_build.search_params)
    elif query_terms is not None:
        search_build.search_client = "typesense"
        search_build.search_query = search_by_text(search_build.search_params)
    else:
        search_build.search_client = "typesense"
        search_build.search_query = None
