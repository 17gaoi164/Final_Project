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
		print("You comply with your mother, and get ready for a day of cleaning.")
		points += 0
		scene2(points)
	elif decision == "B":
		print("You decide to lounge in your room for a while, before getting up to clean the house.")
		points += 1
		scene2(points)
	elif decision == "C":
		print("You tell her that you don't want to do house cleaning today, to which she replies, 'I wasn't giving you an option!'")
		points += 2
		scene2(points)
	elif decision == "D":
		print("You tell that she should do it herself, to which she replies, 'I am providing a food and a roof over your head and you have the audacity to talk back to me!'")
		points += 3
		scene2(points)


def scene2(points):
	print ("After the cleaning incident, your stepsisters tell you to iron their clothes. What is your response?")
	print ("A: Okay my dear sisters! \n B: I will do it later. \n C: I don't wanna do it! \n D: Why don't you do it?! \n")
	
	response = input()
	
	if response == "A":
		print("The stepsisters walk away smugly, feeling satisfied that you did their bidding.")
		points += 0
		scene3(points)
	elif response == "B":
		print("The stepsisters tell you that you better do it now, and walk away, annoyed.")
		points += 1
		scene3(points)
	elif response == "C":
		print("The stepsisters say that you have to do it or they'll tell your stepmother, and walk away, upset.")
		points += 2
		scene3(points)
	elif response == "D":
		print("The stepsisters get so angry, tell you that you won't get away with this, and stomp away, furious.")
		points += 3
		scene3(points)
	else:
		print("Sorry, I don't understand this response.")


def scene3(points):
	print("Later that night, you walk by your sisters' room and see them trying on gorgeous dresses.")
	print("You ask them what it's for, but the just laugh smugly. 'What if a maid like you doesn't need to know?''")
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
	scene4(points)

def scene4(points):
	print("After hearing about the ball from your sisters, you decide to ask your stepmother to attend as well.")
	print("When you ask her, she laughs, 'Cinderella, you have the house to clean, a filthy girl in rags doesn't belong at the Prince's ball.'")
	
	decision = input("Do you... \n A. Decide against going, as your stepmother wishes. \n B. Decide to go secretly anyways. \n C. Confront your mother and tell her that you're going regardless of her opinion.\n")
	
	if decision == "A":
		past = 2
		print("Your step-mother is right, a palace is no place for a house maid like you. You go about your day cleaning the house, and see your step- sisters and -mother off to the ball in the evening.")
		points += 0
		scene5(points, past)
	elif decision == "B":
		past = 1
		print("You continue cleaning the house inconspicuously, planning a way to get to the ball. Once evening approaches, you see your step- sisters and -mother off to the ball. Running up to your step-sisters' dresser, you look for a dress you can wear to the ball.")
		points += 1
		scene6(points, past)
	elif decision == "C":
		past = 2
		print("Appalled at your step-mother's statement, you yell, 'I would obviously clean myself up, I'm going to find a dress and I am going to go to the ball regardless of your wishes!' You run to your step-sisters' dresser and find a dress to wear.")
		points += 2
		scene6(points, past)

def scene5(points, past):
	print("After some intense cleaning, you decide to take a break. Although you know your step-mother is right, you wish you could go to the ball. You sigh and get back up to dust the fireplace, when a fairy appears before your eyes.")
	print("'Cinderella!' she says, 'How could you not go to the ball.' Surprised you ask her who she is, and where she came from. 'I'm your fairy godmother of course, and I am here to take you to the ball!' You feel somewhat excited and realize that you really did want to go to the ball.")
	print("'So what kind of dress can I get for you darling? I offer quite a variety!' your fairy godmother proudly announces.'")

	decision = input("Do you wear... \n A. A modest dress \n B. A goth dress \n C. A sexy dress \n D. No dress, you decide to go for a tux \n")

	if decision == "A":
		print("'Bibbidi bobbidi boo' and a modest dress appears on you!")
		points += 0
		scene7(points, past)
	elif decision == "B":
		print("'Bibbidi bobbidi boo' and a goth dress appears on you!")
		points += 1
		scene7(points, past)
	elif decision == "C":
		print("'Bibbidi bobbidi boo' and a sexy dress appears on you!")
		points += 2
		scene7(points, past)
	elif decision == "D":
		print("'Bibbidi bobbidi boo' and a tux appears on you!")
		points += 3
		scene7(points, past)

def scene6(points, past):
	print ("What kind of dress do you decide to wear to the ball? \n")
	print ("A: Modest; \n B: Goth; \n C: Sexy; \n D: No dress, you wear a tux")
	
	response= input()
	
	if response == "A":
		points += 0
	elif response == "B":
		points += 1
	elif response == "C":
		points += 2
	elif response == "D":
		points += 3
	else:
		print("Sorry, I don't understand this response.")
	scene7(points, past)

def scene7(points, past):
	print("After walking to the palace and arriving at the ball, everything is magical. A charming young man asks you to dance. You agree, and find out that he's the prince. Could anything be better? You spend hours with each other, talking and dancing. But the clock suddenly strikes midnight.")
	
	if past == 1:
		print("You realize your sisters are going back home at midnight, and they will be suspicious if you are not there if they call you to make them some tea after a night out. In your haste running back home and away from the prince, you leave behind a shoe.")
	
	if past == 2:
		print("You realize the fairy godmother's magic wears off then, and in your haste running back home and away from the prince, you leave behind a shoe.")
	scene8(points)


def scene8(points):
	print ("However, your stepmom finds out that you went to the ball and is trying to lock you in the attic. You... \n")
	print ("A. don’t fight back and let her lock you in the attic, as you don't want her to retaliate in a worse way. \n B. angrily ask her why she’s doing this and you get locked in the attic, but not without a struggle. \n C. physically fight your stepmom alone and escape. \n D. physically fight your stepmom and stepsisters with the help of of the mice and you escape.")
	
	response= input()
	
	if response == "A":
		print("The mice free you by stealing the key to the attic from your stepmother.")
		points += 0
	elif response == "B":
		print("The mice free you by stealing the key to the attic from your stepmother.")
		points += 1
	elif response == "C":
		print("You can go show the Duke that the slipper fits you.")
		points += 2
	elif response == "D":
		print("You can go show the Duke that the slipper fits you.")
		points += 3
	else:
		print("Sorry, I don't understand this response.")
	scene9(points)



def scene9(points):
	print("You then hear that the Price is looking for you everywhere. 'He has been going to everyone's house to find the girl,' you hear Anastasia say.")
	print("You hear the doorbell right. Soon you hear your. step-mom caming into your room. 'Don't you dare come downstairs. He is not here for you so stay inside or else you'll get punished,' she hissed.")
	
	decision = input("Do you... \n A. Decide to do as your step-mom says. \n B. Disobey her and go downstairs.\n")
	
	if decision == "A":
		print("... story continues ...")
		points += 0
		scene10(points)
	
	elif decision == "B":
		print("... story continues ...")
		points += 3
		scene11(points)

def scene10(points):
	print("You hear the Prince talk to your step-mother. 'Is there anyone else in this house that is not present in room?' he asks. Your step-mother quickly responds with a firm no.")
	print("You then realize that you are in love with the Prince and want to see him.")
	
	decision = input("Do you... \n A. Decide to obey your step-mom and stay in your room. \n B. Disobey her and go downstairs.\n")
	
	if decision == "A":
		print("But the rats urge you to go down, and finally you listen to them and do.")
		print("... story continues ...")
		points += 0
		scene11(points)
	
	elif decision == "B":
		print("... story continues ...")
		points += 3
		scene11(points)

def scene11(points):
	print("You run downstairs to the main room and lock eyes with the Prince. You step-mom sees you and tells you to go upstais.")
	print("'Wait!' the Prince says.")
	print("'She is just our house maid,' your step-mother replies eyeing you up and down.")
	print("'Let her stay as well' the Prince says.")
	print("'She hasn't left the house at all this month. She doesn't have to stay,'your step-mother says.")
	print("'Doesn't matter,' the Prince says coming towards you. He then brings out his hand forward and looks at you. Without thinking too much about your step-mother, you take his hand and he leads you towards the sofa.")
	print("'Sit,' he says. You obey him. He then order the gaurds to bring the shoe. The guard does so and hands the prince your beautiful shoes that you lost while coming back from the ball.")
	print("The Prince then brings the shoe close to your feet and askes you to put it on. You put on the shoe and it fits perfectly, just like it did during the ball.")
	print("'Were you there?' the Prince asks you with a hopeful eyes.")
	decision = input("Do you... \n A. Say yes \n B. Say no.\n")
	if decision == "A":
		print("The prince says, 'Ah yes, I thought it was you.'")
		print("... story continues ...")
		points += 3
		scene12(points)
	elif decision == "B":
		print("The prince says, 'No, I remember you. You were definitely there.'")
		print("... story continues ...")
		points += 0
		scene12(points)

def scene12(points):
	print("'Ever since I first laid my eyes on you, I knew I loved you.' the Prince tells you")
	print("'Cinderella, will you make me the happiest man alive and marry me?' he asked you'")
	print("You looked around the room and saw your step-mother's angry face. You looked down at the Price. You realized it was your time to make your decision now")
	
	decision = input("Do you... \n A. Say yes, I'll marry you \n B. Say no.\n")
	
	if decision == "A":
		print("And they lived happily ever after.")
		playagain()
	
	elif decision == "B":
        	print("Soon after the incident, Cinderella moved to NYC and she lived happily ever after.")
		playagain()
	
	rebellionscore(points)



def rebellionscore(points):
	if points <= 9:
		print ("You are not very rebellious")
	if points <= 18:
		print ("You're somewhat rebellious")
	if points <= 27:
		print ("You are super rebellious")

scene1(points)
