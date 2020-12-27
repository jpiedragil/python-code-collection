class Employee:

    def earning(self):

        if self.income >= 80000:

            return 'High Earning'

        elif (self.income < 8000) & (self.income > 50000):

            return "Medium Earning"

        else:

            return "Low Earning"


employee1 = Employee()
employee1.name = 'Matt'
employee1.income = 50000

level_earning = employee1.earning()
print(level_earning)
