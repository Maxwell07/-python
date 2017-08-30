class Mario():
    def move(self):
        print("我在移动")
class Big_Mario():
    def eat_mushroom(self):
        print("我变大了")
class Shoot_Mario(Mario,Big_Mario):
    def shoot(self):
        print("我会射击")
Lin = Shoot_Mario()
print(Lin.move())
print(Lin.eat_mushroom())
print(Lin.shoot())
