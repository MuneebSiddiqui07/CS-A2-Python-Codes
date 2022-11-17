class GameElement:
    def __init__(self, posX, posY, w, h, ifn):
        self.__PositionX = posY
        self.__PositionY = posX
        self.__Width = w
        self.__Height = h
        self.__ImageFileName = ifn

    def GetDetails(self):
        details= "PositionX: " + str(self.__PositionX) +  "\n" +  "PositionY: " + \
            str(self.__PositionY) + "\n"  + "Width: " + str(self.__Width) + "\n" + \
            "Height: " + str(self.__Height) + "\n" + "ImageFileName: " + self.__ImageFileName + "\n"
        return details

class Scenery(GameElement):
    def __init__(self, posX, posY, w, h, ifn, CauseDamage, DamagePoints):
        super().__init__( posX, posY, w, h, ifn)
        self.__CauseDamage = CauseDamage
        self.__DamagePoints = DamagePoints

    def GiveDamagePoints(self):
        if self.__CauseDamage == True:
            return self.__DamagePoints
        else:
            return 0

    def GetScenery(self):
        details = super().GetDetails() + "Cause Damage: " + str(self.__CauseDamage) + "\n" + \
            "Damage Points: " + str(self.__DamagePoints)
        return details

GiftBox = Scenery(150,150,50,75, "box.png", True, 50)
print(GiftBox.GetScenery())
