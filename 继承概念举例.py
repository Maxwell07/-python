class parent():
    def print_last_name(self):
        print('Lin')
class child(parent):
    def print_first_name(self):
        print('Qi')
    def print_last_name(self):   #和父类中有相同的函数则会覆盖原函数，执行子类中的函数
        print('Zhang')

Linqi = child()
Linqi.print_first_name()
Linqi.print_last_name()