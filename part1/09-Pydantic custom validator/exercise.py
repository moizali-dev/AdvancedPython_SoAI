from __future__ import annotations
from email import message
from pydantic import BaseModel, validator
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

    @validator("mobile_number")
    @classmethod
    def check_mobile_number(cls, value:int) -> int:
        if len(str(value)) < 6:
            message = f"'{value}' is less than 6 digits"
            raise ValueError(message)

        return value

    @validator("work_email")
    @classmethod
    def check_work_email(cls, value:str, values: Dict[str, Any]) -> str:
        if values["first_name"].lower() not in value:
            msg = f"Work email passed '{value}' doesn't contain first_name: " \
                  f"{values['first_name']}"
            raise ValueError(msg)
        return value

if __name__ == "__main__":
    args_dict = {
        "first_name":"Maryam",
        "last_name":"Mirzakhani",
        "work_email":"mary.mirzakhani@awesome.com",
        "mobile_number":"222333444",
        "managers": ["Curtis"]
    }
    employee1 = Employee(**args_dict)
    print(employee1)