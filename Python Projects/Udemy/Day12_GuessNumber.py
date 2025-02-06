import random as r
print("Welcome to the number guessing game!")

difficulty = input("Choose a difficulty: Easy or Hard: ").lower()
if(difficulty == "easy"):
    print("I am thinking of a number between 1 to 100")
    ran = r.randint(1,101)
    print(f"The number is {ran}")
    for i in range(10):
        print(f"You have {10-i} attempts!")
        guess = input("Enter your guess: ")
        if(guess == "exit"):
            break
        guess = int(guess)
        if(guess>100):
            print("Invalid input!!")
            print("Try again")
        elif(guess == ran):
            print("You have got the correct answer!")
            break
        elif(guess > ran):
            print("Too high!")
            print("Try again")
        elif(guess < ran):
            print("Too low")
            print("Try again")
elif(difficulty == "hard"):
    print("I am thinking of a number between 1 to 1000")
    ran = r.randint(1,1000)
    print(f"The number is {ran}") 
    print("You have 5 guesses to guess the number!")
    for i in range(5):
        print(f"You have {5-i} attempts!")

        guess = input("Enter your guess: ")
        if(guess == "exit"):
            break
        guess = int(guess)
        if(guess>1000):
            print("Invalid input!!")
            print("Try again")            
        elif(guess == ran):
            print("You have got the correct answer!")
            break
        elif(guess > ran):
            print("Too high!")
            print("Try again")
        elif(guess < ran):
            print("Too low")
            print("Try again")

elif(difficulty == "exit"):
    raise SystemExit
else:
    print("Invalid input!")
        