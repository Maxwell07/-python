income = [10,20,30]
def double_money(RMB):
    return RMB*2
print(map(double_money,income))
print(list(map(double_money,income)))

double_income = [double_money(RMB) for RMB in income]
print(double_income)

#结果
# [20, 40, 60]
# [20, 40, 60]