#Rules----------------------------
'''The deck is unlimited in size.
 There are no jokers.
 The Jack/Queen/King all count as 10.
 The  Ace can count as 11 or 1.
 Use the following list as the deck of cards:
 cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
 The cards in the list have equal probability of being drawn.
 Cards are not removed from the deck as they are drawn.
 The computer is the dealer.'''
#-------------------------------------------
from art import logo
import random

# def computer(computer_card):
#     val=0
#     for i in computer_card:
#         val += i
#     if val >= 21:
#        return print(f"You Win!\nComputer card:{computer_card},final score:{val}")
#     if len(computer_card)>=3:
#         list_flag[len(list_flag)-1]
#         if list_flag[len(list_flag)-1]> val:
#             return print(f"You win\nComputer card:{computer_card}final score:{val}")
#         elif list_flag[len(list_flag)-1]< val:
#             return print(f"You lose\nComputer card:{computer_card}final score:{val}")
#         else:
#             return print(f"Draw\nComputer card:{computer_card}final score:{val}")
#     print(flag,val)
#     return print(f"You Lose\nComputer card:{computer_card.append(random.choice(cards))}final score:{val}")
#
# condition='y'
# your_card =[random.choice(cards),random.choice(cards)]
# computer_card=[random.choice(cards)]
# print(f"Computer first card:{computer_card}")
# flag=0
# list_flag=[]
# while condition=='y':
#     for i in your_card:
#         flag += i
#     list_flag.append((str(flag)))
#     print(list_flag)
#     if len(your_card)>3:
#         computer(computer_card)
#         break
#     if flag>=21:
#         print("You lose")
#         print(f"Your cards:{your_card},current score:{flag}")
#         break
#     else:
#         print(f"Your cards:{your_card},current score:{flag}")
#     your_card.append(random.choice(cards))
#     condition = input("Type 'y' to get another card, type 'n' to pass:").lower()
#     computer_card.append(random.choice(cards))
# if condition == 'n':
#     computer(computer_card)
#---------------------------------------------------------------------------------------------------
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    #By using comma to return values it returns as "TUPLE" which is immutable in nature
    card = random.choice(cards)
    return card

def calculate_score(temp_cards):
    if sum(temp_cards) == 21 and len(temp_cards) == 2:
        return 2
    if 11 in temp_cards and sum(temp_cards) > 21:
        temp_cards.remove(11)
        temp_cards.append(1)
    return sum(temp_cards)

def compare(user_score,computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over.You lose"
    if user_score == computer_score:
        return "Draw"
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 2:
        return "Lose, opponent has Blackjack"
    elif user_score == 2:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    print(logo)
    print("-------------------------------------------------------------------")
    user_cards = []
    computer_cards = []
    game_over = False
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    # print(f"Your cards:{user_cards}\nComputer cards:{computer_cards}")
    #  calculate_score(user_cards,computer_cards)
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 2 or computer_score == 2 or user_score > 21:
            game_over = True
        else:
            user_wants_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_wants_card == "y":
               user_cards.append(deal_card())
            else:
                game_over=True
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower() == "y":
    play_game()

