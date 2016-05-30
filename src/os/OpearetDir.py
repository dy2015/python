'''
Created on 2016年5月28日

@author: dy
'''
#coding:utf-8
import os
path='F:\\1'
allFile =[]
allFile2 =[]
def dirList(path):
    fileList=os.listdir(path)
    for fileName in fileList:
        filePath=os.path.join(path,fileName)
        if os.path.isdir(filePath):
            dirList(filePath)
        allFile.append(filePath)
    return allFile
def dirList2(path):
    for tempPath,d,fileList in os.walk(path):
        for fileName in fileList:
            filePath=os.path.join(tempPath,fileName)
            allFile2.append(filePath)
    return allFile2

name=dirList(path)
name2=dirList2(path)
# paths='F:\\1\\2\\3'
# os.mkdir(path)
# os.makedirs(paths)
# os.rmdir(path)
print(name)
print(name2)