
from fastapi import APIRouter, HTTPException
from app.models import Income, MessageResponse

router = APIRouter()

incomes = []

@router.post("/income", response_model=MessageResponse, tags=["Finance"])
def add_income(data: Income):
    if data.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than 0")

    incomes.append(data.amount)
    return {"message": "Income added successfully"}
