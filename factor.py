from pydantic import BaseModel


class factor(BaseModel):
    id:int
    foodQuantity:int
    UnitPrice:int
    Off:float