class Enemy:
    life = 3

    def attack(self):
        print('掉一滴血')
        self.life -= 1
    def checklife(self):
        if self.life <= 0:
            print('我死了')
        else:
            print('我还活着,来打我啊')


enemy1 = Enemy()
print(enemy1.life)
enemy1.attack()
print(enemy1.life)
print(enemy1.checklife())

enemy2 =Enemy()
enemy2.attack()
enemy2.attack()
enemy2.attack()
print(enemy2.checklife())
