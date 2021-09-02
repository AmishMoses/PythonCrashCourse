#!/usr/bin/env3/ python3
'''3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
•	 Start with your program from Exercise 3-4. Add a print() call at the end
of your program stating the name of the guest who can’t make it.
•	 Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
•	 Print a second set of invitation messages, one for each person who is still
in your list.
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
•	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
call to the end of your program informing people that you found a bigger
dinner table.
•	 Use insert() to add one new guest to the beginning of your list.
•	 Use insert() to add one new guest to the middle of your list.
•	 Use append() to add one new guest to the end of your list.
•	 Print a new set of invitation messages, one for each person in your list
3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
•	 Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
•	 Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
•	 Print a message to each of the two people still on your list, letting them
know they’re still invited.
•	 Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.'''

#3.4 Guest List
def dinner_list():
	invites = ['Kasparov', 'Carlsen', 'Fisher']
	for people in invites:
		print(f"Hello {people}, would you like to attend a dinner event at my house?")
#3.5 Changing Guest List
		print(f"{invites[2]} wont be able to make it to dinner.")
		new_invites = invites
		new_invites[2] = 'Hikaru'
		print(new_invites)
	for remaining in new_invites:
		print(f"Hey, {remaining}, I really hope you can still make it! Fisher is out!")
#3.6 More Guests
		print(f"{remaining} I found more space at the table.")
	third_invites = new_invites
	third_invites.insert(0, 'Nepo')
	third_invites.insert(3, 'Gotham')
	third_invites.append('Giri')
	print(third_invites)
	for remaining in third_invites:
		print(f"If you are getting this you are in. See you soon {remaining}")
#3.7 Shrinking Guest Lists	
	last_call = third_invites
	for guests in last_call:
		print(f"I promise I will not adjust the list again {guests}, but I can only invite two of you.")
		uninvited = last_call.pop()
		print(f"I'm sorry {uninvited} you haven't been chosen")
		uninvited = last_call.pop()
		print(f"{uninvited} you are also uninvited")
		for last_two in last_call:
			print(f"Okay {last_two}, you are the chosen ones!")
		print(last_call)
	
dinner_list()