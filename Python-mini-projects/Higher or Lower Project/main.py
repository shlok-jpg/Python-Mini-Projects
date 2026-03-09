import random
import art
import game_data

attempt = 1
Data = game_data.data
choice = random.randint(0,len(Data)-1)
first_choice = Data[choice]
Data.remove(first_choice)
score = 0
while attempt > 0:
#--------------------------------------------the choosing of data------------------------------------------------
    print(art.logo)
    print(f"Compare A - {first_choice["name"]} is a {first_choice["description"]}from {first_choice["country"]}")
    print(art.vs)
    choice = random.randint(0,len(game_data.data)-1)
    second_choice = game_data.data[choice]
    print(f"Compare B - {second_choice["name"]} is a {second_choice["description"]}from {second_choice["country"]}")
    Data.remove(second_choice)
#-----------------------------------------------------------------------------------------------------------------
    guess = input("Who has more followers? Type 'A' or 'B':")

    if guess == "a":
        if first_choice["follower_count"] > second_choice["follower_count"]:
            print("Good job!")
            score += 1
            first_choice = second_choice
            print(f"Your score is: {score}")
        else:
            print("hehehe, loser!")
            attempt = 0
            print(f"Your score was: {score}")
    elif guess == "b":
        if first_choice["follower_count"] < second_choice["follower_count"]:
            print("Good job!")
            score += 1
            first_choice = second_choice
            print(f"Your score is: {score}")
        else:
            print("hehehe, loser!")
            attempt = 0
            print(f"Your score was: {score}")