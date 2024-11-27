def format_nom_complet(
    enseigne=None,
    designation=None,
):

    if not enseigne:
        nom_complet = ""
    else:
        nom_complet = enseigne

    # Add sigle if it exists
    if designation:
        nom_complet += f" ({designation})"

    return nom_complet.upper()
