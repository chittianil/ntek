from sqlalchemy.orm import Session
from ..models.dataset import Dataset
from ..models.column import ColumnModel


def search_datasets(db: Session, keyword):

    table_match = db.query(Dataset).filter(
        Dataset.table_name.ilike(f"%{keyword}%")
    ).all()

    column_match = db.query(Dataset).join(ColumnModel).filter(
        ColumnModel.name.ilike(f"%{keyword}%")
    ).all()

    schema_match = db.query(Dataset).filter(
        Dataset.schema_name.ilike(f"%{keyword}%")
    ).all()

    db_match = db.query(Dataset).filter(
        Dataset.database_name.ilike(f"%{keyword}%")
    ).all()

    return table_match + column_match + schema_match + db_match