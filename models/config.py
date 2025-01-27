# config.py

# Config for sector and volatility risks

SECTOR_RISK = {
    "Technology": 6,
    "Finance": 3,
    "Government": 2,
    "Energy": 4,
    "Healthcare": 4,
    "Real Estate": 2,
    "Consumer Goods": 1,
    "Default": 1  # Default risk if sector not listed
}

VOLATILITY_RISK = {
    "Low": 1,
    "High": 2,
    "Default": 1  # Default risk if volatility not listed
}
