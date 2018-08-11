# coding:utf-8
# 1 编写程序，将包含学生成绩的字典保存为二进制文件，然后再读取内容并显示。
import pickle
d = {'张三':98,'李四':90,'王五':100}
print(d)
f = open('score.dat','wb')
pickle.dump(1,f)
pickle.dump(d,f)
f.close

f = open('score.dat','rb')
pickle.load(f)
d = pickle.load(f)
f.close()
print(d)
# 2. 编写程序，用户输入一个目录和一个文件名，搜索该目录及其子目录中是否存在该文件。
import sys
import os
directory = 'I:\Python'
filename = 'test.py'
paths = os.walk(directory)
for root,dirs,files in paths:
    if filename in files:
        print('Yes')
        break
else:
    print('No')
