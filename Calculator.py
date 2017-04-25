class Calculator(object):

    def __init__(self):
        self.history = []

    def add(self,num1,num2):
        result = num1+num2
        desc = "added {} to {} got {}".format(num1,num2,result)
        self.history.append(desc)
        return result

    def multiply(self,num1,num2):
        result = num1*num2
        desc = "multiplied {} by {} got {}".format(num1,num2,result)
        self.history.append(desc)
        return result

    def subtract(self,num1,num2):
        result = num1-num2
        desc = "subtracted {} from {} got {}".format(num1,num2,result)
        self.history.append(desc)
        return result

    def divide(self,num1,num2):
        try:
            result = num1/num2
            result = int(result)
        except ZeroDivisionError:
            self.history.append("Remember never divide by Zero you little shit!")
        else:
            desc = "divided {} by {} got {}".format(num1,num2,result)
            self.history.append(desc)
            return result

    def printAll(self):
        print("The list has following operations: ")
        if self.history == []:
            print('List is empty')
        else:
            for h in self.history:
                print(h)


    def clearAll(self):
        c = self.history.clear()


class AdvancedCalculator(Calculator):
    self.PI = 3.14

    @staticmethod
    def compute_circle_area(r):
        return AdvancedCalculator.PI * (r ** 2)

    @classmethod
    def compute_circle_area_1(cls, r):
        return cls.PI * (r ** 2)



    def pow(self,num1,num2):
        result = num1**num2
        self.history.append("{} to the power {} is {} ".format(num1,num2, result))
        return result

    def root(self, num1, num2):
        result = num1 ** (1 / num2)
        self.history.append("root {} of {} equals {} ".format(num1, num2, result))
        return result





ob = Calculator()
ob.add(2,4)
ob.add(2,8)
ob.subtract(6,3)
ob.multiply(2,7)

ob.divide(8,0)
ob.printAll()
ob.clearAll()
ob.printAll()
ob.divide(9,9)
ob.subtract(9,9)
ob.printAll()







