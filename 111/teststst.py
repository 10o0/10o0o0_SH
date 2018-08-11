import os
import fnmatch
import time

def findfiles(path, fnmatchex='*.*'):
    for root, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files,fnmatchex):
            fullname = os.path.join(root, filename)
            filestat = os.stat(fullname)
            yield fullname, filestat.st_size, filestat.st_ctime

def strtimestamp(timestamp):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

for filename, filesize, createtime in findfiles(r"d:\\", "*txt"):
    print filename, filesize, strtimestamp(createtime)