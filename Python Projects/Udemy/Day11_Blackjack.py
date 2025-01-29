import random as r
deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def printUserCards(userCards:list):
    print("Your cards are ",userCards)
    userSum = sum(userCards)
    print(f"Current sum is {userSum}")   

def printDealersCards(dealersCards:list):
    print("Dealers cards are ",dealersCards)
    dealersSum = sum(dealersCards)
    print(f"Current sum is {dealersSum}") 

def checkConditions(userCards:list, dealersCards:list):
    dealersSum = sum(dealersCards)
    userSum = sum(userCards)
    print(f"Dealers cards are {dealersCards}")
    if( dealersSum > 21 ):
        print("Your won!! The sum of dealers cards is over 21")
        return
    if(dealersSum < 21 and dealersSum > userSum):
        print("You lost. The dealer is closer to 21")
    elif(dealersSum < 21 and dealersSum < userSum and dealersSum > 13):
        print("You won. You are closer to 21")
    elif(dealersSum == userSum and dealersSum<=21 and userSum<=21):
        print("Push! Its a tie")
    elif(dealersSum == 21 and userSum != 21):
        print("You lost. The sum of dealers cards is equal to 21")

print("Welcome to Blackjack!")
userCards = r.sample(deck,2)
dealersCards = r.sample(deck,2)
printUserCards(userCards)
print("Dealers' first card is: ",dealersCards[0])

if(sum(userCards) == 21):
    print("Blackjack!!!! You won. Congratulations")
    raise SystemExit
while(True):
    choice = input("Do you want to pick a card? Yes/No: ").lower()
    if(choice=="yes"):      # hit condition
        newCard = r.choice(deck)
        userCards.append(newCard)
        printUserCards(userCards)
        if(sum(userCards)>21):
            print("Bust! You lost. Your total went above 21")
            break
    elif(choice=="no"):     # halt condition
        dealersSum = sum(dealersCards)
        userSum = sum(userCards)
        checkConditions(userCards,dealersCards)
        while(dealersSum < 13):
            print("Adding a new card to the dealers' cards....")
            newCard = r.choice(deck)
            dealersCards.append(newCard)
            printDealersCards(dealersCards) 
            if(dealersSum > 13):
                checkConditions(userCards,dealersCards)
            break
        break
    else:
        print("Invalid input! Exiting the game!")
        raise SystemExit
        

        



        