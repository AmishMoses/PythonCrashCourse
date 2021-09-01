#!/usr/bin/env/ python3
'''This is the remainder of chapter 3. We will now be organizing a list after creation
sort() will let you permanently change the order of your list'''
def sorting_list():
	cars = ['bmw', 'audi', 'toyota', 'subaru']
	cars.sort()
	#Again this will sort the list PERMANENTLY alphabeticly
	print (cars)
	#This can also be done in reverse order by passing the argument (reverse=True)
	cars.sort(reverse=True)
	print(cars)
	print(sorted(cars))
'''To sort a list temporarily but maintain the original order of a list you can use the 
sorted() function. This will again default to alphabetically'''
sorting_list()

'''You can also print a list in reverse order without affecting the positioning of the order
alphabetically by using .reverse() instead of .sort(reverse=True)'''
def new_list():
	food = ['Apples', 'Bananas', 'Melon', 'Lemon', 'Tomato']
	food.reverse()
	print(food)
	#notice that this onlyy turns the list order
	#to find the length of a list we can use len(list) python counts this list starting at 1 not 0
	print(len(food))
new_list()
