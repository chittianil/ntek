from pydantic import BaseModel


class ColumnBase(BaseModel):
    name: str
    type: str


class ColumnCreate(ColumnBase):
    pass


class ColumnResponse(ColumnBase):
    id: int
    dataset_id: int

    class Config:
        orm_mode = True