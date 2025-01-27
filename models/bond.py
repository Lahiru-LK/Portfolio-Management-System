#bond.py

from models.security import Security

class Bond(Security):
    def __init__(self, name, sector, price, bond_type):
        super().__init__(name, sector, price)
        self.bond_type = bond_type
        self.calculate_risk()

    def calculate_risk(self):
        sector_risk = {"Finance": 3, "Government": 2}.get(self.sector, 1)
        if self.bond_type == "Government":
            self.risk = sector_risk * 0.5
        else:  # Corporate
            self.risk = sector_risk * 0.1

class GovernmentBond(Bond):
    def __init__(self, name, sector, price):
        super().__init__(name, sector, price, "Government")

class CorporateBond(Bond):
    def __init__(self, name, sector, price):
        super().__init__(name, sector, price, "Corporate")
