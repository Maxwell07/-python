class Enemy:
    life = 3
    def __init__(self,x):
        self.life = x
    def get_life(self):
        print(self.life)

Lin = Enemy(5)
Qi = Enemy(20)

print(Lin.get_life())
print(Qi.get_life())
