def playagain():
	answer == input("Do you want to play again? Y or N? ")
	if answer == "Y" or answer == "y":
		print("Let's start over!")
		scene1()

	elif answer == "N" or answer == "n":
		print("See you!")
    
    points = 0

def scene1():

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
	print ("After the cleaning incident, your stepsisters tell you to iron their clothes. What is your response?")
	print ("A: Okay my dear sisters!; B: I will do it later.; C: I don't wanna do it! D: Why don't you do it?!")
    response= input()
    if response == "A":
		print("The stepsisters walk away smugly, feeling satisfied that you did their bidding.")
        points += 0
	scene3()
    elif response == "B":
	print("The stepsisters tell you that you better do it now, and walk away, annoyed.")
        points += 1
	scene3()
    elif response == "C":
	print("The stepsisters say that you have to do it or they'll tell your stepmother, and walk away, upset.")
        points += 2
	scene3()
    elif response == "D":
	print("The stepsisters get so angry, tell you that you won't get away with this, and stomp away, furious.")
        points += 3
	scene3()
    else:
        print("Sorry, I don't understand this response.")


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
	print ("What kind of dress do you decide to wear to the ball?")
	print ("A: Modest; B: Goth; C: Sexy; D: No dress, you wear a tux")
     response= input()
    if response == "A":
        points += 0
	scene6()
    elif response == "B":
        points += 1
	scene6()
    elif response == "C":
        points += 2
	scene6()
    elif response == "D":
        points += 3
	scene6()
    else:
        print("Sorry, I don't understand this response.")



def scene6():


def scene7():
	print ("Your stepmom finds out that you went to the ball and is trying to lock you in the attic. What do you do?")
	print ("A. You don’t fight back and let her lock you in the attic, as you don't want her to retaliate in a worse way. B. You angrily ask her why she’s doing this and you get locked in the attic, but not without a struggle. C. You physically fight your stepmom alone and escape. D. You physically fight your stepmom and stepsisters with the help of of the mice and you escape.")
    response= input()
    if response == "A":
		print("The mice free you by stealing the key to the attic from your stepmother.")
        points += 0
	scene8()
    elif response == "B":
	print("The mice free you by stealing the key to the attic from your stepmother.")
        points += 1
	scene8()
    elif response == "C":
	print("You can go show the Duke that the slipper fits you.")
        points += 2
	scene8()
    elif response == "D":
	print("You can go show the Duke that the slipper fits you.")
        points += 3
	scene8()
    else:
        print("Sorry, I don't understand this response.")

def scene8():


def scene9():
