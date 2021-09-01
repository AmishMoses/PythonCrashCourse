#!/usr/bin/env/ python3
'''This will be me manipulating strings inside of python'''
def tab():
	print("\tThis text will be tabbed over")
tab()

def newline():
	print("\nThis\nIs\nA\nNewline")
newline()

'''The next option 'strip' is used to manipulate the whitespace in a string'''
def strip():
	message ="       whitespace     "
	print(message.lstrip())
	print(message.rstrip())
	print(message.split())
strip()