import os
import shutil
import string
import random
import pathlib
import pyperclip as pc
from datetime import datetime


def moveToFolder(path,params):
    path=path[0]
    name = extractName(path)
    name = removeExtension(name)
    os.mkdir(name)  
    newpath = path[:path.rfind("\\")]+"\\"+name
    shutil.move(path,newpath)

def copyPath(path,params): pc.copy(path[0])

def copyName(path,params): pc.copy(extractName(path[0]))

def renameRandom(path,params):
    path = path[0]
    randomstr = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
    extension = pathlib.Path(path).suffix
    os.rename(path,path[:path.rfind("\\")]+"\\"+randomstr+extension)

def renameTimestamp(path,params):
    path=path[0]
    dateTimeObj = datetime.now()
    print(f"{dateTimeObj.day}-{dateTimeObj.month}-{dateTimeObj.year} {dateTimeObj.hour}:{dateTimeObj.minute}:{dateTimeObj.second}")
    input("Press Any Key To Continue...")


def extractName(path): return path[path.rfind("\\")+1:]

def removeExtension(name): return name[:name.rfind(".")]

