from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas import ExperimentCreate, Experiment
from ..models import Experiment as ExperimentModel
from ..database import get_db

router = APIRouter()

@router.post('/experiments', response_model=Experiment)
def create_experiment(data: ExperimentCreate, db: Session = Depends(get_db)):
    exp = ExperimentModel(**data.dict())
    db.add(exp)
    db.commit()
    db.refresh(exp)
    return exp

@router.get('/experiments', response_model=list[Experiment])
def list_experiments(db: Session = Depends(get_db)):
    return db.query(ExperimentModel).all()
