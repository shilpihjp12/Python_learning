from employee import Employee
# this inherit employee class
from salary_employee import SalaryEmployee
# this inherit employee class
from hourly_employee import HourlyEmployee
# this inherit salary employee class
from comission_employee import ComissionEmployee

class Company:
  def __init__(self):
    self.employees = []

  def add_employee(self, employee):
    self.employees.append(employee)

  def display_all_employees(self):
    for employee in self.employees:
      print(employee.fname, employee.lname)
      print('----------------------------')
  
  def pay_all_employees(self):
    for employee in self.employees:
      print('pay check for ', employee.fname, employee.lname)
      #f function is used to concat the string and variable and also can add float value with 2 decimal points
      print(f'Amount :, ${employee.calculate_payCheck():,.2f}')
      print('----------------------------')

def main():
  my_company = Company()
  emp1 = SalaryEmployee("John", "Doe", 50000)
  my_company.add_employee(emp1)
  emp2 = SalaryEmployee("Jane", "Smith", 25000)
  my_company.add_employee(emp2)
  emp3 = HourlyEmployee("Tom", "Brown", 50, 25)
  my_company.add_employee(emp3)
  emp4 = ComissionEmployee("shilpi", "test", 50000, 100, 0.1)
  my_company.add_employee(emp4)

  my_company.display_all_employees()
  my_company.pay_all_employees()
    

main()