# 📊 Portfolio Management System

Welcome to the **Portfolio Management System**! This project is a robust, local AI-powered portfolio management solution, leveraging SQLite for data storage and Ollama AI models to provide advanced financial insights and recommendations.

---

https://github.com/user-attachments/assets/6c1f718a-ed9a-4e0c-a234-1b37d975a71b
![image](https://github.com/user-attachments/assets/504e9eb4-8695-441c-aaad-657e45e36d77)



## 🔧 Key Features

### 📈 Portfolio Management:
- Buy and sell **stocks** and **bonds**.
- Set and validate risk levels (Low, Medium, High) for your portfolio.
- Analyze and display your portfolio composition using tables and graphs.

### 🤖 AI-Powered Insights (via Ollama):
- Query the financial AI agent for personalized advice (e.g., "What is the highest-risk stock in my portfolio?").
- Natural language interaction for portfolio management and financial insights.
- The AI accesses and analyzes data from the **SQLite database** in real-time.

### 🔍 Local Deployment:
- Fully local system powered by the **Ollama AI model**.
- Data privacy and no reliance on external cloud services.

### 🔗 Integration with SQLite:
- Database-driven architecture for storing and retrieving portfolio data.
- Seamlessly integrated with the AI for real-time analysis.

---

## 📚 Project Structure

```
portfolio_project/
|-- .venv/                 # Virtual environment
|-- ai_agent/
|   |-- agent.py          # AI-powered financial agent logic
|-- controllers/
|   |-- portfolio_controller.py  # Portfolio management logic
|   |-- portfolio_risk.py         # Risk management functions
|-- data/
|   |-- database.py        # SQLite database connection
|   |-- portfolio.db       # SQLite database file
|-- models/
|   |-- bond.py            # Bond-related data models
|   |-- config.py          # Configuration and constants
|   |-- security.py        # Base class for securities
|   |-- stock.py           # Stock-related data models
|-- views/
|   |-- display.py         # Graphical and tabular display logic
|-- main.py                # Entry point of the application
```

---

## 🚀 How It Works

1. **Portfolio Setup:**
   - Define a risk level (Low, Medium, High).
   - Add securities (stocks or bonds) to your portfolio.

2. **AI Assistance:**
   - Use the Ollama-powered AI agent to get insights, such as risk analysis or suggestions for portfolio optimization.

3. **Data Visualization:**
   - View your portfolio in a **table** or as a **graph** to understand the risk composition and distribution.

4. **Database Integration:**
   - All data is stored in `portfolio.db`, an SQLite database. The AI reads from and writes to this database seamlessly.

---

## 🔄 Ollama AI Integration

This project utilizes Ollama’s advanced AI models to:
- **Answer financial queries:** Ask the AI about the performance, risk, or details of your portfolio (e.g., "Which stock has the lowest risk?").
- **Analyze data:** Process your portfolio’s structure and provide insights based on historical data and risk models.

### Example Queries:
- "What is the average risk of my portfolio?"
- "How can I balance my portfolio to minimize risk?"
- "What is the highest-risk stock in my portfolio?"

---

## 🔢 Technologies Used

- **Python**: Core programming language.
- **SQLite**: Database for storing portfolio data.
- **Matplotlib**: For graph generation and visualization.
- **Ollama AI Models**: Advanced AI integration for financial insights.

---

## 🛠️ Installation & Setup

### Prerequisites:
- Python 3.10+
- Ollama AI installed locally.

### Steps:
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/portfolio_project.git
   ```

2. Set up the virtual environment:
   ```bash
   cd portfolio_project
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python main.py
   ```

---

## 🌐 Screenshots

### Main Menu
![image](https://github.com/user-attachments/assets/c32b1ce1-45c0-45f5-950b-534b9528e010)


### Portfolio Table
![image](https://github.com/user-attachments/assets/d75027bd-ac8b-45bc-9d28-fdd28bbaece3)


### Risk Graph
![image](https://github.com/user-attachments/assets/dc0fa80a-f8e0-416a-a86a-1b12839443d3)


### AI Query Example
![image](https://github.com/user-attachments/assets/8b70f0ba-3bdb-4ca0-b63c-efaaaa855663)


---

## 📊 Example Use Cases

### Use Case 1: Query AI for Portfolio Risk
Ask the AI: "What is the risk level of my current portfolio?" The AI will analyze the data in `portfolio.db` and provide a detailed response, including the weighted risk score and suggestions for improvement.

### Use Case 2: Visualize Portfolio
Select the "Display Portfolio Graph" option to view the composition and risk distribution of your portfolio.

### Use Case 3: Consult Financial Agent
Interact with the AI agent for tailored financial advice, using Ollama’s conversational capabilities.

---

## 🚧 Limitations
- **Single User**: The system supports only one user.
- **Local AI**: AI interactions are limited to the locally deployed Ollama model.
- **Simplified Risk Models**: Advanced risk calculations (e.g., market predictions) are not implemented.

---

## 📢 Future Enhancements
- Support for multiple users and authentication.
- Integration with real-time stock market APIs.
- Enhanced AI models for market trend predictions.

---

## 🙏 Acknowledgments
This project is built as part of an academic assignment in **Object-Oriented Programming and Python**. Special thanks to Ollama for providing robust local AI model support.

---

## 🚀 Get Started Today!
Clone the repository and take your first step into AI-powered portfolio management! Let us know your thoughts and suggestions. Happy investing! 🚀

