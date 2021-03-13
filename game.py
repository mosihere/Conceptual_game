import time
time.sleep(1)
print('Hi, What is your name:')
name = input()

# Start Game
def StartGame():
	print('Welcome to this conceptual game',name)
	time.sleep(2)
	print()

	print(name,'you lost in a jungle! You don"t have any map or something helpful there')
	time.sleep(2)
	print()

	print('you have 3 choices!')
	time.sleep(2)
	print()

	print('1-make fire --> make a fire and sleep there tonight')
	time.sleep(2)
	print('2-keep going --> keep going and try to find a safe place')
	time.sleep(2)
	print('3-nearest cave --> go to a nearest cave there!')
StartGame()

choice = input()

# Choices Start here

def choices():
	# First Choice
	if choice == 'make fire'.lower():
		print("well, it seems OK.")
		time.sleep(2)
		print('wait, A wolf is coming...')
		print()
		time.sleep(2)
		print('What do you want to do!')
		time.sleep(2)

		print()
		print('You have two choices!')
		time.sleep(2)

		print('1-Run away')
		time.sleep(2)
		print('2-kill wolf--> Try to kill wolf')

		first_option_choice = input()

		if first_option_choice == 'run away'.lower():
			print('you fell on the ground')
			time.sleep(2)
			print('the wolf is coming...')
			time.sleep(2)
			print('Wanna shout and ask for help or try to fight on your own?')
			time.sleep(2)
			print('Shout or fight ?')
			time.sleep(2)
			shout_or_fight = input()
			if shout_or_fight == 'shout'.lower():
				time.sleep(2)
				print('HEEEEEEEEY')
				time.sleep(1)
				print('ANYONE HEREEEE !')
				time.sleep(2)
				print('HEEEELP MEE')
				time.sleep(1)
				print('a hunter shoot the wolf!')
				time.sleep(1)
				print('You are safe :)')
			
			elif shout_or_fight == 'fight'.lower():
				time.sleep(2)
				print('Try to attack wolf')
				time.sleep(1)
				print('Wolf hurt you as hell')
				time.sleep(2)
				print('You Are Dead :(',name)
			
			else:
				print('That is not in game')

		elif first_option_choice == 'kill wolf'.lower() or 'kill'.lower():
			print('you wannna fight the wolf')
			time.sleep(2)
			print()
			print('try to look around and find something to use as a weapon!')
			print()
			time.sleep(2)
			print('There is a sharp broken branch right here!')
			time.sleep(2)
			print('And also there is a knife')
			print()
			time.sleep(2)
			print('which weapon you prefer ?')
			time.sleep(2)
			print('knife or branch ?')

			choosen_weapon = input()
			if choosen_weapon =='branch'.lower():
				print('You took the branch')
				time.sleep(2)
				print()
				print('Try to attack the wolf')
				time.sleep(2)
				print('Press "A" to attack the wolf')
				time.sleep(2)
				attack = input()
				if attack == 'A'.lower():
					print('You Are Attacking The wolf ...')
					time.sleep(2)
					print('Your Branch broke!')
					time.sleep(2)
					print('Wolf hurt you hard',name)
					time.sleep(2)
					print('You are Bleeding...')
					time.sleep(2)
					print('You are Dead :( ')

				else:
					print('You did not attack wolf')
					time.sleep(2)
					print('You Are Dead :( ')

			elif choosen_weapon == 'knife'.lower():
				print('You took the knife')
				time.sleep(2)
				print('Try to attack wolf')
				time.sleep(2)
				print('Press "A" to attack')
				time.sleep(2)
				knife_attack = input()
				if knife_attack == 'A'.lower():
					time.sleep(2)
					print('Well Done, keep attacking by press "A"')
					second_attack = input()
					if second_attack == 'A'.lower():
						print('You killed the wolf')
						time.sleep(2)
						print('You Are Safe now',name)
					else:
						print('You did not attack wolf')
						time.sleep(2)
						print('You died :(')
				
				else:
					print('You did not hit the wolf')
					time.sleep(2)
					print('You Are Dead :(( ')

			else:
				print('That is not support in game...')

		else:
			print('This is not in game...')

	# Second Choice
	elif choice == 'keep going'.lower():
		print('You are so tired and out of energy!') 
		time.sleep(2)
		print('wanna sleep or keep walking?(sleep, walking)')
		second_choice = input()
		if second_choice == 'walking'.lower():
			print('you fucked up and fell down on the ground and u cant keep walking')

		elif second_choice == 'sleep'.lower():
			print('well, you find a place, that seems ok!')
			time.sleep(2)
			print('drink --> want to drink some water from the fountain near you?')
			time.sleep(2)
			print('sleep --> wanna sleep right now?')
			another_choice = input()

			if another_choice == 'drink'.lower():
				time.sleep(2)
				print('the water was poisend by aliens!')  
				time.sleep(2)
				print('You are dead')

			elif another_choice == 'sleep'.lower():
				print('there is a big rock near you')
				time.sleep(2)
				print('would you wanna sleep on the rock?')
				sleep_choice = input()
				
				if sleep_choice == 'y'.lower() or 'yes'.lower():
					print('good night',name)
				else:
	
					print('Ok sleep on the ground',name)

	# Third Choice
	elif choice == 'nearest cave'.lower():
		print('it is dark and spooky!')
		time.sleep(2)
		print('there is a big caves"s bear behind you')
		time.sleep(2)
		print('what are you going to do now {}!'.format(name))
		time.sleep(2)
		print('you have 2 choies!')
		time.sleep(2)
		print('1-run --> run away and run and run and run...')
		time.sleep(2)
		print('2-sleep on the ground --> to seems you are dead and maybe bear let you go')
		cave_choice = input()

		if cave_choice == 'run'.lower() or '1':
			print('The bear is too fast')
			time.sleep(2)
			print('it seems he can haunt you right now!!!')
			time.sleep(2)
			print('You are Dead',name)
		elif cave_choice == 'sleep on the ground'.lower() or '2':
			print('The bear is too crazy')
			time.sleep(2)
			print('He is roaring as hell...')
			time.sleep(2)
			print('The Bear let you go')
			time.sleep(2)
			print('You are survived',name)
		else:
		
			print('you dont choose the true answer')

	# If user fill out input with sth else that not exist in game
	else:
		print('Thats not in the game...')

choices()
