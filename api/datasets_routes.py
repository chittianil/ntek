from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from project.core.database import get_db
from project.schemas.dataset_schema import DatasetCreate
from project.services.dataset_service import create_dataset
from project.repository.dataset_repo import list_datasets

router = APIRouter(prefix="/datasets")


@router.post("/")
def create(data: DatasetCreate, db: Session = Depends(get_db)):
    dataset= create_dataset(db, data)
    return {
            "message": "inserted successfully",
            "dataset_id": dataset.id
        }


@router.get("/")
def list_all(db: Session = Depends(get_db)):
    return list_datasets(db)