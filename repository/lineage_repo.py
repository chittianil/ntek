from sqlalchemy.orm import Session
from project.models.lineage import Lineage


def create_lineage(db: Session, lineage):
    db.add(lineage)
    db.commit()
    db.refresh(lineage)
    return lineage


def get_all_edges(db: Session):
    return db.query(Lineage).all()