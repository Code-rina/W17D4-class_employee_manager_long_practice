from employee import Employee

class Manager(Employee):
    def __init__(self, name, title, salary, boss, employees):
        super().__init__(name, title, salary, boss)
        self.employees = [];

    def add_employee(self, employee):
        