from fastapi import APIRouter, HTTPException
from app.models import Expense, MessageResponse

router = APIRouter()

# Store full expense object now (not just amount)
expenses = []

@router.post("/expense", response_model=MessageResponse, tags=["Finance"])
def add_expense(data: Expense):
    if data.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than 0")

    expenses.append({
        "amount": data.amount,
        "category": data.category
    })

    return {"message": "Expense added successfully"}
