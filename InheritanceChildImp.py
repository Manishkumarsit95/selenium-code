from OppsPrinciple import Calculator


class InheritanceChildImp(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 10, 15)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()


obj = InheritanceChildImp()
print(obj.getCompleteData())


