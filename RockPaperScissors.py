from random import randint

# Call with 1: Returns "Rock"
def convertToSign(value:int)->str:
    return ["Rock", "Paper", "Scissors"][value-1]

def printHelper():
    print("/"*10 + " THIS IS THE HELP SECTION " + "/"*10)

# Handle Player's input
def getPlayerInput()->int:
    action, finalAction = None, None
    while(finalAction == None):
        action = input("Choose a number between 1 and three representing respectively Rock, Paper and Scissors: ")
        try:
            action = int(action)
            if (1 <= action <= 3):
                finalAction = action
            else:
                print("Wrong input: The range of the input must be between 1 and 3")
        except(ValueError):
            if action == "/exit":
                print("Game ended!")
                exit()
            elif action == "/help":
                printHelper()
            else:
                print("Wrong input: You must input a number!")
    return finalAction

def DisplayScore(name1, score1, sign1, name2, score2, sign2):
    print(f"{name1} won the round with {sign1} against {sign2}")
    print(f"Current Score: {name1} : {score1} | {name2} : {score2}")

def PaperRockScissors(bo:int, p1_name, p2_name)->None:
    # Définir la variable p1_score qui va contenir le score du joueur1
    p1_score = 0
    # Définir la variable p2_score qui va contenir le score du joueur2
    p2_score = 0

    while(p1_score < bo and p2_score < bo):
        # Définir p1_action à l'aide du retour de la fonction getPlayerInput
        p1_action = getPlayerInput()
        # Définir p2_action à l'aide du retour de la fonction random
        p2_action = randint(1, 3)

        # Définir p1_sign qui contient le signe du joueur1
        p1_sign = convertToSign(p1_action)
        # Définir p2_sign qui contient le signe du joueur2
        p2_sign = convertToSign(p2_action)

        if (p1_action == p2_action):
            print(f"Draw between {p1_sign}!")

        elif (p1_action == 1): # Rock
            if (p2_action == 2): # Paper
                p2_score += 1
                DisplayScore(p2_name, p2_score, p2_sign, p1_name, p1_score, p1_sign)
            else: # Scissors
                p1_score += 1
                DisplayScore(p1_name, p1_score, p1_sign, p2_name, p2_score, p2_sign)

        elif (p1_action == 2): # Paper
            if (p2_action == 1): # Rock
                p1_score += 1
                DisplayScore(p1_name, p1_score, p1_sign, p2_name, p2_score, p2_sign)
            else: # Scissors
                p2_score += 1
                DisplayScore(p2_name, p2_score, p2_sign, p1_name, p1_score, p1_sign)
        else: # Scissors
            if (p2_action == 1): # Rock
                p2_score += 1
                DisplayScore(p2_name, p2_score, p2_sign, p1_name, p1_score, p1_sign)
            else: # Paper
                p1_score += 1
                DisplayScore(p1_name, p1_score, p1_sign, p2_name, p2_score, p2_sign)

    if (p1_score >= bo): # Player1 won!
        print(f"{p1_name} WON!")
    else: # Player2 won!
        print(f"{p2_name} WON!")

print("///// Commands:  /////\n/////   /help    /////\n/////   /exit    /////")
PaperRockScissors(3, "Antoine", "IA")