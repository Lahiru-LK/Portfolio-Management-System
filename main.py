# main.py (with bold, highlighted text, and spacing)

from controllers.portfolio_controller import add_stock, add_bond
from data.database import PortfolioDatabase
from ai_agent.agent import FinancialAgent  # Import the class
from views.display import display_portfolio_table, display_portfolio_graph, calculate_average_risk
from controllers.portfolio_risk import analyze_portfolio_risk
from controllers.portfolio_risk import validate_risk_level

# Initialize the database
db = PortfolioDatabase()

# Initialize the Financial Agent with the database connection
agent = FinancialAgent(db=db)

# ANSI escape codes for styling
BOLD = "\033[1m"
RESET = "\033[0m"
HIGHLIGHT = "\033[44m\033[97m"  # Blue background and white text
UNDERLINE = "\033[4m"

# Function to consult the AI financial agent
def consult_financial_agent():
    """
    Consult the AI financial agent with a user-defined query.
    """
    print(f"\n{BOLD}🧠 Consulting the AI Financial Agent...{RESET}")
    query = input(f"{HIGHLIGHT}Ask the financial agent a question (e.g., 'How can I balance my portfolio?'){RESET}: ")
    print(f"{HIGHLIGHT}🔍 Querying AI agent... Please wait...{RESET}")
    response = agent.consult(query)
    print(f"{HIGHLIGHT}💡 AI Response: {RESET}{response}\n")

# Risk level (global variable for simplicity)
risk_level = "Medium"  # Default value

def buy_security():
    validate_risk_level(db, risk_level)

def sell_security():
    validate_risk_level(db, risk_level)


def validate_risk_level(db, risk_level):

    securities = db.get_all_securities()  # Retrieve all portfolio securities
    if not securities:
        print(f"{HIGHLIGHT}🚫 No securities in the portfolio to validate risk level.{RESET}")
        return

    avg_risk = sum(sec[7] for sec in securities) / len(securities)  # Calculate the average risk
    print(f"{BOLD}📈 Average Portfolio Risk: {avg_risk:.2f}{RESET}")

    # Validate against the user-defined risk level
    if risk_level == "Low" and avg_risk > 2.5:
        print(f"{HIGHLIGHT}⚠️ Warning: Your portfolio is exceeding the Low Risk threshold.{RESET}")
    elif risk_level == "Medium" and (avg_risk < 2.51 or avg_risk > 4.5):
        print(f"{HIGHLIGHT}⚠️ Warning: Your portfolio is outside the Medium range.{RESET}")
    elif risk_level == "High" and avg_risk < 4.51:
        print(f"{HIGHLIGHT}⚠️ Warning: Your portfolio is not at the High risk limit.{RESET}")
    else:
        print(f"{BOLD}✅ Your portfolio is consistent with an appropriate level of risk.{RESET}")


def set_risk_level():
    global risk_level
    valid_levels = ["Low", "Medium", "High"]
    while True:
        risk_level = input(f"{BOLD}🔧 Enter desired risk level (Low/Medium/High): {RESET}").capitalize()
        if risk_level in valid_levels:
            print(f"{HIGHLIGHT}✔️ Risk level set to {risk_level}.{RESET}")
            break
        print(f"{HIGHLIGHT}❌ Invalid risk level. Please choose from Low, Medium, or High.{RESET}")

def buy_security():
    security_type = input(f"{BOLD}💼 Do you want to buy a Stock or a Bond? (Stock/Bond): {RESET}").capitalize()
    if security_type == "Stock":
        name = input(f"{BOLD}📝 Enter stock name: {RESET}")
        sector = input(f"{BOLD}🌐 Enter stock sector: {RESET}")
        price = float(input(f"{BOLD}💵 Enter stock price: {RESET}"))
        volatility = float(input(f"{BOLD}🌪️ Enter stock volatility: {RESET}"))
        stock_type = input(f"{BOLD}📊 Enter stock type (Common/Preferred): {RESET}").capitalize()
        add_stock(db, name, sector, price, volatility, stock_type)
    elif security_type == "Bond":
        name = input(f"{BOLD}📝 Enter bond name: {RESET}")
        sector = input(f"{BOLD}🌐 Enter bond sector: {RESET}")
        price = float(input(f"{BOLD}💵 Enter bond price: {RESET}"))
        bond_type = input(f"{BOLD}📊 Enter bond type (Government/Corporate): {RESET}").capitalize()
        add_bond(db, name, sector, price, bond_type)
    else:
        print(f"{HIGHLIGHT}❌ Invalid security type. Please choose Stock or Bond.{RESET}")

def sell_security():
    securities = db.get_all_securities()
    if not securities:
        print(f"{HIGHLIGHT}🚫 No securities available in the portfolio to sell.{RESET}")
        return

    print(f"\n{BOLD}📜 Portfolio Table:{RESET}")
    print(f"{'ID':<5} {'Name':<15} {'Ticker':<10} {'Price ($)':<10} {'Share (%)':<10} {'Risk':<5}")
    print("-" * 70)
    for sec in securities:
        print(f"{sec[0]:<5} {sec[2]:<15} {sec[3]:<10} {sec[4]:<10.2f} {sec[5]:<10.2f} {sec[7]:<5.2f}")

    try:
        row_id = int(input(f"{BOLD}🔢 Enter the ID of the security to sell: {RESET}"))
        if db.delete_by_id(row_id):
            print(f"{HIGHLIGHT}✅ Security with ID {row_id} has been sold.{RESET}")
            # Validate risk level after selling a security
            validate_risk_level(db, risk_level)
        else:
            print(f"{HIGHLIGHT}❌ Failed to sell security with ID {row_id}. {RESET}")
    except ValueError:
        print(f"{HIGHLIGHT}❌ Invalid input. Please enter a numeric ID.{RESET}")

def calculate_portfolio_risk():
    securities = db.get_all_securities()
    if not securities:
        print(f"{HIGHLIGHT}🚫 No securities in the portfolio to calculate risk.{RESET}")
        return
    avg_risk = calculate_average_risk(securities)
    print(f"\n{BOLD}📊 Average Portfolio Risk: {avg_risk:.2f}{RESET}")

def menu():
    print(f"\n{BOLD}{HIGHLIGHT}🌟 Portfolio Manager 🌟{RESET}\n")
    print(f"1. Set Risk Level 🔧")
    print(f"2. Buy Stock or Bond 💼")
    print(f"3. Sell Stock or Bond 💸")
    print(f"4. Display Portfolio Table 📜")
    print(f"5. Display Portfolio Graph 📊")
    print(f"6. Consult Financial Agent 🤖")
    print(f"7. Display Average Portfolio Risk 📈")
    print(f"8. Exit 🚪")

def main():
    while True:
        menu()
        choice = input(f"{BOLD}🔘 Enter your choice: {RESET}")

        if choice == "1":
            set_risk_level()

        elif choice == "2":
            buy_security()

        elif choice == "3":
            sell_security()

        elif choice == "4":
            securities = db.get_all_securities()
            display_portfolio_table(securities)

        elif choice == "5":
            securities = db.get_all_securities()
            display_portfolio_graph(securities)

        elif choice == "6":
            consult_financial_agent()  # Now this is correctly referenced

        elif choice == "7":
            calculate_portfolio_risk()

        elif choice == "8":
            print(f"{HIGHLIGHT}👋 Goodbye!{RESET}")
            break

        else:
            print(f"{HIGHLIGHT}❌ Invalid choice. Please try again.{RESET}")

if __name__ == "__main__":
    main()
