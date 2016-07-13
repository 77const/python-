#!/usr/bin/env python
# _*_coding:utf-8_*_
'''
date:2016年6月30日09:53:19
'''

number = int(raw_input("please input a number that you want to convert English (0-1000):"))

TheUnitList = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
                14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "ninetee"}
TheDecadeList = {0: '', 1: "ten", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

def the_unit(number):
    UnitNumber = number % 100 % 10
    return UnitNumber

def the_decade(number):
    DecadeNumber = number % 100 / 10
    return DecadeNumber

def the_hundreds(number):
    HundredNumber = number / 100
    return HundredNumber

def convert():
    EnglishNumberH = the_hundreds(number)
    EnglishNumberD = the_decade(number)
    EnglishNumberU = the_unit(number)
    EnglishNumberDU = number % 100
    Mnumber = number % 100
    Decition = Mnumber % 10
    if number == 0:
        print "Zero"
    elif number == 1000:
        print "One thousand"
    elif 100 <= number < 1000:
        if Mnumber == 0:
            print "%s hundred %s%s"%(TheUnitList[EnglishNumberH], TheDecadeList[EnglishNumberD], TheUnitList[EnglishNumberU])
        elif Mnumber >= 20:
            if Decition == 0:
                print "%s hundred and %s%s"%(TheUnitList[EnglishNumberH], TheDecadeList[EnglishNumberD], TheUnitList[EnglishNumberU])
            else:
                print "%s hundred and %s-%s"%(TheUnitList[EnglishNumberH], TheDecadeList[EnglishNumberD], TheUnitList[EnglishNumberU])
        else:
            print "%s hundred and %s"%(TheUnitList[EnglishNumberH], TheUnitList[EnglishNumberDU])
    elif 10 <= number < 100:
        if Mnumber >= 20:
            if Decition == 0:
                print "%s%s"%(TheDecadeList[EnglishNumberD], TheUnitList[EnglishNumberU])
            else:
                print "%s-%s"%(TheDecadeList[EnglishNumberD], TheUnitList[EnglishNumberU])
        else:
            print "%s"%TheUnitList[EnglishNumberDU]
    elif 0 < number < 10:
        print "%s"%TheUnitList[EnglishNumberU]
    else:
        print "error,please run again!"


if __name__ == "__main__":
    convert()