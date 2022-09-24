#!/usr/bin/python3
#taha-shaikhh 
import random

lst = ["stone","paper","scissor"]
print("*******-------Welcome to the Game-------*******")
print('You have 10 lives. \n')
com_point = 0
usr_point = 0
n = 0
while n < 10:
	inp = input("-->Enter stone,paper,scissor<--\n").lower()
	r = random.choice(lst)
	if inp == r:
		print(f"You chose {inp} and Computer chose {r}")
		print("Tied")
		print(f"Your Point {usr_point} \t Computer Point {com_point}\n\n")
		n+=1
	elif inp == 'stone' and r == 'paper' or inp == 'scissor' and r == 'stone' or inp == 'paper' and r == 'scissor':
		print(f"You chose {inp} and Computer chose {r}")
		print("Computer Wins")
		com_point = com_point + 1
		print(f"Your Point {usr_point} \t Computer Point {com_point}\n\n")
		n+=1
	elif inp == 'stone' and r == 'scissor' or inp == 'scissor' and r == 'paper' or inp == 'paper' and r == 'stone':	
		print(f"You chose {inp} and Computer chose {r}")
		print("You win")
		usr_point = usr_point + 1
		print(f"Your Point {usr_point} \t Computer Point {com_point}\n\n")
		n+=1
	else:
		print("Invalid Input")
		
		
if com_point == usr_point:
	print("Game Tied")
	
elif com_point < usr_point:
	print("\n\nCongratulations, '''''You are the Winner'''''")
	print(f"You win with {usr_point} points")
else:
	print("\n\nSorry, You lose the Game \n Better Luck Next Time :( ")
	print(f"Computer win with {com_point} points")