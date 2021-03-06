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
	print("It was a bright Monday morning. Cinderella's step mom drusted into her room and ordered her to clean the house. 'I want the house clean by 12!', Lady Tremaine yelled.")

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
	print ("A: Okay my dear sisters! \n B: I will do it later. \n C: I don't wanna do it \n D: Why don't you do it?! \n")
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
		past = "2"
		scene5()

	elif decision == "B":
		print("... story continues ...")
		points += 1
		past = "1"
		scene6()

	elif decision == "C":
		print("... story continues ...")
		points += 2
		past = "1"
		scene6()
		
	return points


def scene5(points):
	print("After some intense cleaning, you decide to take a break. Although you know your step-mother is right, you wish you could go to the ball. You sigh and get back up to dust the fireplace, when a fairy appears before your eyes.")
	print("'Cinderella!' she says, 'How could you not go to the ball.' Surprised you ask her who she is, and where she came from. 'I'm your fairy godmother of course, and I am here to take you to the ball!' You feel somewhat excited and realize that you really did want to go to the ball.")
	print("'So what kind of dress can I get for you darling? I offer quite a variety!' your fairy godmother proudly announces.'")
	      
	decision = input("Do you wear... \n A. A modest dress \n B. A goth dress \n C. A sexy dress \n D. No dress, you decide to go for a tux \n")

	if decision == "A":
		print("'Bibbidi bobbidi boo' and a modest dress appears on you!")
		points += 0
		scene7()

	elif decision == "B":
		print("'Bibbidi bobbidi boo' and a goth dress appears on you!")
		points += 1
		scene7()

	elif decision == "C":
		print("'Bibbidi bobbidi boo' and a sexy dress appears on you!")
		points += 2
		scene7()
	
	elif decision == "D":
		print("'Bibbidi bobbidi boo' and a tux appears on you!")
		points += 3
		scene7()
		
	return points
		


def scene6(points):
	print ("What kind of dress do you decide to wear to the ball?")
	print ("A: Modest; B: Goth; C: Sexy; D: No dress, you wear a tux")
     response= input()
    if response == "A":
        points += 0
	scene7()
    elif response == "B":
        points += 1
	scene7()
    elif response == "C":
        points += 2
	scene7()
    elif response == "D":
        points += 3
	scene7()
    else:
        print("Sorry, I don't understand this response.")
	
	return points

def scene7(points, past):
    print("After walking to the palace and arriving at the ball, everything is magical. A charming young man asks you to dance. You agree, and find out that he's the prince. Could anything be better? You spend hours with each other, talking and dancing. But the clock suddenly strikes midnight.")
    if past == 1:
        print("You realize your sisters are going back home at midnight, and they will be suspicious if you are not there if they call you to make them some tea after a night out. In your haste running back home and away from the prince, you leave behind a shoe.")
    if past == 2:
        print("You realize the fairy godmother's magic wears off then, and in your haste running back home and away from the prince, you leave behind a shoe.")
    return points


def scene8(points):
	print ("However, your stepmom finds out that you went to the ball and is trying to lock you in the attic. What do you do?")
	print ("A. You don’t fight back and let her lock you in the attic, as you don't want her to retaliate in a worse way \n B. You angrily ask her why she’s doing this and you get locked in the attic, but not without a struggle. \n C. You physically fight your stepmom alone and escape. \n D. You physically fight your stepmom and stepsisters with the help of of the mice and you escape. \n")
    response= input()
    if response == "A":
		print("The mice free you by stealing the key to the attic from your stepmother.")
        points += 0
	scene9()
    elif response == "B":
	print("The mice free you by stealing the key to the attic from your stepmother.")
        points += 1
	scene9()
    elif response == "C":
	print("You can go show the Duke that the slipper fits you.")
        points += 2
	scene9()
    elif response == "D":
	print("You can go show the Duke that the slipper fits you.")
        points += 3
	scene9()
    else:
        print("Sorry, I don't understand this response.")
	
	return points

def scene9():


def scene10():
	
def scene11():
	
def scene12():
	
	
	def playagain()
	
	

	
	
	
	
if points <= 9:
	print ("You are not very rebellious")
	elif points <= 18:
		print ("You're somewhat rebellious")
		elif points <= 27:
			print ("You are super rebellious")
			

scene1()

