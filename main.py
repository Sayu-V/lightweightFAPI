from fastapi import FastAPI, HTTPException
from models import Income, Expense, Budget
from app.routes import income, expense, summary, budget

app = FastAPI()

incomes = []
expenses = []
budget = 0

@app.post("/income")
def add_income(data: Income):
    if data.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than 0")

    incomes.append(data.amount)
    return {"message": "Income added successfully"}

@app.post("/expense")
def add_expense(data: Expense):
    if data.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than 0")

    expenses.append(data.amount)
    return {"message": "Expense added successfully"}

@app.get("/summary")
def get_summary():
    return {
        "total_income": sum(incomes),
        "total_expense": sum(expenses),
        "balance": sum(incomes) - sum(expenses)
    }

@app.post("/budget")
def set_budget(data: Budget):
    global budget
    budget = data.limit
    return {"message": "Budget set successfully"}

@app.get("/budget-status")
def get_budget_status():
    total_expense = sum(expenses)
    return {
        "budget": budget,
        "spent": total_expense,
        "remaining": budget - total_expense
    }
# Include routers
app.include_router(income.router)
app.include_router(expense.router)
app.include_router(summary.router)
app.include_router(budget.router)

# ✅ ADD HEALTH CHECK HERE
@app.get("/health", tags=["System"])
async def health_check():
    return {"status": "API is running"}
