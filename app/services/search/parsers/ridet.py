import re


def is_ridet(query_string: str) -> bool:
    """
    Check if string is siret (composed of 14 digits).
    """
    if query_string is None:
        return False
    clean_query_string = query_string.replace(" ", "")
    ridet_valides = r"\b\d{10}\b"
    if re.search(ridet_valides, clean_query_string):
        return True
    return False
