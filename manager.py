from employee import Employee

class Manager(Employee):
    def __init__(self, name, title, salary, boss, employees):
        super().__init__(name, title, salary, boss)
        self.employees = [];

    def add_employee(self, employee):
        self.employees.append(employee)

annie = Manager('Annie', 'Director', 100000, None, None)
alvy = Employee('Alvy', 'Analyst', 75000, 'Annie', None)
print(annie.employees)
# print(alvy.employees)