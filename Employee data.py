#1

class Employee:
    def __init__(self, name="", empNum=0):
        self.name = name
        self.empNum = empNum
    #accessor
    def getName(self):
        return self.name
    def getEmpNum(self):
        return self.empNum
    #mutator
    def setName(self, name):
        self.name = name
    def setEmpNum(self, empNum):
        self.empNum = empNum

class ProductionWorker(Employee):
    def __init__(self, name="", empNum=0, shiftNum=1, hrPay=0.0):
        super().__init__(name, empNum)
        self.shiftNum = shiftNum
        self.hrPay = hrPay

    def getShiftNum(self):
        return self.shiftNum
    def getHrPay(self):
        return self.hrPay

    def setShiftNum(self, shiftNum):
            if shiftNum == 2 or shiftNum == 1:
                self.shiftNum = shiftNum
                return True
            else:
                print("Invalid shift number. Enter 1 for Morning or 2 for Night")
                return False
    def setHrPay(self, hrPay):
        self.hrPay = hrPay

worker = ProductionWorker()
worker.setName(input("What is your name? "))
worker.setEmpNum(int(input("What is your employee number? ")))
worker.setShiftNum(int(input("What is your shift number? ")))
#found =  True
while worker.setShiftNum(int(input("What is your shift number? "))) == False:
    worker.setShiftNum(int(input("What is your shift number? ")))
else:
    worker.setHrPay(float(input("What is your hourly pay rate? ")))


print()
print("Employee Name: "+worker.getName())
print("Employee Number: %d"%worker.getEmpNum())
print("Employee Shift Number: %d"%worker.getShiftNum())
print("Employee Hourly Pay Rate: %.2f"%worker.getHrPay())
