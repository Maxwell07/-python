Path = 'F:\\01-Python学习\\01-python学习举例\\'
filename_copy = 'copy.txt'
filename_paste = 'paste.txt'
print('我要把文件%s中的内容复制到%s中去' %(filename_copy,filename_paste))
filepath_copy = Path + filename_copy
filepath_paste = Path + filename_paste
# print(filepath_copy,filepath_paste)

file_copy = open(filepath_copy,'w')
line1 = input('复制代码行1:')
line2 = input('复制代码行2:')
line3 = input('复制代码行3:')
file_copy.write(line1)
file_copy.write('\n')
file_copy.write(line2)
file_copy.write('\n')
file_copy.write(line3)
file_copy.close()

in_file = open(filepath_copy)
copy_date = in_file.read()
print('复制数据的长度为%d'% len(copy_date))

out_file = open(filepath_paste,'w')
out_file.write(copy_date)
print('大功告成了')

in_file.close()
out_file.close()



