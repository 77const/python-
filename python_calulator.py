#!/usr/bin/env python
#_*_coding:utf-8_*_
operator = {1:'+',2:'-',3:'*',4:'/'}
def calulator():
	NumberA = input("please input a numberA:")
	NumberB = input("please input anther numberB:")
	print operator
	oper= input("pleadse choose a operator:")
	if(oper==1):
		result = NumberB+NumberA
	elif(oper==2):
		result = NumberB-NumberA
	elif(oper==3):
		result = NumberB*NumberA
	elif(oper==4):
		result = NumberB/NumberA
	print result


calulator()
