'''
Created on 2016-5-20

@author: Administrator
'''
import re 
import urllib
#coding:utf-8
def getHtml(url): 
    page = urllib.urlopen(url) 
    htmlCon = page.read() 
    return htmlCon

def getImg(html): 
    reg = r'src="(.*?.jpg)' 
    imgre = re.compile(reg, re.X) 
    imglist = re.findall(imgre, html) 
    x = 0 
    for imgurl in imglist: 
        urllib.urlretrieve(imgurl, '%s.jpg' % x) 
        x += 1

html = getHtml("http://learning.sohu.com/20160519/n450288860.shtml") 
print getImg(html)