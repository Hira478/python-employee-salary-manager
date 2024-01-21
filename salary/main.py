# main.py

# Import the Employee module
from employee import Satpam, Sales, Administrasi, Manajer

def get_employee_details():
    nip = input("Enter NIP: ")
    name = input("Enter Name: ")
    year_of_entry = int(input("Enter Year of Entry: "))
    basic_salary = float(input("Enter Basic Salary: "))
    return nip, name, year_of_entry, basic_salary

def get_satpam_details():
    overtime_hours = int(input("Enter Overtime Hours: "))
    return overtime_hours

def get_sales_details():
    customers_count = int(input("Enter Customers Count: "))
    return customers_count

def get_admin_details():
    years_of_service = int(input("Enter Years of Service: "))
    return years_of_service

def get_manager_details():
    sales_increase_percentage = float(input("Enter Sales Increase Percentage: "))
    return sales_increase_percentage

# Example usage with user input:
nip, name, year_of_entry, basic_salary = get_employee_details()
employee_type = input("Enter Employee Type (Satpam/Sales/Administrasi/Manajer): ").capitalize()

if employee_type == "Satpam":
    overtime_hours = get_satpam_details()
    employee = Satpam(nip, name, year_of_entry, basic_salary, overtime_hours)
elif employee_type == "Sales":
    customers_count = get_sales_details()
    employee = Sales(nip, name, year_of_entry, basic_salary, customers_count)
elif employee_type == "Administrasi":
    years_of_service = get_admin_details()
    employee = Administrasi(nip, name, year_of_entry, basic_salary, years_of_service)
elif employee_type == "Manajer":
    sales_increase_percentage = get_manager_details()
    employee = Manajer(nip, name, year_of_entry, basic_salary, sales_increase_percentage)
else:
    print("Invalid Employee Type")

if employee_type in ["Satpam", "Sales", "Administrasi", "Manajer"]:
    # Display information using the interface
    employee.display_information()
    print(f"Final Salary: {employee.calculate_final_salary()}")
