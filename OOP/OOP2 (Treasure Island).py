import random

#Part b
class IslandClass:
    def __init__(self):
        Sand = '.'
        self.__Grid= [[Sand for col in range(30)],[Sand for row in range(10)]]

#Part d
    def HideTreasure(self):
        treasure= 'T'
        row= random.randint(0,9)
        col= random.randint(0,29)
        while self.__Grid[row][col] == treasure:
            row= random.randint(0,9)
            col= random.randint(0,29)
        self.__Grid[row][col] = treasure

#Part e(i)
    def DigHole(self,row,col):
        foundtreasure= 'X'
        hole= 'O'
        if self.__Grid[row][col] == treasure:
            self.__Grid[row][col] = foundtreasure
        else:
            self.__Grid[row][col] = hole

#Part c(i)
    def GetSquare(self, row, col):
        return self.__Grid[row][col]

    Island = IslandClass()
#Part c(ii)
    def DisplayGrid():
        for row in range(10):
            for col in range(30):
                print(Island.GetSquare(row,col), end='')
        print("")

#Part e(ii)
    def StartDig():
        flag = False
        while flag== False:
            xloc=int(input("Enter X location "))
            yloc=int(input("Enter Y location"))
            if xloc > 29 and xloc < 0:
                flag = False
            elif yloc > 9 and yloc < 0:
                flag = False
            else:
                flag = true
        Island.DigHole(yloc,xloc)

#Part a
DisplayGrid()
for i in range(3):
    Island.HideTreasure()
StartDig()
DisplayGrid()


