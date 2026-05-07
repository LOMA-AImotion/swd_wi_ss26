def flaeche(breite: int, laenge: int, preis_pro_qm: int = 5, 
            steuersatz: float, waehrung: str) -> int:
    return str(breite * laenge * preis_pro_qm * steuersatz) + waehrung

print(flaeche(10, 20, 0.19, "USD"))