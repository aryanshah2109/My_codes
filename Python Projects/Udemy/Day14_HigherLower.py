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
    print("\nWelcome to the higher lower game: ")
    a = r.choice(list(dict)) 
    b = r.choice(list(dict))
    valA = dict.get(a)
    valB = dict.get(b)
    while(True):
        print("\nChoose which has more followers:")
        print(f"{a} or {b}")
        usersChoice = input("\nEnter your choice: a or b: ").lower()
        if usersChoice not in ["a","b","exit"]:
            print(f"\nInvalid input! Exiting the game. Current points: {points}")
            break
        elif usersChoice == "exit":
            print(f"\nExiting the game. Current points: {points}")
            break
        if usersChoice == a.lower() and valA > valB :
            points += 1
            print(f"\nYou scored a point. Current points: {points} ")            
            dict.pop(a)
            a = b
            valA = dict.get(b)
            b = r.choice(list(dict))
            valB = dict.get(b)
            
        elif usersChoice == a.lower() and valA < valB:
            print(f"\nYou lost. Exiting the game. Current points: {points}")
            break        
        elif usersChoice == b.lower() and valA < valB:
            points += 1
            print(f"\nYou scored a point. Current points: {points} ")
            b = r.choice(list(dict))
            valB = dict.get(b)
        elif usersChoice == b.lower() and valA > valB:
            print(f"\nYou lost. Exiting the game. Current points: {points}")                     
            break
    

higherLower()


