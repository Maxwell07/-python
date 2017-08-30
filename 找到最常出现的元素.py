from collections import Counter
text = '字符/科学上网/字符/字符/字符/科学上网/好帮手/好帮手/科学上网'
words = text.split('/')
print(words)

counter =Counter(words)
top_two = counter.most_common(2)
print(top_two)
