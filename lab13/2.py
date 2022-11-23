class WORKER():

    def __init__(self, Names, YearBorn, Work):
        self.Names = Names
        self.YearBorn = YearBorn
        self.Work = Work

    def CalcAg(self):
        return 2022-self.YearBorn

    def ShowYear(self):
        print(self.YearBorn)

    def SetWork(self, ag):
        self.Work=ag


A=WORKER('Anton', 1984, 15)

D=WORKER('Dmytro', 1999, 5)

N=WORKER('Nikita', 1990, 10)

W_all=A.Work + D.Work + N.Work
Y_all=A.CalcAg()+D.CalcAg()+N.CalcAg()
print(W_all)
print(Y_all)



