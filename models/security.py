#security.py

from models.config import SECTOR_RISK, VOLATILITY_RISK

class Security:
    """
    Base class for all securities. Provides a structure for common attributes and methods.
    """
    def __init__(self, name, sector, price, volatility=None, risk=None):
        self.name = name
        self.sector = sector
        self.price = price
        self.volatility = volatility
        self.risk = risk

    def calculate_risk(self):
        """
        Calculate risk based on sector, volatility, and type.
        Must be implemented in subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")


class Stock(Security):
    """
    Stock class extending Security. Includes specific logic for calculating risk for stocks.
    """
    def __init__(self, name, sector, price, volatility):
        super().__init__(name, sector, price, volatility)
        self.calculate_risk()

    def calculate_risk(self):
        """
        Calculate risk for stocks using weighted risk formula:
            Risk = 0.5 * sector_risk + 0.3 * volatility_risk + 0.2 * type_risk
        """
        sector_risk = SECTOR_RISK.get(self.sector, SECTOR_RISK["Default"])
        volatility_risk = VOLATILITY_RISK.get(self.volatility, VOLATILITY_RISK["Default"])
        type_risk = 1  # Stock type risk is fixed
        self.risk = (0.5 * sector_risk) + (0.3 * volatility_risk) + (0.2 * type_risk)


class Bond(Security):
    """
    Bond class extending Security. Includes specific logic for calculating risk for bonds.
    """
    def __init__(self, name, sector, price, bond_type):
        super().__init__(name, sector, price)
        self.bond_type = bond_type
        self.calculate_risk()

    def calculate_risk(self):
        """
        Calculate risk for bonds using weighted risk formula:
            Risk = 0.5 * sector_risk + 0.3 * volatility_risk + 0.2 * type_risk
        """
        sector_risk = SECTOR_RISK.get(self.sector, SECTOR_RISK["Default"])
        volatility_risk = 1  # Default volatility risk for bonds
        type_risk = 0.5 if self.bond_type == "Government" else 0.1 if self.bond_type == "Corporate" else 1
        self.risk = (0.5 * sector_risk) + (0.3 * volatility_risk) + (0.2 * type_risk)


class CommonStock(Stock):
    """
    Common Stock class extending Stock.
    """
    def __init__(self, name, sector, price, volatility):
        super().__init__(name, sector, price, volatility)


class PreferredStock(Stock):
    """
    Preferred Stock class extending Stock. Includes dividend priority attribute.
    """
    def __init__(self, name, sector, price, volatility, dividend_priority=True):
        super().__init__(name, sector, price, volatility)
        self.dividend_priority = dividend_priority
