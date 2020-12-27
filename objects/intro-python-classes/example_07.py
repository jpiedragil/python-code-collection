class Employee:

    def __init__(self, name, income):

        self.name = name
        self.income = income

    def earning(self):

        if self.income >= 80000:

            return 'High Earning'

        elif (self.income < 8000) & (self.income > 50000):

            return "Medium Earning"

        else:

            return "Low Earning"


employee1 = Employee('Matt', 50000)
level_earning = employee1.earning()
print(employee1.name, "=", level_earning)

employee2 = Employee('Penelope', 90000)
level_earning = employee2.earning()
print(employee2.name,  "=", level_earning)
