from pydantic import BaseModel

class Income(BaseModel):
    amount: float

class Expense(BaseModel):
    amount: float

class Budget(BaseModel):
    limit: float

# Response Models
class MessageResponse(BaseModel):
    message: str

class SummaryResponse(BaseModel):
    total_income: float
    total_expense: float
    balance: float

class BudgetResponse(BaseModel):
    budget: float
    spent: float
    remaining: float

class Expense(BaseModel):
    amount: float
    category: str
