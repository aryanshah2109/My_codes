dic = {}
print("Welcome to The Grand Auction!")
while True:
    key = input("What's your name? ")
    val = int(input("Enter your bid: $"))
    add_bid = input("Is there any other bidders? Input yes or no: ").lower()
    if(add_bid != "yes" or add_bid != "no"):
        print("Incorrect input!")
        break
    dic.update({key:val})
    if(add_bid == "no"):
        all_bids = []
        for i in dic:
            all_bids.append(dic[i])

        winning_bid = max(all_bids)
        winning_bidder_list = [key for key,value in dic.items() if value==winning_bid]
        winning_bidder = "".join(winning_bidder_list)
        print(f"The maximum bid was: ${winning_bid} made by {winning_bidder}")
        break


