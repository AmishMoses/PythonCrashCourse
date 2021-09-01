#!/usr/bin/env/ python3
'''This is just a small bit of work with 'strings' inside of Python'''
def practice():
  name = "alex floyd"
  print(name.title())
  print(name.upper())
  print(name.lower())
practice()

'''F (format) strings'''
def f_string():
  first_name = "Alex"
  last_name = "Floyd"
  full_name = f"{first_name} {last_name}"
  print(full_name)
  print(f"Hello, {full_name.title()}!")
  print(f"Hello, {first_name} {last_name}")
  print("Hello, {} {}".format(first_name,last_name))
f_string()
'''To insert a variable's value into a string, place the letter 'f' before the
opening quoatation marks'''  
