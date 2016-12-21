#!/usr/bin/env python
# _*_coding:utf-8_*_
'''
date:2016年6月29日15:48:17
利用辗转相除法进行计算
'''

numberA = int(raw_input("please input a number:"))
numberB = int(raw_input("please input another number:"))

def count_number(Anumber, Bnumber):
    while Bnumber != 0:
        result = Anumber % Bnumber
        Anumber = Bnumber
        Bnumber = result
        # print Anumber,result
        return result

if numberA == numberB != 0:
    print "最大公约数和最小公倍数为%d"%numberA
if numberA < numberB:
    numberA, numberB = numberB, numberA

value = count_number(numberA, numberB)
numberResult = numberA * numberB / value

print "最大公约数为%d"%value
print "最小公倍数为%d"%numberResult

