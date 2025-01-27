#stock.py

from models.security import Security

class Stock(Security):
    def __init__(self, name, sector, price, volatility):
        super().__init__(name, sector, price)
        self.volatility = volatility
        self.calculate_risk()

    def calculate_risk(self):
        sector_risk = {"Technology": 6, "Finance": 3}.get(self.sector, 1)
        self.risk = sector_risk + self.volatility

class CommonStock(Stock):
    def __init__(self, name, sector, price, volatility):
        super().__init__(name, sector, price, volatility)

class PreferredStock(Stock):
    def __init__(self, name, sector, price, volatility, dividend_priority=True):
        super().__init__(name, sector, price, volatility)
        self.dividend_priority = dividend_priority
