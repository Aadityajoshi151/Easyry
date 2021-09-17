import os
import shutil
import pyperclip as pc

def moveToFolder(path,params):
    path=path[0]
    name = path[path.rfind("\\")+1:]
    name = name[:name.rfind(".")]
    os.mkdir(name)  
    newpath = path[:path.rfind("\\")]+"\\"+name
    shutil.move(path,newpath)

def copyPath(path,params):
    pc.copy(path[0])