
from fastapi import APIRouter
from app.models import Budget, BudgetResponse, MessageResponse
from app.routes.expense import expenses

router = APIRouter()

budget = 0

@router.post("/budget", response_model=MessageResponse, tags=["Finance"])
def set_budget(data: Budget):
    global budget
    budget = data.limit
    return {"message": "Budget set successfully"}

@router.get("/budget-status", response_model=BudgetResponse, tags=["Finance"])
def get_budget_status():
    total_expense = sum(expenses)
    return {
        "budget": budget,
        "spent": total_expense,
        "remaining": budget - total_expense
    }
