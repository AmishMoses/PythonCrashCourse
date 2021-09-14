#!/usr/bin/env/ python3
'''In the last chapter when we were working with list we already started implementing 
looping through list with a for loop, but now we will work on that concept directly'''
# LOOPING THROUGH A LIST
def non_looped_list():
	magicians = ['David', 'Alice', 'Chris']
	print(f"Great trick {magicians[0]}")
	print(f"Great trick {magicians[1]}")
	print(f"Great trick {magicians[2]}")
non_looped_list()
'''You can see how accessing each element in the list individually like this calls for multiple 
repetitive lines of code. Instead of this, lets try using a for loop that will access each
element for us with much less code'''
def looped_list():
	magicians = ['David', 'Alice', 'Chris']
	for magician in magicians: 
		print(f"I really enjoyed the show {magician}")
looped_list()
'''Note that using magician as a varible is just a way of using meaningful name to match the list
the for loop would execute the same with any variable name. The for loop will run through the list 
associating each name in magicians with magician until the list is empty and then simply end'''

# DOING MORE WORK WITHIN A FOR LOOP
def more_looped_list():
	magicians = ['david', 'alice', 'chris']
	for magician in magicians: 
		print(f"I really enjoyed the {magician.title()}")
		#as long as you keep the lines of code formatted correctly
		#all lines of code indented under the for loop will be
		#considered nested and run inside the same loop
		print(f"{magician.upper()}! I can't wait for your next show.\n")
		#to break out of the for loop simply break the indentation
		#subsequently to create a complex nested for loop you would indent further
	#this broke out of the loop
	print("This executed after the loop finished all tasks")
more_looped_list()

'''Remember many common mistakes can happen in this sceanario. Maybe you indented the last line and therefore
it was also looped and printed 3 times, maybe you forgot your : after magicians: all loops we will be
working with will require the : after the loop has been staged.'''