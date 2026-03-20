def darf_achterbahn_fahren(groesse):
    """
    Überprüft ob eine Person Achterbahn fahren darf.
    
    Args:
        groesse: Körpergröße in cm
        
    Returns:
        bool: True wenn größer als 150 cm, sonst False
    """
    return groesse > 150


# Beispiel Nutzung
if __name__ == "__main__":
    groesse = float(input("Geben Sie Ihre Größe in cm ein: "))
    
    if darf_achterbahn_fahren(groesse):
        print("✓ Du darfst Achterbahn fahren!")
    else:
        print("✗ Du musst mindestens 150 cm groß sein.")