import datetime

class Employee(object):
    num_of_emp = 0
    raise_amount = 1.04 #class variable
    def __init__(self, first_name, last_name, pay):

        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        Employee.num_of_emp +=1

    @property
    def email(self):
        return self.first_name + '.' + self.last_name +"@mail.com"

    @property
    def fullname(self, procent):
        return "{} {}".format(self.first_name,self.last_name)

#setter won't work without that @proprty up there
    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod    #classmethod as alternative constractor
    def from_string(cls,emp_str):
        first_name, last_name, pay = emp_str.split(' ')
        return cls(first_name, last_name, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name,pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first_name, last_name, pay, employees=None):
        super().__init__(first_name, last_name,pay)
        if self.employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)


    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.append(emp)


emp1 = Employee("Kasia", "Bigos", 90)
emp2 = Employee("Anna", "Nowak", 50)
dev1 = Developer("Iga", "Lotz", 100, 'Python')
dev2 = Developer("Tomasz", "Bizon",100, 'JavaScript')

Employee.raise_amount = 1.05
emp1.raise_amount = 1.20    #powstał raise_amount atrybut dla emp1
#print(emp1.__dict__)
print(Employee.num_of_emp)

print(dev1.email)
dev1.apply_raise()
print(dev1.pay)
emp1.fullname = "Corey Schafer"
print(emp1.email)
Employee.set_raise_amount(20)
print(Employee.raise_amount)
new_emp1 = Employee.from_string("Ela Lotz 200")
print(new_emp1.email)
print(new_emp1.pay)
d = datetime.date(2017, 4, 29)

print(Employee.is_workday(d))
