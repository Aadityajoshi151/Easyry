import os
import shutil
import string
import random
import pathlib
import ctypes
import pyperclip as pc
from datetime import datetime

#Easyry functionalities:-
#Move To Folder
def moveToFolder(path, params):
    path=path[0]
    name = extractName(path)
    name = removeExtension(name)
    os.mkdir(name)  
    newpath = path[:path.rfind("\\")]+"\\"+name
    shutil.move(path, newpath)

#Copy Path To Clipboard
def copyPath(path, params): pc.copy(path[0])

#Copy Name To Clipboard
def copyName(path, params): pc.copy(extractName(path[0]))

#Rename With Random String
def renameRandom(path, params):
    path = path[0]
    randomstr = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
    rename(path, newname=randomstr)

#Rename With Timestamp
def renameTimestamp(path, params):
    path=path[0] 
    timestamp = getTimeStamp()
    rename(path, newname=timestamp)

#Append Timestamp
def appendTimestamp(path, params):
    path=path[0]
    timestamp = getTimeStamp()
    newname = extractName(path)
    newname = f"{removeExtension(newname)}-{timestamp}"
    rename(path, newname)

#Corrupt File
def corruptFile(path, params):
    path=path[0]
    res = ctypes.windll.user32.MessageBoxW(0, "This will cause permanent damage to the file which might not be reversible. Are you sure you want to corrupt the file?", "Are you sure?", 0x04 | 0x30)
    if res==6:
        #Code to corrupt file will go here
        print("Done")

#Duplicate File
def duplicateFile(path, params):
    path=path[0]
    extension = pathlib.Path(path).suffix
    newname = extractName(path)
    newname = removeExtension(newname)
    newpath = path[:path.rfind("\\")]+"\\"+newname+"_Duplicate"+extension
    shutil.copy(path, newpath)

#Misc required functions:-
def getTimeStamp():
    dateTimeObj = datetime.now()
    return(f"{dateTimeObj.day}{dateTimeObj.strftime('%B')}{dateTimeObj.year}_{dateTimeObj.hour}-{dateTimeObj.minute}-{dateTimeObj.second}")

def rename(path, newname):
    extension = pathlib.Path(path).suffix
    os.rename(path, path[:path.rfind("\\")]+"\\"+newname+extension)

def extractName(path): return path[path.rfind("\\")+1:]

def removeExtension(name): return name[:name.rfind(".")]

