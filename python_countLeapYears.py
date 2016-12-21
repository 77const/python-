#!/usr/bin/env python
#_*_coding:utf-8_*_

def count_years():
	years = input("please input a years that need to text:")
	if((years%4 == 0) and (years%100 != 0)):
		print "%s is a leap years!"%years
		return years
	elif((years%4 == 0) and (years%100 == 0)):
		print ("%s is a leap years!"%years)
		return years 
	else:
		print"%s is not a leap years!"%years

count_years()
