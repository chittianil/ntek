from sqlalchemy.orm import Session
from project.models.dataset import Dataset


def get_dataset(db: Session, dataset_id: int):
    return db.query(Dataset).filter(Dataset.id == dataset_id).first()


def list_datasets(db: Session):
    return db.query(Dataset).all()


def create_dataset(db: Session, dataset):
    db.add(dataset)
    db.commit()
    db.refresh(dataset)
    return dataset