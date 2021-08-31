# Project :- Arithmetic Calculator
import time


class Calculator:

    def __init__(self, number1, number2):

        self.num1 = number1
        self.num2 = number2

    def addition(self):
        return self.num1+self.num2

    def substraction(self):
        return self.num1-self.num2

    def multiplication(self):
        return self.num1*self.num2

    def division(self):
        return self.num1/self.num2

    def exponention(self):
        return self.num1**self.num2


if __name__ == "__main__":

    print("Arithmetic Calculator")
    print("""You Have Options for Choosing Numbers
             1. Addition
             2. Substraction
             3. Multiplication
             4. Division
             5. Exponention""")
    time.sleep(2)
    number1 = int(input("Enter 1st Number: "))
    number2 = int(input("Enter 2nd Number: "))
    option = int(input("Enter number of operation: "))
    calc_obj = Calculator(number1, number2)

    if option not in [1, 2, 3, 4, 5]:
        print("Entered Wrong Information ... Exit")
        exit()
    else:
        dict_of_operations = {"1": calc_obj.addition(),
                              "2": calc_obj.substraction(),
                              "3": calc_obj.multiplication(),
                              "4": calc_obj.division(),
                              "5": calc_obj.exponention(),
                              }
        print(dict_of_operations[str(option)])
