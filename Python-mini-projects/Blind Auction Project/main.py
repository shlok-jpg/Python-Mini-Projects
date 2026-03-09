

auction = {}
new_bids = "yes"
while not new_bids == "no":

    name = input("Enter your name: ")
    bid = input("Enter your bid: ")


    auction[name] = bid
    print(auction)
    new_bids = input("Press enter yes to continue or no to stop")
    a= "\n"
    print(a*10000)

max_value = max(auction.values())
print(max_value)
for name in auction:
     if auction[name] == max_value:
         print(f'the highest bid is of{name} of value{max_value}')


