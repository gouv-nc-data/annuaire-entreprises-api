def format_adresse_complete(
    adresse=None,
    ville=None,
    code_postal=None,
):
    if not adresse:
        return None

    adresse_complete = adresse

    # Add sigle if it exists
    if ville:
        adresse_complete += f", {ville}"

    if code_postal:
        adresse_complete += f", {code_postal}"

    return adresse_complete
