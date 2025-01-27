#portfolio_risk.py

def analyze_portfolio_risk(securities):
    """
    Analyze and calculate the portfolio's average risk.

    :param securities: A list of securities from the database.
    :return: A string indicating the portfolio's risk level.
    """
    if not securities:
        return "No securities in the portfolio to calculate risk."

    total_risk = sum(sec[7] for sec in securities)
    avg_risk = total_risk / len(securities)

    if avg_risk > 5:
        return "Your portfolio has high risk. Consider diversifying."
    return "Your portfolio risk is moderate or low."


def validate_risk_level(risk_level, db):
    """
    Validate the portfolio's average risk level against the user-defined risk level.

    :param risk_level: The user-defined risk level ("Low", "Medium", "High").
    :param db: The database instance.
    """
    securities = db.get_all_securities()  # Retrieve all portfolio securities
    if not securities:
        print("No securities in the portfolio to validate risk level.")
        return

    avg_risk = sum(sec[7] for sec in securities) / len(securities)  # Calculate the average risk
    print(f"Average Portfolio Risk: {avg_risk:.2f}")

    # Validate against the user-defined risk level
    if risk_level == "Low" and avg_risk > 2.5:
        print("Warning: Your portfolio is exceeding the Low Risk threshold.")
    elif risk_level == "Medium" and (avg_risk < 2.51 or avg_risk > 4.5):
        print("Warning: Your portfolio is outside the Medium range.")
    elif risk_level == "High" and avg_risk < 4.51:
        print("Warning: Your portfolio is not at the High risk limit.")
    else:
        print("Your portfolio is consistent with an appropriate level of risk.")
