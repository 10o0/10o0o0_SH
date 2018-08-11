# -*- coding:utf-8 -*-
import re
import os
# file = open("text1", 'r')
# text = file.read()
#
# title = re.findall('<h3 id="vul_name">(.*?)</h3>',text)
#
# f =open(title[0].decode('utf-8'),'w')
# f.write(text)
# print title[0]
# coding:utf-8
# by LandGrey
# Function: Modify the file name or file postfix

import os

Path = r'I:\Python\websoc' #要修改文件所处路径
all_file_list = os.listdir(Path) #列出指定目录下的所有文件
# Oldpart = "test" #要替换的文件名中的部分
# Newpart = "Land" #新的文件名部分
#
# Oldpostfix =r".txt" #要修改的文件扩展名类型
# Newpostfix = r".Grey" #新的文件扩展名类型

#批量修改文件名字
# def Modifyprefix(oldcontent,newcontent):
   for file_name in all_file_list:
       currentdir =os.path.join(Path, file_name) #连接指定的路径和文件名or文件夹名字
       if os.path.isdir(currentdir): #如果当前路径是文件夹，则跳过
          continue
        fname = os.path.splitext(file_name)[0] #分解出当前的文件路径名字
        file = open(fname,'r')
        print file

   #      ftype = os.path.splitext(file_name)[1] #分解出当前的文件扩展名
   #      replname =fname.replace(oldcontent,newcontent)
   #      newname = os.path.join(Path,replname+ftype) #文件路径与新的文件名字+原来的扩展名
   #      os.rename(currentdir,newname) #重命名
   # print "Modify file name........"

