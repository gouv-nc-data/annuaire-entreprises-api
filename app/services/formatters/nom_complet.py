def format_nom_complet(
    enseigne=None,
    designation=None,
):

    if not designation:
        nom_complet = ""
    else:
        nom_complet = designation

    # Add sigle if it exists
    if enseigne:
        nom_complet += f" ({enseigne})"

    return nom_complet.upper()
