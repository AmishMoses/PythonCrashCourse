#!/usr/bin/env3/ python3
'''3-8. Seeing the World: Think of at least five places in the world you’d like to
visit.
•	 Store the locations in a list. Make sure the list is not in alphabetical order.
•	 Print your list in its original order. Don’t worry about printing the list neatly,
just print it as a raw Python list.
•	 Use sorted() to print your list in alphabetical order without modifying the
actual list.
•	 Show that your list is still in its original order by printing it.
•	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
•	 Show that your list is still in its original order by printing it again.
•	 Use reverse() to change the order of your list. Print the list to show that its
order has changed.
•	 Use reverse() to change the order of your list again. Print the list to show
it’s back to its original order.
•	 Use sort() to change your list so it’s stored in alphabetical order. Print the
list to show that its order has been changed.
•	 Use sort() to change your list so it’s stored in reverse alphabetical order.
Print the list to show that its order has changed.
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
through 3-7 (page 42), use len() to print a message indicating the number
of people you are inviting to dinner.
3-10. Every Function: Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once.'''

#3.8 Seeing the world
def see_the_world():
	locations = ['Paris', 'London', 'Argentina', 'Barcelona', 'Moscow']
	print(locations) #prints a raw python list
	print(sorted(locations, reverse=True)) #prints the list in reverse alphabetical order without changing the original
	print(f"Showing the original list remained unchanged : \n{locations}")
	locations.reverse() #this will stage the list in reverse order to be shown with the print() method
	print(locations) 
	locations.reverse() #this put the order back into the original format
	print(locations)
	locations.sort() #this like reverse() stages the list permanently unlike the sorted() method
	print(locations)
	locations.sort(reverse=True) #like sorted(reverse=True) but the changes are permanent
	print(locations)
see_the_world()

#3.9 Dinner Guests
'''In this we will take our guest lise from an earlier lesson and simply add a variable called guest_count and use
that to specify the number of guest that are coming'''
def guest_list():
	invites = ['Kasparov', 'Carlsen', 'Fisher']
	invites.insert(3, 'Hikaru')
	invites.append('Gotham')
	guest_count = len(invites)
	print(f"The people invited to the party are {invites} , so plan for {guest_count} guests.")
guest_list()

#3.10 
'''I think I've done a pretty good job at not copying the book examples, but I will still attempt this
used: insert, title, append, pop, changing a item using indexing, del, and remove'''
def using_everything():
	list = []
	list.insert(0, 'alex')
	print(list[0].title())
	list.append('Barcelona')
	cant_afford = list.pop()
	print(f'I doubt I\'ll ever go to {cant_afford}!')
	list[0] = 'Changed_Name'
	print(list)
	del list[0]
	print (list)
	list.append('Remember you can delete by name')
	print(list)
	list.remove('Remember you can delete by name')
	print(list)
using_everything()
'''The rest of the chapter is what we practiced in excercises 3.8-3.10 including:
sort() - permanent
sorted() - creates a instance of the list but doesn't change the original
reverse() - permanent but can be easily reverse() again
len() - helps to easily identify the length or number of elements in a list starting with 1 '''