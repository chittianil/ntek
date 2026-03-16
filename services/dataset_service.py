from sqlalchemy.orm import Session
from project.models.dataset import Dataset
from project.models.column import ColumnModel


def create_dataset(db: Session, data):

    dataset = Dataset(
        fqn=data.fqn,
        connection_name=data.connection_name,
        database_name=data.database_name,
        schema_name=data.schema_name,
        table_name=data.table_name,
        source_type=data.source_type
    )

    db.add(dataset)
    db.commit()
    db.refresh(dataset)

    for col in data.columns:
        column = ColumnModel(
            dataset_id=dataset.id,
            name=col.name,
            type=col.type
        )

        db.add(column)

    db.commit()

    return dataset