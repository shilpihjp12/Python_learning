from salary_employee import SalaryEmployee

class ComissionEmployee(SalaryEmployee):
  def __init__(self, fname, lname, salary, sales_num, com_rate):
    super().__init__(fname, lname, salary)
    self.sales_num = sales_num
    self.com_rate = com_rate

  def calculate_payCheck(self):
    regular_sal = super().calculate_payCheck()
    total_comission = self.sales_num * self.com_rate
    return regular_sal + total_comission