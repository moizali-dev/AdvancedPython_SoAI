from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import List, Union

@dataclass
class Employee:

    first_name:str
    last_name:str
    work_email:str
    mobile_number:int
    managers:Union[List[Employee], List[str]]
    complete_name:str = field(init=False)

    def __post_init__(self) -> None:
        self.complete_name = self.first_name + " " + self.last_name

    @classmethod
    def from_dict(cls, args_dict: dict) -> Employee:
        return cls(**args_dict)

    def to_dict(self) -> dict:
        return asdict(self)

if __name__ == "__main__":
    args_dict = {
        "first_name":"Maryam",
        "last_name":"Mirzakhani",
        "work_email":"maryam.mirzakhani@awesome.com",
        "mobile_number":"000",
        "managers": ["Curtis"]
    }
    employee1 = Employee.from_dict(args_dict)
    print(employee1.to_dict())