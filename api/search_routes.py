from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from project.core.database import get_db
from project.services.search_service import search_datasets

router = APIRouter(prefix="/search")


@router.get("/")
def search(q: str, db: Session = Depends(get_db)):
    return search_datasets(db, q)