from __future__ import annotations
from pydantic import BaseModel
from typing import List, Union

class Employee(BaseModel):

    first_name:str
    last_name:str
    work_email:str
    mobile_number:int
    managers:Union[List[Employee], List[str]]
    complete_name:str = None


    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.complete_name = self.first_name + " " + self.last_name

if __name__ == "__main__":
    args_dict = {
        "first_name":"Maryam",
        "last_name":"Mirzakhani",
        "work_email":"maryam.mirzakhani@awesome.com",
        "mobile_number":"000",
        "managers": ["Curtis"]
    }
    employee1 = Employee(**args_dict)
    print(employee1)