from pydantic import BaseModel


class ResponseSchemaOut(BaseModel):
    answer:str
