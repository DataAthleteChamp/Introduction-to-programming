class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=2000):
        self.annual_salary = self.annual_salary + amount


employe = Employee("Jakub", "Piotrowski", 15000)
print(employe.annual_salary)
employe.give_raise()
employe.give_raise(1234)
print(employe.annual_salary)
