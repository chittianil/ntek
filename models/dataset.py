from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from project.core.database import Base


class Dataset(Base):

    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True)

    fqn = Column(String(255), unique=True)

    connection_name = Column(String(100))
    database_name = Column(String(100))
    schema_name = Column(String(100))
    table_name = Column(String(100))

    source_type = Column(String(50))

    columns = relationship("ColumnModel", back_populates="dataset")