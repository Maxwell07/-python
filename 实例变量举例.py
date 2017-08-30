class Girl:
    gender = 'female'
    def __init__(self,name):
        self.name = name

Zhang = Girl('zhang')
Qin = Girl('Qin')
print(Zhang.gender)
print(Qin.gender)
print(Zhang.name)
print(Qin.name)
