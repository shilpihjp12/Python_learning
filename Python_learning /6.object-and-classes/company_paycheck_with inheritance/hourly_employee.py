from employee import Employee

class HourlyEmployee(Employee):
    def __init__(self, fname, lname, hourly_rate, weekly_hours):
        super().__init__(fname, lname)
        self.hourly_rate = hourly_rate
        self.weekly_hours = weekly_hours

    def calculate_payCheck(self):
        return self.hourly_rate * self.weekly_hours