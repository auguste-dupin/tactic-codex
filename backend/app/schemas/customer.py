from pydantic import BaseModel, EmailStr

class CustomerBase(BaseModel):
    name: str
    email: EmailStr
    notes: str | None = None

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int

    class Config:
        orm_mode = True
