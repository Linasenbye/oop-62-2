class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary
    
    def get_role(self):
        return self.__class__.__name__
    
    def get_info(self):
        return f"Имя: {self.name} | Роль: {self.get_role()} | Зарплата: {int(self.get_salary())}" 

class BackendDeveloper(Employee):
    def __init__(self, name, salary, level):
        super().__init__(name, salary)
        self.level = level

    def get_salary(self):
        if self.level == 'junior':
            return self.salary
        elif self.level == 'middle':
            return self.salary + ((20* self.salary) / 100)
        elif self.level == 'senior':
            return self.salary + ((50* self.salary) / 100)
        else:
            return self.salary
        
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_salary(self):
        return self.salary + (self.team_size * 1000)
        
class Intern(Employee):
    def __init__(self, name, salary, months):
        super().__init__(name, salary)
        self.months = months

    def get_salary(self):
        return 10000

def print_salary(employees):
    for employee in employees:
       print(employee.get_info())

employees = [
   BackendDeveloper("Artem", 40000, "middle"),
   Manager("Oleg", 50000, 5),
   Intern("Ivan", 20000, 3),
]

print_salary(employees)