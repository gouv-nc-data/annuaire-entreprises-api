from app.services.search.parsers.ridet import is_ridet


def build_search(search_build):
    query_terms = search_build.search_params.terms

    print("query terms : ", query_terms)

    if is_ridet(query_terms):
        search_build.search_kind = 'ridet'
        print("query terms are ridet like")
