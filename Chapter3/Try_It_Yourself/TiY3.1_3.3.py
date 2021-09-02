#!/usr/bin/env3 python3
'''Try these short programs to get some firsthand experience with Python’s lists.
You might want to create a new folder for each chapter’s exercises to keep
them organized.
3-1. Names: Store the names of a few of your friends in a list called names. Print
each person’s name by accessing each element in the list, one at a time.
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the
person’s name.
3-3. Your Own List: Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle."'''
def names():
	#3.1 Names
	friends = ['Mike', 'Sabo', 'Manny', 'Andrew']
	print(friends[0])
	print(friends[1])
	print(friends[2])
	print(friends[3])
	#3.2 Greetings
	print(f"Hello {friends} how are you today?")
	#I think that's what they want but using a loop will make this cleaner
	for friend in friends:
		print(f"Hello {friend} I hope you are doing good!")
names()

#3.3 Your own list
def my_list():
	transportation = ['Cars', 'Truck', 'Motorcycles']
	print (f"I have owned a few {transportation[0]}")
	print (f"I have owned one {transportation[1]}")
	print(f"I have owned two {transportation[2]}")
my_list()