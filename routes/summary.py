from fastapi import APIRouter
from app.models import SummaryResponse
from app.routes.income import incomes
from app.routes.expense import expenses

router = APIRouter()

@router.get("/summary", response_model=SummaryResponse, tags=["Finance"])
def get_summary():
    return {
        "total_income": sum(incomes),
        "total_expense": sum(expenses),
        "balance": sum(incomes) - sum(expenses)
    }
