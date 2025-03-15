import math

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

    def __str__(self):
        return f"Lokalita: {self.name}, Koeficient: {self.locality_coefficient}"

class Property:
    def __init__(self, locality: Locality):
        self.locality = locality

    def __str__(self):
        return f"Nemovitost v lokalitě: {self.locality.name}"

class Estate(Property):
    estate_type_coefficiens = {"land": 0.85, "building site": 9, "forrest": 0.35, "garden": 2}

    def __init__(self, locality: Locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area

    def calculate_tax(self) -> int:
        tax = self.area * self.locality.locality_coefficient * 15
        if self.commercial:
            tax *=2
        return math.ceil(tax)
 
    def __str___(self):
        return (f"Pozemek ({self.estate_type}) v lokalitě {self.locality.name} s plochou {self.area} m2. Daň: {self.calculate_tax()} Kč.")
 
class Residence(Property):
        def __init__(self, locality: Locality, area, commercial):
            super().__init__(locality)
            self.area = area
            self.commercial = commercial
        def calculate_tax(self) -> int:
            tax = self.area * self.locality.locality_coefficient * 15
            if self.commercial:
                tax *= 2
            return math.ceil(tax)
        def __str__(self):
            type_desc = "Komerční nemovitost" if self.commercial else "Rezidenční nemovitost"
            return (f"{type_desc} v lokalitě {self.locality.name} s plochou {self.area} m2. Daň: {self.calculate_tax()} Kč.")

manetin = Locality ("Manětín", 0.8)
brno = Locality ("Brno", 3)

zemedelsky_pozemek = Estate(manetin, "land", 900)
dum = Residence(manetin, 120, False)
kancelar = Residence(brno, 90, True)

print(zemedelsky_pozemek)
print(dum)
print(kancelar)
