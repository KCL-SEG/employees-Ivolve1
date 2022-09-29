"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, hours = 0, hourlyRate = 0, salary = 0, commissions = 0, commissionPay = 0, bonus = 0):
        self.name = name
        self.hours = hours
        self.hourlyRate = hourlyRate
        self.salary = salary
        self.commissions = commissions
        self.commissionPay = commissionPay
        self.bonus = bonus
        self.totalPay = 0

    def get_pay(self):
        if self.salary:
            self.totalPay += self.salary
        if self.hours:
            self.totalPay += (self.hours * self.hourlyRate)
        if self.commissions:
            self.totalPay += (self.commissions * self.commissionPay)
        if self.bonus:
            self.totalPay += self.bonus
        return self.totalPay

    def __str__(self):
        string = self.name
        if self.salary:
            string += (f" works on a monthly salary of {self.salary}")
        else:
            string += (f" works on a contract of {self.hours} hours at {self.hourlyRate}/hour")

        if self.commissions:
            string += (f" and receives a commission for {self.commissions} contract(s) at {self.commissionPay}/contract.")
        elif self.bonus:
            string += (f" and receives a bonus commission of {self.bonus}.")
        else:
            string += "."

        string += (f"  Their total pay is {self.totalPay}.")
        return string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary = 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hours = 100, hourlyRate = 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salary = 3000, commissions = 4, commissionPay = 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hours = 150, hourlyRate = 25, commissions = 3, commissionPay = 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary = 2000, bonus = 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hours = 120, hourlyRate = 30, bonus = 600)
