from pydantic import BaseModel
from typing import List


class ColumnCreate(BaseModel):
    name: str
    type: str


class DatasetCreate(BaseModel):
    fqn: str
    connection_name: str
    database_name: str
    schema_name: str
    table_name: str
    source_type: str
    columns: List[ColumnCreate]