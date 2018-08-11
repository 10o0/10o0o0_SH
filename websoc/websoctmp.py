# -*- coding: utf-8 -*-
import os
import re
Path = r'I:\Desktop\websoc' #要修改文件所处路径
all_file_list = os.listdir(Path) #列出指定目录下的所有文件
print all_file_list
for file_name in all_file_list:
    try:
        file = open(file_name[0],'r')
        print file_name[0]
        text = file.read()
        title = re.findall('<h3 id="vul_name">(.*?)</h3>',text)
        f =open(title[0].decode('utf-8'),'w+')
        f.write(text)
        # print title[0]
    except:
        continue