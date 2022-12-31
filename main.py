############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card = random.choice(cards)

new_game=''
while True:
  user_hands = random.choices(cards, k = 2)
  computer_hand = []
  computer_hand.append(random.choice(cards))
  
  print(f'Your hand: {user_hands}\n')
  print(f'Computer\'s first card in hand: {computer_hand}\n')
  
  txt = input('Type "y" to get another card, type "n" to stand: ')
  hit_or_stand = txt.lower()
  
  if hit_or_stand == 'y':
     user_hands.append(random.choice(cards))
     computer_hand.append(random.choice(cards))
  elif hit_or_stand == 'n':
    computer_hand.append(random.choice(cards))
    
  print(f'Your final hand: {user_hands}\n') 
  print(f'Computer\'s final hand: {computer_hand}\n')
  
  if sum(user_hands) <= 21 and sum(user_hands) > sum(computer_hand):
    print("You win!")
  elif sum(computer_hand) <= 21 and sum(computer_hand) > sum(user_hands):
    print("You lose!")
  elif sum(computer_hand) == sum(user_hands) or (sum(user_hands) == 21 and sum(computer_hand) == 21):
    print("Draw!")
  new_game=input('Type "y" to play again, type "n" to end program: ')
  if new_game=='y':
    continue
  elif new_game=='n':
    break
