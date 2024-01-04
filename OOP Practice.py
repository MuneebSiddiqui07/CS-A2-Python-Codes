# Question1

class Box:
    # PRIVATE Size : string
    # PRIVATE Lock : string
    # PRIVATE Strength : integer
    # Declare Contents : Array[0:9] of FieldObject

    def __init__(self, sizeP, lockP):
        self.__Size = sizeP
        self.__Lock = lockP
        self.__Strength = 100
        self.__Contents = []
        for x in range(0,10):
            self.__Contents.append(x)

    def Unlock(self, code):
        if code == self.__Lock:
            return True
        else:
            self.__Strength = self.__Strength -1
        if self.__Strength < 1:
            return True
        else:
            return False

    def LoadGame(self):
        try:
            file = open("Progress.txt", "r")
            GameData = file.read()
            file.close()
        except:
            print("File does not exist")


# Question 2
class foodItem():
    def __init__(self, nameP, codeP, costP):
        self.__name = nameP
        self.__code = codeP
        self.__cost = costP

    def getCode(self):
        return self.__code

    def getCost(self):
        return self.__cost


class vendingMachine:
    # PRIVATE items : Array [0:3]OF foodItem
    # PRIVATE moneyIn: real
    def __init__(self, item1, item2, item3, item4):
        self.__moneyIn = 0
        self.__items = []
        self.__items.append(item1)
        self.__items.append(item2)
        self.__items.append(item3)
        self.__items.append(item4)

    def checkValid(self, code):
        for x in range(4):
            if self.__items[x].getCode == code:
                if self.__moneyIn >= self.__items[x].getCost:
                    return x
                else:
                    return -2
        return -1
chocolate = foodItem("dairy",232,1)
sweets= foodItem("dair",2312,12)
sandwich = foodItem("dary",22,177)
apple = foodItem("dy",2,13)

Machine1 = vendingMachine(chocolate,sweets,sandwich,apple)


# Question 3


class QuestionClass:
    # PRIVATE Question : string
    # PRIVATE Answer : string
    # PRIVATE Difficulty : integer

    def __init__(self, QuestionP, AnswerP, DifficultyP):
        self.__Question = QuestionP
        self.__Answer = AnswerP
        self.__Difficulty = DifficultyP


class QuizClass():
    # PRIVATE NumberofQuestions : Integer
    # Declare Questions : Array[0:19] of QuestionClass

    def __init__(self):
        self.__NumberofQuestions = 0
        self.__Questions = []
        for x in range(0,19):
            self.__Questions.append(QuestionClass("","", 0))

    def AddQuestion(self, qus):
        if self.__NumberofQuestions < 20:
            self.__Questions[self.__NumberofQuestions] = qus
            self.__NumberofQuestions = self.__NumberofQuestions + 1
            return True
        else:
            return False


FirstQuiz = QuizClass()
Question1 = QuestionClass("What is 100/5?", "20", 1)
FirstQuiz.AddQuestion(Question1)

#Question 4

class PuzzlePlayer():
    # PRIVATE PlayerID : string
    # PRIVATE  Name : string
    # PRIVATE  Score : integer

    def __init__(self):
        self.__PlayerID = "PL12a3"
        self.__Name = ""
        self.__Score = 0

    def GetPlayerID(self):
        return self.__PlayerID

    def SetPlayer(self, ID):
        if len(ID) == 6 and (ID[0:2] == "PL"):
            self.__PlayerID = ID
            return True
        else:
            return False


# Question 8


class Employee():
    # PRIVATE EmployeeID : String
    # PRIVATE Name : string
    # PRIVATE Address : string
    # PRIVATE DateOfBirth : Date

    def __init__(self, employeeIDP, nameP, addressP, dobP):
        self.__EmployeeID = employeeIDP
        self.__Address = addressP
        self.__Name = nameP
        self.__DateofBirth = dobP

    def GetEmployeeID(self):
        return self.__EmployeeID

    def SetEmployeeID(self,ID):
        self.__EmployeeID= ID


class SalaryEmployee(Employee):
    # PRIVATE MonthlyPayment : Currency
    # PRIVATE HoursThisMonth : real
    # PRIVATE PublicHoliday : boolean
    # PRIVATE Pension : Boolean

    def __init__(self, MonthlyPaymentP, HoursMonthlyP, PHolidayP, PensionP):
        self.__MonthlyPayment = MonthlyPaymentP
        self.__HoursThisMonth = HoursMonthlyP
        self.__PublicHoliday = PHolidayP
        self.__Pension = PensionP

    def SetPension(self,pension):
        if pension == True:
            self.__Pension= pension

        else:
            return False

    def GetMonthlyPayment(self):
        return self.__MonthlyPayment

    def GetHoursThisMonth(self):
        return self.__HoursThisMonth

    def GetPublicHoliday(self):
        return self.__PuclicHoliday

    def GetPension(self):
        return self.__Pension



def CalculateMonthlySalary(SalaryEmployee):
    if SalaryEmployee.GetPublicHoliday  == True:
        holidaybonus = (SalaryEmployee.GetMonthlyPayment * 3) /100

    if SalaryEmployee.GetHoursThisMonth() > 160:
        extrabonus = (SalaryEmployee.GetMonthlyPayment * 5)/100

    if SalaryEmployee.GetPension() == True:
        pensionpayment = (SalaryEmployee.GetMonthlyPayment * 4)/100

    print(pensionpayment)
    print(holidaybonus+extrabonus)
    MonthlySalary = (SalaryEmployee.GetMonthlyPayment() + holidaybonus + extrabonus) - pensionpayment

    return MonthlySalary

# Question 8


class Character():
    def SetSkill(self, val):
        if val >= 10 and val <= 25:
            self.__skill = self.skill + val
            if self.__skill < 200:
                return 1
            elif self.skill == 200:
               return 0
        else:
            return -1

# Declare CharacterArray : Array[0:5] of Character
CharacterArray = [""]*5
