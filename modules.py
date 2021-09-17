import os
import shutil
import pyperclip as pc

def moveToFolder(path,params):
    path=path[0]
    name = extractName(path)
    name = removeExtension(name)
    os.mkdir(name)  
    newpath = path[:path.rfind("\\")]+"\\"+name
    shutil.move(path,newpath)

def copyPath(path,params): pc.copy(path[0])

def copyName(path,params): pc.copy(extractName(path[0]))

def extractName(path): return path[path.rfind("\\")+1:]

def removeExtension(name): return name[:name.rfind(".")]