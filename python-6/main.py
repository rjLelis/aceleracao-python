import abc

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(metaclass=abc.ABCMeta):

    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary

    @abc.abstractmethod
    def calc_bonus(self):
        pass

    def get_hours(self):
        return 8


class Manager(Employee):
    def __init__(self, code, name, salary,
            department=Department('managers', 1)):

        super().__init__(code, name, salary)
        self.__departament = department

    def calc_bonus(self):
        return self.salary * 0.15

    def get_department(self):
        return self.__departament.name

    def set_department(self, departament_name):
        self.__departament.name = departament_name


class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self.__sales = 0

    def calc_bonus(self):
        return self.get_sales() * 0.15

    def get_sales(self):
        return self.__sales

    def put_sales(self, sale):
        self.__sales += sale
