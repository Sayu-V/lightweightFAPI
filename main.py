from fastapi import FastAPI
from models import Income, Expense, Budget

app = FastAPI()

# In-memory storage
incomes = []
expenses = []   # ✅ NEW
budget = 0   # ✅ NEW

@app.get("/")
def home():
    return {"message": "Finance API is running 🚀"}

# Income API
@app.post("/income")
def add_income(data: Income):
    incomes.append(data.amount)

    return {
        "message": "Income added successfully",
        "amount": data.amount,
        "source": data.source
    }

# ✅ NEW Expense API
@app.post("/expense")
def add_expense(data: Expense):
    expenses.append(data.amount)

    return {
        "message": "Expense added successfully",
        "amount": data.amount,
        "category": data.category
    }

# ✅ NEW Summary API
@app.get("/summary")
def get_summary():
    total_income = sum(incomes)
    total_expense = sum(expenses)
    balance = total_income - total_expense

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
    }


# -----------------------
# ✅ NEW Budget API
# -----------------------

@app.post("/budget")
def set_budget(data: Budget):
    global budget
    budget = data.limit

    return {
        "message": "Budget set successfully",
        "budget": budget
    }

@app.get("/budget-status")
def get_budget_status():
    total_expense = sum(expenses)
    remaining = budget - total_expense

    return {
        "budget": budget,
        "spent": total_expense,
        "remaining": remaining
    }
