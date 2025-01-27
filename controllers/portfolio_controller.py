#portfolio_controller.py

from models.stock import CommonStock, PreferredStock
from models.bond import GovernmentBond, CorporateBond

def add_stock(db, name, sector, price, volatility, stock_type="Common"):
    stock = CommonStock(name, sector, price, volatility) if stock_type == "Common" else PreferredStock(name, sector, price, volatility)
    ticker = name[:3].upper()
    db.add_security("Stock", stock.name, ticker, stock.price, 1, stock.sector, stock.risk)
    print(f"Stock '{name}' added with risk {stock.risk:.2f}.")

def add_bond(db, name, sector, price, bond_type):
    bond = GovernmentBond(name, sector, price) if bond_type == "Government" else CorporateBond(name, sector, price)
    ticker = name[:3].upper()
    db.add_security("Bond", bond.name, ticker, bond.price, 1, bond.sector, bond.risk)
    print(f"Bond '{name}' added with risk {bond.risk:.2f}.")

def add_security(db, security_type, name, sector, price, **kwargs):

    if security_type == "Stock":
        stock_type = kwargs.get("stock_type", "Common")
        volatility = kwargs.get("volatility", "Low")
        stock = CommonStock(name, sector, price, volatility) if stock_type == "Common" else PreferredStock(name, sector, price, volatility)
        ticker = name[:3].upper()
        db.add_security("Stock", stock.name, ticker, stock.price, 1, stock.sector, stock.risk)
        print(f"Stock '{name}' added with risk {stock.risk:.2f}.")
    elif security_type == "Bond":
        bond_type = kwargs.get("bond_type", "Government")
        bond = GovernmentBond(name, sector, price) if bond_type == "Government" else CorporateBond(name, sector, price)
        ticker = name[:3].upper()
        db.add_security("Bond", bond.name, ticker, bond.price, 1, bond.sector, bond.risk)
        print(f"Bond '{name}' added with risk {bond.risk:.2f}.")
