import random as r

dict = {
    "Virat Kohli" : 8000000,
    "MS Dhoni" : 2000000,
    "Sachin Tendulkar" : 3000000,
    "Rohit Sharma" : 4000000,
    "Ishant Sharma" : 100000,
    "Bhuvneshwar Kumar" : 120000,
    "Axar Patel" : 130000,
    "Hardik Pandya" : 2000000,
    "Shreyas Iyer" : 500000,
    "Jasprit Bumrah" : 5000000,
    "Shubhman Gill" : 1000000,
    "Mohammad Siraj" : 900000
}
 
def higherLower():
    points = 0
    print("Welcome to the higher lower game: ")

    while(True):
        print("Welcome to the higher lower game: ")
        a = r.choice(list(dict))
        b = r.choice(list(dict))
        
        print("Choose which has more followers:")
        print(f"{a} or {b}")
        usersChoice = input("Enter your choice: ").lower()
        if usersChoice not in [a.lower(),b.lower(),"exit"]:
            print(f"Invalid input! Exiting the game. Current points: {points}")
        elif usersChoice == "exit":
            print(f"Exiting the game. Current points: {points}")
            return
        if usersChoice == a.lower() and dict.get(a) > dict.get(b) :
            print(f"You scored a point. Current points: {points} ")
            continue
        elif usersChoice == a.lower() and dict.get(a) < dict.get(b):
            print(f"You lost. Exiting the game. Current points: {points}")        

    

higherLower()


