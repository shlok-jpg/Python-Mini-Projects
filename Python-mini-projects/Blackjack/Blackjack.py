cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import art
import random
def blackjack_algo():
    if score > 21:
        print("You lose!, You are busted")
    elif comp_score == 21:
        print("You Lose! computer has the BLACKJACK")
    elif score == 21:
        print("You Win!, You have the BLACKJACK")
    elif score > comp_score:
        print("You Win!")
    elif score == comp_score:
        print("Draw")
    else:
        print("You Lose!")

play = input("Do you want to play Blackjack Game? type 'y' or 'n'")
while play.lower() == 'y':
    loop = True
    print(art.logo)
#your card
    your_card1 = random.choice(cards)
    your_card2 = random.choice(cards)
    score = your_card1 + your_card2
    if your_card1 == 11 or your_card2 == 11:
        if score > 21:
            score -= 10
    print(f"Your cards: [{your_card1},{your_card2}] , Current Score : {score}")
#computer card
    comp_card1 = random.choice(cards)
    comp_card2 = random.choice(cards)
    comp_score = comp_card1 + comp_card2
    print(f"Computer's First Card: {comp_card1}")
    hit_or_stand = input("Hit or Stand?")
# hit or stand
    if hit_or_stand.lower() == 'hit':
        your_card3 = random.choice(cards)
        score += your_card3
        print(f"Your Final cards: [{your_card1},{your_card2},{your_card3}] , Current Score : {score}")
    else:
        score += 0
        print(f"Your Final cards: [{your_card1},{your_card2}] , Current Score : {score}")
    print(f"Computer's cards: [{comp_card1}, {comp_card2}] , Current Score : {comp_score}")
    blackjack_algo()
    play = input("Do you want to play Blackjack Game? type 'y' or 'n'")