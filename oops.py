class Employee:

    # Constructor
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary;

    # Normal function

    def getSalary(self):
        self.salary;

ansh = Employee('Ansh','90,000');
print(ansh.salary)
print(ansh.name)

another = Employee('Another','1234')
print(another.name)
print(another.salary)