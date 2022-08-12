from __future__ import annotations
from dataclasses import dataclass
from typing import List, Union

@dataclass
class Employee:

    first_name:str
    last_name:str
    work_email:str
    mobile_number:int
    managers:Union[List[Employee], List[str]]

    @classmethod
    def from_dict(cls, args_dict: dict) -> Employee:
        return cls(**args_dict)

if __name__ == "__main__":
    args_dict = {
        "first_name":"Maryam",
        "last_name":"Mirzakhani",
        "work_email":"maryam.mirzakhani@awesome.com",
        "mobile_number":"000",
        "managers": ["Curtis"]
    }
    employee1 = Employee.from_dict(args_dict)
    print(employee1)