def format_nom_complet(
    sigle=None,
    designation=None,
):

    if not sigle:
        nom_complet = ""
    else:
        nom_complet = sigle

    # Add sigle if it exists
    if designation:
        nom_complet += f" ({designation})"

    return nom_complet.upper()
