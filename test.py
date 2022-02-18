from employee import Employee
from manager import Manager

hobbes = Manager('Hobbes', 'Founder', 1000000, None)
calvin = Manager('Calvin', 'Director', 130000, hobbes)
susie = Manager('Susie', 'TA Manager', 100000, calvin)
lily = Employee('Lily', 'TA', 90000, susie)
clifford = Employee('Clifford', 'TA', 90000, susie)

print(hobbes.bonus(0.05))       #70500
print(calvin.bonus(0.05))       #20500
print(susie.bonus(0.05))        #14000
print(lily.bonus(0.05))         #4500
print(clifford.bonus(0.05))     #4500

print(isinstance(hobbes, Manager))      # true
print(isinstance(lily, Manager))        # false

