#!/usr/bin/env/ python3
'''This chapter has to do with working with lists. List are indicated by [] and 
seperated by commas'''
def list():
	languages = ['Python3', 'C++', 'JavaScript', 'CSS']
	print (languages)
	#this prints the entire list including the brackets and apostrophes
	print (languages[0])
	#using indexing will only display the specific element you select from 0
	print (f'{languages[0]} is the best!')
	#including the f option from chapter two to write more specific scripts
	print (languages[-1])
	#-1 is used to represent the end of a list without having to know the exact position
list() 

'''To modifying elements in a list use the list name and the index position you want to change'''
def modifiedlist():
	languages = ['Python3', 'C++', 'JavaScript', 'CSS']
	languages[1] = 'Ruby'
	#this will change C++ to Ruby
	print (languages[1])
	languages.append('Kotlin')
	print (languages[-1])
    #to add elements to the end of a list use the .append('newitem')
modifiedlist()
'''appending makes it easy to create a dynamic list that allows you to start with an empty list 
and allow the user to add input in as needed'''
def dynamic_list():
	dylist = []
	dylist.append('item0')
	dylist.append('item1')
	dylist.append('item2')
	dylist.append('item3')
	print(dylist)
	#adding a item to a list is done by defining the index position and using .insert(#,'item')
	dylist.insert(4,'item4')
	print(dylist)
	#removing elements from a list can be done a couple ways first we will use del list [position]
	del dylist [4]
	print (dylist)
	#next we will use pop() by default this will remove the top item of the list
	#pop() is useful when you would like to use the item laster del will remove the item completly
	dylist.pop()
	print(dylist)
	print (f'The last item in the list now is {dylist.pop()}')
	#you can also specify the item you would like to delete 
	dylist.pop(1)
	print(dylist)
	dylist.append('item1')
	dylist.append('item2')
	#removing an item by value using .remove('item')
	#the .remove() option only removes the first occurence of the item
	dylist.remove('item2')
	print(dylist)
dynamic_list()

'''this hopefully will be a more readable example of this practice'''
def last_list():
	motorcycles = ['Ducati', 'Honda', 'Suzuki', 'BMW']
	too_expensive = 'Ducati' 
	motorcycles.remove(too_expensive)
	print (f"{too_expensive} was removed due to being out of my price range")
last_list()
'''after initalizing the list we created a variable called too_expensive and used it to 
store 'Ducati' we then use this variable to tell python what to delete while still
allowing us to access the variable later by using too_expensive'''