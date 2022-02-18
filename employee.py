class Employee:
    def __init__(self, name, title, salary, boss):
        self.name = name
        self.title = title
        self.salary = salary
        self.boss = boss

        if boss:
            self.boss.add_employee(self)

    def bonus(self, multiplier):
        return self.salary * multiplier

         