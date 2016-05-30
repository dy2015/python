#coding:utf-8
'''
Created on 2016年5月29日

@author: dy
'''
class Class1:
    first=123
    second=456
    def __init__(self, params):
        print("我是第一个类:"+params)
if __name__ == "__main__":
    temp=Class1('123')
    print(temp.first)
    print(temp.second)
else:
    print("不存在Class1这个类")     
     
     
            