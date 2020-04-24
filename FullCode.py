def playagain():
	answer == input("Do you want to play again? Y or N? ")
	if answer == "Y" or answer == "y":
		print("Let's start over!")
		scene1()

	elif answer == "N" or answer == "n":
		print("See you!")
    

def scene1():
def scene1():
    points = 0

	print("Once upon a time, there was a girl named Cinderella. She lived with her step-mother, Lady Tremaine, and two step-sisters, Anastasia and Drizella. They would make Cinderella work all day and give her little to no food.")
	print("It was a bright Monday mornig. Cinderella's step mom drusted into her room and ordered her to clean the house. 'I want the house clean by 12!', Lady Tremaine yelled.")

	decision = input("Do you... \n A. Decide to do as your step-mom says. \n B. Tell her you'll do it later. \n C. Tell her you don't feel like doing it. \n D. Tell her to do it herself.\n")

	if decision == "A":
		print("... story continues ...")
		points += 0
		scene2()

	elif decision == "B":
		print("... story continues ...")
		points += 1
		scene2()

	elif decision == "C":
		print("... story continues ...")
		points += 2
		scene2()
    
	elif decision == "D":
		print("... story continues ...")
		points += 3
		scene2()

    return points

scene1()

def scene2():


def scene3():

def scene4():
	print("After hearing about the ball from your sisters, you decide to ask your stepmother to attend as well.")
	print("... story continues ...")

	decision = input("Do you... \n A. Decide against going, as your stepmother wishes. \n B. Decide to go secretly anyways. \n C. Confront your mother and tell her that you're going regardless of her opinion.\n")

	if decision == "A":
		print("... story continues ...")
		points += 0
		scene5()

	elif decision == "B":
		print("... story continues ...")
		points += 1
		scene6()

	elif decision == "C":
		print("... story continues ...")
		points += 2
		scene6()

def scene5():


def scene6():


def scene7():


def scene8():


def scene9():
