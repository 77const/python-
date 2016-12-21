#!/usr/bin/env python
# _*_coding:utf-8_*_
'''
date:2016年7月1日08:53:30
'''
import demo

def findchar(string, char):
    if char in string:
        print "good!"
    else:
        print -1

if __name__=="__main__":
    demo.foo()
    string = ['one', 'two', 'three', 'four', 'five']
    char = raw_input("please input a demo:")
    findchar(string, char)
    print __file__
    print __doc__