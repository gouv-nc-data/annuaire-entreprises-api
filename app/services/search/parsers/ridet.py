import re


def is_ridet(query_string: str) -> bool:
    """
    Check if string is siret (composed of 14 digits).
    """
    if query_string is None:
        return False
    clean_query_string = query_string.replace(" ", "")
    # TODO might change this regex for correct ridet length
    ridet_valides = r"\b\d{6}\b"
    if re.search(ridet_valides, clean_query_string):
        return True
    return False
