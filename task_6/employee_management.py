class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class RegularEmployee(Employee):
    def calculate_salary(self):
        return self.salary + 2000   # bonus


class ContractEmployee(Employee):
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate


class Manager(Employee):
    def calculate_salary(self):
        return self.salary + 5000   # allowance


emp = [
    RegularEmployee("Rahul", 30000),
    ContractEmployee("Amit", 120, 200),
    Manager("Neha", 50000)
]

for e in emp:
    print(e.name, "Salary:", e.calculate_salary())