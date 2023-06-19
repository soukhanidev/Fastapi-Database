from pydantic import BaseModel


class customer(BaseModel):
    id:int
    name:str
    number:int
    address:str