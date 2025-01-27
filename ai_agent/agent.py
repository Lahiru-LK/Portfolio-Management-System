#agent.py
import requests
import json
from data.database import PortfolioDatabase  # Import the database class


class FinancialAgent:
    def __init__(self, host="http://127.0.0.1:11434", model="qwen2:0.5b", db=None):
        self.host = host
        self.api_url = f"{self.host}/api/generate"
        self.model = model
        self.db = db  # Database instance

    def fetch_portfolio_data(self):
        # Retrieve all securities in the portfolio from the database
        securities = self.db.get_all_securities()
        portfolio_data = []
        for sec in securities:
            portfolio_data.append({
                "name": sec[2],  # Security Name
                "sector": sec[6],  # Sector
                "risk": sec[7],  # Risk Level
                "price": sec[4],  # Price
                "share": sec[5]  # Share Percentage
            })
        return portfolio_data

    def consult(self, prompt):
        try:
            # If the query is related to portfolio, include real portfolio data
            if "portfolio" in prompt.lower():
                portfolio_data = self.fetch_portfolio_data()
                # Provide the AI model with the real data
                prompt += f"\nHere is the current portfolio: {portfolio_data}"

            response = requests.post(
                self.api_url,
                json={"model": self.model, "prompt": prompt},
                stream=True  # Enable streaming for large responses
            )

            if response.status_code == 200:
                messages = []
                for line in response.iter_lines():
                    if line:
                        try:
                            json_line = json.loads(line.decode('utf-8'))
                            messages.append(json_line.get("response", ""))
                            if json_line.get("done", False):  # Stop when response is complete
                                break
                        except json.JSONDecodeError:
                            continue  # Skip invalid JSON lines
                return "".join(messages)
            else:
                return f"Error: {response.status_code} - {response.reason}"
        except requests.exceptions.RequestException as e:
            return f"Error communicating with AI server: {e}"
