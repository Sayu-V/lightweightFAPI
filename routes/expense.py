from fastapi import APIRouter, HTTPException
from app.models import Expense, MessageResponse

router = APIRouter()

expenses = []

@router.post("/expense", response_model=MessageResponse, tags=["Finance"])
def add_expense(data: Expense):
    if data.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than 0")

    expenses.append(data.amount)
    return {"message": "Expense added successfully"}
