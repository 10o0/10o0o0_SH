# -*- coding: utf-8 -*-
import os
import re
Path = r'I:\Desktop\websoc' #要修改文件所处路径
all_file_list = os.listdir(Path) #列出指定目录下的所有文件
for file_name in all_file_list:
    try:
        currentdir =os.path.join(Path, file_name) #连接指定的路径和文件名or文件夹名字
        fname = os.path.splitext(file_name)[0] #分解出当前的文件路径名字
        file = open(fname,'r')
        text = file.read()
        title = re.findall('<h3 id="vul_name">(.*?)</h3>',text)
        f =open(title[0].decode('utf-8'),'w+')
        f.write(text)
        print title[0]
    except IOError:
        None