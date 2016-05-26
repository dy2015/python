#coding:utf-8
import sys
print sys.getfilesystemencoding()#系统编码格式
file_handle =open('D:/eclipseGitWorkSpace/python/src/reptile/PaChong.py','a+')
file_handle.write('\n丁毅')
file_handle.seek(0)
print file_handle.read()
file_handle.close()
print '#'*40

