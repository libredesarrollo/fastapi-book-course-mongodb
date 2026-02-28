from enum import Enum
from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr

class StatusType(str,Enum):
    DONE = "done"
    PENDING = "pending"

class Category(BaseModel):
    name: str
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "id" : 1234,
    #             "name": "Cate 1"
    #         }
    #     }

class User(BaseModel):
    name: str = Field(min_length=5)
    surname: str
    email: EmailStr
    website: str #HttpUrl

class Task(BaseModel):
    name: str
    description: Optional[str] = Field("No description",min_length=5)
    status: StatusType
    category: Optional[Category] = None
    # user: User
    tags: List[str] = []

    class Config:
        from_attributes=True
        # schema_extra = {
        #     "example": {
        #         "id" : 123,
        #         "name": "Salvar al mundo",
        #         "description": "Hola Mundo Desc",
        #         "status": StatusType.PENDING,
        #         "tag":["tag 1", "tag 2"],
        #         "category": {
        #             "id":1234,
        #             "name":"Cate 1"
        #         },
        #         "user": {
        #             "id":12,
        #             "name":"Andres",
        #             "email":"admin@admin.com",
        #             "surname":"Cruz",
        #             "website":"http://desarrollolibre.net",
        #         }
        #     }
        # }


        

class TaskRead(Task):
    id: str

class TaskWrite(Task):
    id: Optional[str] = Field(default=None)

class TagsUpdate(BaseModel):
    tags: List[str]