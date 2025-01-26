import random as r
deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
'''
pickAgain = input("Do you want to pick another card? Type yes or no: ").lower()
    if(pickAgain == "yes"):
        pickAnotherCard(usersCards)
    elif(pickAgain == "no"):
        
    else:
        print("Invalid input! Exiting the game")
        break
'''

def pickAnotherCard(usersCardsCurrent:list, dealersCardsCurrent:list):    
    while True:
        newCard = r.random(deck)
        usersCardsCurrent.append(newCard)
        print("Your cards are: ",usersCardsCurrent)

        usersCardsSum = sum(usersCardsCurrent)
        dealersCardsSum = sum(dealersCardsCurrent)
        
        print("Current sum: ",usersCardsSum)
        if(dealersCardsSum > usersCardsSum and dealersCardsSum < 21):
            print("The dealer won!")
        elif((dealersCardsSum < usersCardsSum and usersCardsSum <= 21) or dealersCardsSum ):
            print("You Won! Congratulations")
        elif():
            pass
    


def checkReplay():
    playAgain = input("Do you want to play again? Type yes or no: ").lower()
    if(playAgain == "yes"):
        return True
    elif(playAgain == "no"):
        return False
    else:
        print("Invalid input!")
    
print("Welcome to Blackjack!")
while True:
    usersCards = r.sample(deck,2)
    dealersCards = r.sample(deck,2)
    print("Your cards are ",usersCards)
    print("Dealers' first card is: ",dealersCards[0])
    initial_sum = sum(usersCards)
    if(initial_sum == 21):
        print("Blackjack!!!! You won. Congratulations")
        if(checkReplay()):
            continue
        else:
            break
    elif(initial_sum > 21):
        print("Your initial total went over 21. You lost :( ")
        if(checkReplay()):
            continue
        else:
            break
    while True:
        pickAgain = input("Do you want to pick another card? Type yes or no: ").lower()
        if(pickAgain == "yes"):
            pickAnotherCard(usersCards)
            
        elif(pickAgain == "no"):
            pass
        else:
            print("Invalid input! Exiting the game")
            break


    