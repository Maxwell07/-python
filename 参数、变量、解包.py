from sys import argv
Path = 'F:\\01-Python学习\\01-python学习举例\\ex15_sample.txt'
text = open(Path)
filename = Path.split('\\')[-1]
print("Here's your file %r:" % filename)
print(text.read())