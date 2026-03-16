from pydantic import BaseModel


class LineageCreate(BaseModel):
    upstream_dataset_id: int
    downstream_dataset_id: int