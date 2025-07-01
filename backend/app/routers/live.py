from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas import CustomerCreate, Customer
from ..models import Customer as CustomerModel
from ..database import get_db

router = APIRouter()

@router.post('/customers', response_model=Customer)
def create_customer(data: CustomerCreate, db: Session = Depends(get_db)):
    customer = CustomerModel(**data.dict())
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

@router.get('/customers', response_model=list[Customer])
def list_customers(db: Session = Depends(get_db)):
    return db.query(CustomerModel).all()
