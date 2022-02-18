from employee import Employee

class Manager(Employee):
    def __init__(self, name, title, salary, boss):
        super().__init__(name, title, salary, boss)
        self.employees = [];

    def add_employee(self, employee):
        self.employees.append(employee)
        return employee

annie = Manager('Annie', 'Director', 100000, None)
alvy = Employee('Alvy', 'Analyst', 75000, annie)
# print(annie.add_employee(alvy))
print(annie.employees)
# annie.add_employee()
# print(alvy.employees)