# employee.py

# Define an interface class
class Displayable:
    def display_information(self):
        pass  # This method will be implemented by classes using this interface


# Create a package by organizing classes into a module
class Employee(Displayable):
    def __init__(self, nip, name, year_of_entry, basic_salary):
        self._nip = nip  # protected
        self._name = name  # protected
        self._year_of_entry = year_of_entry  # protected
        self._basic_salary = basic_salary  # protected

class Satpam(Employee):
    def __init__(self, nip, name, year_of_entry, basic_salary, overtime_hours):
        super().__init__(nip, name, year_of_entry, basic_salary)
        self._overtime_hours = overtime_hours  # protected

    def calculate_final_salary(self):
        overtime_bonus = self._overtime_hours * 20000
        return self._basic_salary + overtime_bonus

class Sales(Employee):
    def __init__(self, nip, name, year_of_entry, basic_salary, customers_count):
        super().__init__(nip, name, year_of_entry, basic_salary)
        self._customers_count = customers_count  # protected

    def calculate_final_salary(self):
        commission = self._customers_count * 50000
        return self._basic_salary + commission

class Administrasi(Employee):
    def __init__(self, nip, name, year_of_entry, basic_salary, years_of_service):
        super().__init__(nip, name, year_of_entry, basic_salary)
        self._years_of_service = years_of_service  # protected

    def calculate_final_salary(self):
        if self._years_of_service >= 5:
            allowance = 0.03 * self._basic_salary
        elif self._years_of_service >= 3:
            allowance = 0.01 * self._basic_salary
        else:
            allowance = 0
        return self._basic_salary + allowance

class Manajer(Employee):
    def __init__(self, nip, name, year_of_entry, basic_salary, sales_increase_percentage):
        super().__init__(nip, name, year_of_entry, basic_salary)
        self._sales_increase_percentage = sales_increase_percentage  # protected

    def calculate_final_salary(self):
        if self._sales_increase_percentage > 10:
            bonus = 0.1 * self._basic_salary
        elif 6 <= self._sales_increase_percentage <= 10:
            bonus = 0.05 * self._basic_salary
        elif 1 <= self._sales_increase_percentage <= 5:
            bonus = 0.02 * self._basic_salary
        else:
            bonus = 0
        return self._basic_salary + bonus
