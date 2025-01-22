
from employee import Employee

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
  emp1 = Employee("John", "Doe", 50000)
  my_company.add_employee(emp1)
  emp2 = Employee("Jane", "Smith", 25000)
  my_company.add_employee(emp2)
  emp3 = Employee("Tom", "Brown", 90000)
  my_company.add_employee(emp3)

  my_company.display_all_employees()
  my_company.pay_all_employees()
    

main()