Path = 'F:\\01-Python学习\\01-python学习举例\\ex15_sample.txt'
target = open(Path,'w')
filename = Path.split('\\')[-1]
print('Truncationg the file.Goodbye')
target.truncate()
print('Now I am going to ask you 3 lines')
line1 = input('line 1:')
line2 = input('line 2:')
line3 = input('line 3:')
print('I am going to write these to the file')

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')
print('And finally,we closing it')
target.close()

test = target = open(Path,'r')
print(test.read())
