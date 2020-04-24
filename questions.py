def scene1():
    print ("After the cleaning incident, your stepsisters told you to iron their clothes. What is your response?")
    print ("1: Okay my dear sisters!; 2: I will do it later.; 3: I don't wanna do it! 4: Why don't you do it?!")
    response= input()
    if response == "1":
        points += 1
    elif response == "2":
        points += 2
    elif response == "3":
        points += 3
    elif response == "4":
        points += 4
    else:
        print("Sorry, I don't understand this response.")
    
    
def scene5():
    print ("What kind of dress do you decide to wear to the ball?")
    print ("1: Modest; 2: Goth; 3: Sexy; 4: No dress, you wear a tux")
     response= input()
    if response == "1":
        points += 1
    elif response == "2":
        points += 2
    elif response == "3":
        points += 3
    elif response == "4":
        points += 4
    else:
        print("Sorry, I don't understand this response.")


    
    
def scene7():
    print ("Your stepmom finds out that you went to the ball and is trying to lock you in the attic. What do you do?")
    print ("1. You don’t fight back and let her lock you in the attic, as you don't want her to retaliate in a worse way. 2. You angrily ask her why she’s doing this and you get locked in the attic, but not without a struggle. 3. You physically fight your stepmom alone and escape. 4. You physically fight your stepmom and stepsisters with the help of of the mice and you escape.")
    response= input()
    if response == "1":
        points += 1
    elif response == "2":
        points += 2
    elif response == "3":
        points += 3
    elif response == "4":
        points += 4
    else:
        print("Sorry, I don't understand this response.")
