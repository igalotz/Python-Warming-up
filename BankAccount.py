import sys

class BankAccount(object):
    def __init__(self, number):
        self.__cash = 0.0

        if isinstance(number, int)==True:
            self.__number = number
        else:
            sys.exit("Numer konta ma być liczbą całkowitą!")

    def get_number(self):
        return self.__number

    def get_cash(self):
        return self.__cash


    def depositCash(self, amount):
        try:
            if amount < 0:
                print("Number has to be positive to deposit cash")
            else:
                self.__cash = self.__cash + amount
        except TypeError:
            print("Amount you deposit must be a number!")


    def withdrawCash(self,amount):
        try:
            if amount > self.__cash:
                print("You don't havee this kind of money, I will only give you {} ".format(self.__cash))
                self.__cash = 0.0
                print("You have left {0}".format( self.__cash))

            elif amount <0:
                print("Number has to be positive to withdraw cash")

            else:
                self.__cash = self.__cash - amount
                print("You took {}, you have left {}".format(amount, self.__cash))


        except TypeError:
            print("Amount must be a number")

    def printInfo(self):
        print("Your account number is {}, you have {} $".format(self.__number, self.__cash))


k = BankAccount(7)
print(k.get_number())
print(k.get_cash())
k.depositCash(79)
print(k.get_cash())
k.withdrawCash(5)
k.printInfo()
