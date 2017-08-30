answer = lambda x:x*7
print(answer(5))

def calcu(answer = lambda x:x*7):
    print(answer(5))

print(answer(7))

# 结果:
# 35
# 49
