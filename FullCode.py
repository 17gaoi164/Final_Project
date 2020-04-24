def playagain():
	answer == input("Do you want to play again? Y or N? ")
	if answer == "Y" or answer == "y":
		print("Let's start over!")
		scene1()

	elif answer == "N" or answer == "n":
		print("See you!")
    
    points = 0

def scene1(points):

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


def scene2(points):
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
	
	return points


def scene3(points):
    print("Later that night, you walk by your sisters' room and see them trying on gorgeous dresses.")
    print("You ask them what it's for, but the just laugh smugly. 'What if a maid like you doesn't need to know?")
    print("Do you give an angry response or a compliant response? What do you say?")
    response = input("You:")
    from random import choice
    def respond(comment):
        points = 0
        if contains(comment,angryWords):
            points = points + 2
            print("They look shocked at your outburst, but they still say with arrogance, 'We're going to a ball at the palace. And you're not invited.'")
        elif contains(comment,submissiveWords):
            points = points +  0
            print("They nod. 'Good bye', they say. The next morning, however, as you walk by their door to prepare them breakfast, you hear them laughing. 'I'm so excited for the ball!' they exclaim. You realize that last night, they had been trying on dresses for the ball.")
        else:
            points = points + 1
            print("But they don't even listen to what you have to say. They laugh over your response and slam the door shut. You eavesdrop, and realize that they're trying on clothes for a ball at the palace.")
    def contains(sentence,words):
        wordsInSentence = [word for word in words if word in sentence]
        return len(wordsInSentence) >= 1
    angryWords = "deserve desire want angry mad unfair upset fight !"
    submissiveWords = "okay fine ... ok right alright sure yes agree"
    print(respond(response))
    return points

def scene4(points):
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
	return points

def scene5(points):
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
	
	return points

def scene6(points, past):
    print("After walking to the palace and arriving at the ball, everything is magical. A charming young man asks you to dance. You agree, and find out that he's the prince. Could anything be better? You spend hours with each other, talking and dancing. But the clock suddenly strikes midnight.")
    if past == 1:
        print("You realize your sisters are going back home at midnight, and they will be suspicious if you are not there if they call you to make them some tea after a night out. In your haste running back home and away from the prince, you leave behind a shoe.")
    if past == 2:
        print("You realize the fairy godmother's magic wears off then, and in your haste running back home and away from the prince, you leave behind a shoe.")
    return points


def scene7(points):
	print ("However, your stepmom finds out that you went to the ball and is trying to lock you in the attic. What do you do?")
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
	
	return points

def scene8():

	print("You then hear that the Price is looking for you everywhere. 'He has been going to everyone's house to find the girl,' you hear Anastasia say.")
	print("You hear the doorbell right. Soon you hear your. step-mom caming into your room. 'Don't you dare come downstairs. He is not here for you so stay inside or else you'll get punished,' she hissed.")

	decision = input("Do you... \n A. Decide to do as your step-mom says. \n B. Disobey her and go downstairs.\n")

	if decision == "A":
		print("... story continues ...")
		points += 0
		scene9()

	elif decision == "B":
		print("... story continues ...")
		points += 3
		scene10()

scene8()

def scene9():

	print("You hear the Prince talk to your step-mother. 'Is there anyone else in this house that is not present in room?' he asks. Your step-mother quickly responds with a firm no.")
	print("You then realize that you are in love with the Prince and want to see him.")

	decision = input("Do you... \n A. Decide to obey your step-mom and stay in your room. \n B. Disobey her and go downstairs.\n")

	if decision == "A":
		print("... story continues ...")
		points += 0
		scene11()

	elif decision == "B":
		print("... story continues ...")
		points += 3
		scene10()

scene9()
def scene10():

	print("")
	print("You then realize that you are in love with the Prince and want to see him.')

	decision = input("Do you... \n A. Decide to obey your step-mom and stay in your room. \n B. Disobey her and go downstairs.\n")

	if decision == "A":
		print("... story continues ...")
		points += 0
		scene12()

	elif decision == "B":
		print("... story continues ...")
		points += 3
		scene12()

scene10()
	
