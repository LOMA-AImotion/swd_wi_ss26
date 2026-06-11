class MQB:
    def __init__(self, fahrgestellnr, hubraum, leistung, farbe, nr_türen):
        self.fahrgestellnr = fahrgestellnr
        self.hubraum = hubraum
        self.leistung = leistung
        self.farbe = farbe
        self.nr_türen = nr_türen

    def türgeräusch(self):
        print("Generisches Türgeräusch")

    def blinkergeräusch(self):
        print("Generisches Blinkergeräusch")

    def print_info(self):
        info = (
            f"Fahrgestellnummer: {self.fahrgestellnr}\n"
            f"Hubraum: {self.hubraum} L\n"
            f"Leistung: {self.leistung} PS\n"
            f"Farbe: {self.farbe}\n"
            f"Anzahl Türen: {self.nr_türen}"
        )
        print(info)


class VW_Golf(MQB):
    def __init__(self, fahrgestellnr, hubraum, leistung, farbe, nr_türen, gti=False):
        super().__init__(fahrgestellnr, hubraum, leistung, farbe, nr_türen)
        self.gti = False
    
class Audi_A3(MQB):
    def __init__(self, fahrgestellnr, hubraum, leistung, farbe, nr_türen, quattro=True):
        super().__init__(fahrgestellnr, hubraum, leistung, farbe, nr_türen)
        self.quattro = quattro

    # Polymorphismus
    def türgeräusch(self):
        print("Super premium Audi Türgeräusch")

    def blinkergeräusch(self):
        print("Super premium Audi Blinkergeräusch")

class Seat_Leon(MQB):
    def __init__(self, fahrgestellnr, hubraum, leistung, farbe, nr_türen, sportfahrwerk=True):
        super().__init__(fahrgestellnr, hubraum, leistung, farbe, nr_türen)
        self.sportfahrwerk = sportfahrwerk

a3_1 = Audi_A3(1234, 1.3, 115, "blau", 5)
a3_1.print_info()
a3_1.türgeräusch()

golf_1 = VW_Golf(6789, 1.0, 100, "schwarz", 5)
golf_1.print_info()
golf_1.türgeräusch()
