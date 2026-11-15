class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Employee Salary:", self.__salary)


emp = Employee("Sujeet", 30000)

emp.display()
