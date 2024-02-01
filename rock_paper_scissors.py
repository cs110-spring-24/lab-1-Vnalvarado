import random
cpu = random.randint(1,3)

user=input("Enter rock, paper, or scissors: ")

if user== "rock":
	if cpu == 1: # cpu chose rock 
		print("Tie game!")
	elif cpu==2: #Cpu chose paper
		print("You lost")
	else: # CPU Chose scissors
			print("You win")

if user=="scissors":
	if cpu==1: #cpu chose rock
		print("You lose!")
	elif cpu==2: #CPI chose papaer 
		print("You win!")
	else: # CPU chose scissors: 
		print("Tie game!")

if user=="paper":
	if cpu==1: # CPU chose rock
		print("You win!")
	elif cpu==2: # CPU chose paper
		print("Tie Game!")
	else: # CPU chose scissors
		print("You Lose!")