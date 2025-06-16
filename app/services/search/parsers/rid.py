import re


def is_rid(query_string: str) -> bool:
    """
    Check if string is rid (composed of 7 digits).
    """
    if query_string is None:
        return False

    rid_valides = r"\b\d{7}\b"
    if re.search(rid_valides, query_string):
        return True
    return False
