from employee import Employee

class SalaryEmployee(Employee):
  def __init__(self, fname, lname, salary):
    super().__init__(fname, lname)
    self.salary = salary
  
  def calculate_payCheck(self):
    return self.salary/52
