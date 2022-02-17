from employee import Employee

class Manager(Employee):
    def __init__(self, name, title, salary, boss, employees):
        super().__init__(name, title, salary, boss)
        self.employees = [];

    def add_employee(self, employee, employees):
        employees.append(employee)

annie = Manager('Annie', 'Director', 100000, 'Alvy', 'Gina')
print(annie.employees)
alvy = Employee('Alvy', 'Analyst', 75000, 'Mark', 'Annie')
print(alvy.employees)