#Priya: Ask your step mother if you can also go to the ball, but you mom says no
#Options: 1. No you follow your mom’s wishes (fairy godmother appears) 2. You decide to secretly go anyways (dress scene) 3. you confront your mother and tells her that you’re going regardless (dress scene)

points = 0

def scene4():
	print("After hearing about the ball from your step-sisters, you decide to ask your step-mother to attend as well.")
	print("When you ask her, she laughs, 'Cinderella, you have the house to clean, a filthy girl in rags doesn't belong at the Prince's ball.'")

	decision = input("Do you... \n A. Decide against going, as your stepmother wishes. \n B. Decide to go secretly anyways. \n C. Confront your mother and tell her that you're going regardless of her opinion.\n")

	if decision == "A":
		print("Your step-mother is right, a palace is no place for a house maid like you. You go about your day cleaning the house, and see your step- sisters and -mother off to the ball in the evening.")
		points += 0
		scene5()

	elif decision == "B":
		print("You continue cleaning the house inconspicuously, planning a way to get to the ball. Once evening approaches, you see your step- sisters and -mother off to the ball. Running up to your step-sisters' dresser, you look for a dress you can wear to the ball.")
		points += 1
		scene6()

	elif decision == "C":
		print("Appalled at your step-mother's statement, you yell, 'I would obviously clean myself up, I'm going to find a dress and I am going to go to the ball regardless of your wishes!' You run to your step-sisters' dresser and find a dress to wear.")
		points += 2
		scene6()

scene4()

#scene5() is the fairygodmother scene - change text of dress scene
#scene6() is the dress scene
