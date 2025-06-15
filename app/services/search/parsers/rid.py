import re


def is_rid(query_string: str) -> bool:
    """
    Check if string is rid (composed of 7 digits).
    """
    if query_string is None:
        return False
    clean_query_string = query_string.replace(" ", "")
    
    # Checking if rid is 6 digits, if so, add a 0 at the beginning
    if len(clean_query_string) == 6:
        clean_query_string = "0" + clean_query_string

    rid_valides = r"\b\d{7}\b"
    if re.search(rid_valides, clean_query_string):
        return True
    return False
