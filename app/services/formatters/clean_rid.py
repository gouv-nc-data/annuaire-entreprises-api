def clean_rid(rid: str):
    if not rid:
        return
    
    clean_rid = rid.replace(" ", "")

    # Dinum rid : 0 122 531
    # if we're trying to search for 122 531, we need to add a 0 at the beginning
    # 122 531 -> 0122531
    if len(clean_rid) == 6:
        clean_rid = "0" + clean_rid

    # Dinum ridet : 0 122 531 001
    # if we're trying to search for 122 531 001, we need to add a 0 at the beginning
    # 122 531 001 -> 0122531
    elif len(clean_rid) == 9:
        clean_rid = "0" + clean_rid[0:6]
    elif len(clean_rid) == 10:
        clean_rid = clean_rid[0:7]

    return clean_rid
