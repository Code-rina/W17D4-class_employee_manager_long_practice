from ast import If
from termios import TIOCPKT_DOSTOP
from employee import Employee

class Manager(Employee):
    def __init__(self, name, title, salary, boss):
        super().__init__(name, title, salary, boss)
        self.employees = [];

    def add_employee(self, employee):
        self.employees.append(employee)
        return employee

# annie = Manager('Annie', 'Director', 100000, None)
# alvy = Employee('Alvy', 'Analyst', 75000, annie)

# print(annie.employees)

    def bonus_calculator(self):
        sum = 0

        for employee in self.employees:
            if isinstance(employee, Manager):
                sum += employee.salary + employee.bonus_calculator()
            else:
                sum += employee.salary
        return sum

    def bonus(self, multiplier):
        return (self.salary + self.bonus_calculator()) * multiplier