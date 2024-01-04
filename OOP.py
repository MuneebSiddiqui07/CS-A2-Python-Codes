"""
class sword:
    #PRIVATE xvalue:integer
    #PRIVATE yvalue:integer
    #PRIVATE type:string

    def __init__(self, x, y, swordtype):
        self.xvalue = x
        self.yvalue = y
        self.type = swordtype

    def displaytype(self):
        return self.type

darksword = sword(25,46, "katana")
print(darksword.displaytype())
"""
"""
class Picture:
    #PRIVATE Description : string
    #PRIVATE Width : integer
    #PRIVATE Height : integer
    #PRIVATE FrameColor : string

    def __init__(self, d, w, h, fc):
        self.Description = d
        self.Width = w
        self.Height = h
        self.FrameColor = fc

    def GetDescription(self):
        return self.Description

    def GetHeight(self):
        return self.GetHeight

    def GetWidth(self):
        return self.Width

    def GetColor(self):
        return self.FrameColor

    def SetDescription(self, val):
        self.Description = val


new = input("Enter description: ")
monalisa= Picture(new, )
"""

"""
class TreasureChest:
    #PRIVATE question: string
    #PRIVATE answer: integer
    #PRIVATE points: integer

    def __init__(self, q, ans, p):
        self.question = q
        self.answer = ans
        self.points = p

    def getQuestion(self):
        return self.question

    def checkAnswer(self, chkans):
        if chkans == self.answer
            return True
        else:
            return False

    def getPoints(self, attempts):
        if attempts == 1:
            return int(self.points)
        elif attempts ==2:
            return int(self.points // 2)
        elif attempts == 3 or attempts == 4:
            return int(self.points // 4)
        else:
            return 0
"""

"""
class Balloon:
    #PRIVATE Health : integer
    #PRIVATE Colour : string
    #PRIVATE DefenceItem: string

    def __init__(self, ColourP, DefenceItemP):
        self.Health = 100
        self.Colour = ColourP
        self.DefenceItem = DefenceItemP

    def GetDefenceItem(self):
        return self.DefenceItem

    def ChangeHealth(self, newhealth):
        self.Health= self.Health + int(newhealth)

    def CheckHealth(self):
        if self.Health <= 0:
            return True
        else:
            return False

item = input("Enter defence item: ")
color = input("Enter colour: ")
Balloon1 = Balloon(color, item)

def Defend(obj):
    strength = int(input("Enter strength of the opponent: "))
    obj.ChangeHealth(-strength)
    print(obj.GetDefenceItem())
    temp = obj.CheckHealth()
    if temp == True:
        print("No health remaining")
    else:
        print("Health still remaining")
    return obj

Balloon1=Defend(Balloon1)
"""
"""
class Lesson():
    #PRIVATE LessonType: string
    #PRIVATE Instructor : String

    def __init__(self, LessonTypeP, InstructorP):
        self.LessonType = LessonTypeP
        self.Instructor = InstructorP

    def GetLessonType(self):
        return self.LessonType

    def GetInstructor(self):
        return self.Instructor

    def GetFee(self, char):  # returns the cost of the lesson
        if char == 'B':
            return 45
        elif char == 'I':
            return 50
        elif char == 'A':
            return 55
        else:
            return -1

    def SetLessonType(self, ltype):
        self.LessonType = ltype

    def SetInstructor(self, inst):
        self.Instructor = inst


# Declare LessonArray : Array [0:8] OF Lesson
LessonArray = ["", "", "", "", "", "", "", "", ""]
LessonArray[2] = Lesson("Improve your self", "David")
print(LessonArray[2].GetInstructor())
"""

"""
class Employee():
    # PRIVATE Name : String
    # PRIVATE Age : Integer

    def __init__(self, NameP, AgeP):
        self.__Name = NameP
        self.__Age = AgeP

    def GetName(self):
        return self.__Name


class PartTime(Employee):
    # PRIVATE HourlyRate : Integer

    def __init__(self, NameP, AgeP, HourlyRateP):
        super().__init__(NameP, AgeP)
        self.__HourlyRate = HourlyRateP

    def DailyWage(self, Hoursworked):
        temp = self.__HourlyRate * Hoursworked
        return temp


class FullTime(Employee):
    # PRIVATE MonthlyRate: Integer

    def __init__(self, NameP, AgeP, MonthlyRateP):
        super().__init__(NameP, AgeP)
        self.__MonthlyRate = MonthlyRateP

    def YearlySalary(self):
        temp = 12 * self.__MonthlyRate
        print(temp)


Person1 = PartTime("Muneer", 18, 45)
Person2 = FullTime("Ossama", 30, 45)
print(Person1.GetName())
print(Person2.YearlySalary())
"""

class Member:
    # PRIVATE MemberName : String
    # PRIVATE MemberID : String
    # PRIVATE SubscriptionPaid : Boolean

    def __init__(self):
        self.__MemberName = " "
        self.__MemberID = " "
        self.__SubscriptionPaid = False

    def SetMemberName(self, name):
        self.__MemberName = name

    def SetMemberID(self, ID):
        self.__MemberID = ID

    def SetSubscriptionPaid(self, SubPaid):
        self.__SubscriptionPaid = SubPaid


class JuniorMember(Member):
    # PRIVATE DateOfBirth : String

    def __init__(self):
        super().__init__()
        self.__DateOfBirth = ""

    def SetDateOfBirth(self, dob):
        self.__DateOfBirth = dob

    def SetMemberName(self, name):
        super().SetMemberName(name)

    def SetMemberID(self, ID):
        super().SetMemberName(ID)

    def SetSubscriptionPaid(self, SubPaid):
        super().SetSubscriptionPaid(SubPaid)


NewMember = JuniorMember()
NewMember.SetMemberName("Ahmed")
NewMember.SetMemberID("12347")
NewMember.SetDateOfBirth("12/11/2001")
NewMember.SetSubscriptionPaid(True)
"""
"""
Array2D = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

Array2D[1][3] = 5

for x in range(3):
    print(Array2D[x])

Array2D[2][1] = 3
print()
print(Array2D[2])
"""

"""
Array2D = [["Ahmed", "Ali", "Bano"], ["Qasim", "Faisal", "Khalid"]]

for rows in range(2):
    for col in range(3):
        if Array2D[rows][col] == "Faisal":
            print("Present")


