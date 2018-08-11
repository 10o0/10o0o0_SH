# -*- coding: utf-8 -*-
import os

Path = r'I:\Python\websoc' #要修改文件所处路径
all_file_list = os.listdir(Path) #列出指定目录下的所有文件
for file_name in all_file_list:
    currentdir =os.path.join(Path, file_name) #连接指定的路径和文件名or文件夹名字
    fname = os.path.splitext(file_name)[0] #分解出当前的文件路径名字
    try:
        file = open(fname,'r')
        text = file.read()
        print text
    except:
        print "error"