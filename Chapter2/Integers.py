#!/usr/bin/env/ python3
'''This is how we can use Python to manage integers'''
#integers are whole numbers
#floats are decimal numbers
#dividing two integers will always result in a float

'''to make large numbers readable use '_' ex: 1000 as 1_000 the numbers don't have
to be grouped in 3's 1_000 is 10_00'''
def large_number():
	unreadable = 1000000000000
	readable = 1_000_000_000_000
	print(readable, unreadable)
large_number()

'''You can also assign multiple values to multiple variables in one line
this is used often for initalizing a set of numbers'''
def number_set():
	a, b, c = 1, 2, 3
	print(a,b,c)
number_set()

'''Constants are variables whose value will never change and is indicated by
using ALL CAPITAL LETTERS'''
def constants():
	MY_NAME = "Alex Floyd"
	print(MY_NAME)
constants()