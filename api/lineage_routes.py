from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from project.core.database import get_db
from project.schemas.lineage_schema import LineageCreate
from project.services.lineage_service import add_lineage

router = APIRouter(prefix="/lineage")


@router.post("/")
def create_lineage(data: LineageCreate, db: Session = Depends(get_db)):
    lineage = add_lineage(
        db,
        data.upstream_dataset_id,
        data.downstream_dataset_id
    )

    return {
        "message": "Lineage inserted successfully",
        "data": {
            "upstream_dataset_id": data.upstream_dataset_id,
            "downstream_dataset_id": data.downstream_dataset_id
        }
    }