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
    rename(path,randomstr)

def renameTimestamp(path,params):
    path=path[0]
    dateTimeObj = datetime.now()
    timestamp = str(dateTimeObj.day)+"-"+str(dateTimeObj.month)+"-"+str(dateTimeObj.year)+" "+str(dateTimeObj.hour)+"-"+str(dateTimeObj.minute)+"-"+str(dateTimeObj.second)
    rename(path,timestamp)

def extractName(path): return path[path.rfind("\\")+1:]

def removeExtension(name): return name[:name.rfind(".")]

def rename(path,newname):
    extension = pathlib.Path(path).suffix
    os.rename(path,path[:path.rfind("\\")]+"\\"+newname+extension)