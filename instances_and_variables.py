from classes import *
import random
ck = Central_pile()
suits = ["h", "t", "k", "p"]
deck = [Card(number, suit) for number in range(1, 14) for suit in suits]
#positions of playing squares
rect_position = [(SCREEN_WIDTH/5,SCREEN_HEIGHT/5), (SCREEN_WIDTH*4/5,SCREEN_HEIGHT/5), (SCREEN_WIDTH/2,SCREEN_HEIGHT/2),
                (SCREEN_WIDTH/5,SCREEN_HEIGHT*4/5), (SCREEN_WIDTH*4/5,SCREEN_HEIGHT*4/5)]

rules = ("Hello and welcome to TOUCH!, a centuries-old children's card game with simple rules.\n"
         "Each player starts with half a standard deck.\n"
         "If the active player has cards in his discard pile, he must first check if he can place the top card to the "
         "central pile or the other player's discard pile. If he can't, only then is he allowed to draw a card. "
         "After drawing a new card, he goes through the same check.\n"
         "The central pile has priority over the other player's pile.\n"
         "Cards are placed in ascending order. Ace starts the central pile and otherwise goes on the King. The suits do not matter.\n"
         "If the player makes a mistake, the other player must shout \"TOUCH!\" and give the former the top card from "
         "his discard pile, or, if there's no discard pile, the bottom card from his deck. This is done automatically "
         "for your convenience.\n"
         "Remember these rules as you'll never see them again! Good luck!\n"
         "PRESS ANY KEY TO CONTINUE")
back1 = Card_backs(1/5)
back2 = Card_backs(4/5)
sprites_group=pygame.sprite.Group()
sprites_group.add(back1,back2)
