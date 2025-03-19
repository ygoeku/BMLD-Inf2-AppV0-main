from utils import helpers

def calculate_mch(hgb, erythrozyten, timezone='Europe/Zurich'):
    """
    Berechnet den MCH-Wert (Mean Corpuscular Hemoglobin) und gibt ein Dictionary mit den Eingaben, 
    dem berechneten MCH-Wert, der Kategorie und dem Zeitstempel zurück.

    Args:
        hgb (float): Hämoglobin in g/dl.
        erythrozyten (float): Erythrozytenanzahl in Millionen/µl.
        timezone (str): Zeitzone für den Zeitstempel (Standard: Europe/Zurich).

    Returns:
        dict: Ein Dictionary mit den Eingaben, dem MCH-Wert, der Kategorie und dem Zeitstempel.
    """
    if hgb <= 0 or erythrozyten <= 0:
        raise ValueError("Hämoglobin und Erythrozytenanzahl müssen positive Werte sein.")

    # MCH-Formel: MCH = (Hämoglobin / Erythrozytenanzahl) * 10
    mch = (hgb / erythrozyten) * 10

    # Bestimmung der Kategorie basierend auf Referenzwerten
    if mch < 26:
        category = 'Niedrig (Hypochromie)'
    elif mch > 33:
        category = 'Hoch (Hyperchromie)'
    else:
        category = 'Normal'

    result_dict = {
        "timestamp": helpers.ch_now(),
        "hgb": hgb,
        "erythrozyten": erythrozyten,
        "mch": round(mch, 2),
        "category": category,
    } 

    return result_dict

