class human:
    def __init__(self, n, ad, ag):
        self.__name = n
        self.__address = ad
        self.__age = ag

    #setters
    def setname(self, n):
        self.__name = n

    def setaddress(self, ad):
        self.__address = ad

    def setage(self, ag):
        self.__age = ag

    #getters
    def tellname(self):
        return self.__name

    def telladdress(self):
        return self.__address

    def tellage(self):
        return self.__age

    def tellall(self):
        hAll = "Name:" + self.__name + ", Address:" + self.__address + ", Age: " + str(self.__age)
        return hAll


class teacher(human):
    def __init__(self, n, ad, ag, q, s, e):
        super().__init__(n,ad,ag)
        self.__qual = q
        self.__sub = s
        self.__exp = e

    #setters
    def setqual(self, q):
        self.__qual = q

    def setsub(self,s):
        self.__sub = s

    def setexp(self, e):
        self.__exp = e

    #getters
    def tellqual(self):
        return self.__qual

    def tellsub(self):
        return self.__sub

    def tellexp(self):
        return self.__exp

    def tellall(self):
        all = super().tellall()
        TAll = all + ", Qualification: " + self.__qual + ", Subject: " + self.__sub + ", Experience: " + str(self.__exp)
        return TAll

h1= human("Muneeb", "Karachi", 18)
t1= teacher("Atif Wasi","Karachi",69,"Masters in Phy","Physics",15)

print(h1.tellname())
print(t1.tellall())

