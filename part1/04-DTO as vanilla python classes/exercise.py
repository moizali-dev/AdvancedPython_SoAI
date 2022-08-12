class Employee:

    def __init__(self, first_name,
                last_name, work_email,
                mobile_number, managers) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.work_email = work_email
        self.mobile_number = mobile_number
        self.managers = managers

    def __str__(self) -> str:
        return f"first name = '{self.first_name}', last name = '{self.last_name}'"

    def __eq__(self, other : object) -> bool:
        if self.first_name == other.first_name and self.last_name == other.last_name:
            return True
        return False

if __name__ == "__main__":
    employee1 = Employee("Maryam","Mirzakhani","maryam.mirzakhani@awesome.com","000",["Curtis"])
    employee2 = Employee("Maryam","Mirzakhani","maryam.mirzakhani@awesome.com","000",["Curtis"])
    print(employee1 == employee2)