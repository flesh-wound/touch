import copy
from functions import *
def main():
    game_over = False
    #is the player moving a card around?
    moving = False
    #variable that will contain the card to be given to the active player in case he plays a wrong move;
    #otherwise it is set as False; when containing a card, it will trigger an animation loop and disable any moves
    #until the animation finishes
    touch_moving = False
    p1,p2 = deal_cards (deck)
    active_player = random.choice([p1,p2])
    inactive_player = p1 if active_player == p2 else p2
    while not game_over:
        if (not active_player.cards and not active_player.pile) or (not inactive_player.cards and not inactive_player.pile):
            
            if not touch_moving and not moving:
                game_over = True
        screen.fill(background)
        if not game_over and not touch_moving:
            screen.blit(info_turn(active_player, p1),(0,0) if active_player == p1 else (0,750))
        #draw squares for placing the cards
        for pos in rect_position:
            Square(*pos).draw(screen)
    #ovo može ili kao funkcija ili u grupu
        if active_player.pile:
            active_player.pile[-1].draw_in_player_pile (screen, active_player.ID)
        if inactive_player.pile:
            inactive_player.pile[-1].draw_in_player_pile (screen, inactive_player.ID)
        if ck.pile:
            ck.pile[-1].draw_in_central_pile (screen)
        
        if touch_moving:
            touch_text = touch_font.render("TOUCH!", False, (0, 0, 0))
            screen.blit((touch_text),(SCREEN_WIDTH/2 - touch_text.get_rect().width/2, 2))
            #disable the play during the animation of being given a card
            pygame.event.set_blocked(None)
            if touch_moving not in sprites_group:
                sprites_group.add (touch_moving)
                where_from = touch_punish (inactive_player, touch_moving, p1)
            touch_moving.rect.move_ip (where_from, 6 if inactive_player == p1 else -6)
            
            if active_player.rect.colliderect(touch_moving):
                sprites_group.remove(touch_moving)
                active_player.pile.append (touch_moving)
                touch_moving = False
                pygame.event.set_allowed(None)
                
        sprites_group.draw(screen)
        
        if active_player.cards and active_player.in_hand == active_player.cards[0] and not moving:
            active_player.in_hand.draw(screen, active_player.ID)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if active_player.in_hand and active_player.in_hand.rect.collidepoint(event.pos):
                    moving = True
                #moving the card from the top of the active player's pile
                elif not active_player.in_hand and active_player.pile and active_player.pile[-1].rect.collidepoint(event.pos):
                    moving = True
                    #add the top card from the player pile to the hand
                    active_player.in_hand = active_player.pile[-1]
                    sprites_group.add (active_player.in_hand)
                    active_player.pile.pop()
            if event.type == pygame.MOUSEBUTTONUP and not moving:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in sprites_group if s.rect.collidepoint(pos)]
                #drawing a card if the hand is empty
                if back1 in clicked_sprites and active_player == p1 or back2 in clicked_sprites and active_player == p2:
                    #do not punish the player for trying to draw another card as this is generally something that
                    #should not happen during a real card game
                    if not active_player.in_hand:
                        touch_moving = played_move ("new_card", active_player, inactive_player)
                        if not touch_moving:
                            draw_card(active_player, p1)
                #if the deck is spent, turn the discard pile over into the new deck
                if not active_player.cards and active_player.square_rect.collidepoint(pos):
                    active_player.cards = copy.copy(active_player.pile)
                    active_player.pile.clear()
                    sprites_group.add (back1 if active_player == p1 else back2)
            if event.type == pygame.MOUSEBUTTONUP and moving:
                #if the player has drawn a card
                if active_player.rect.colliderect(active_player.in_hand):
                    touch_moving = played_move ("own_pile", active_player, inactive_player)
                    if active_player.cards and active_player.cards[0] == active_player.in_hand and not touch_moving:
                        add_to_pile1 (active_player, active_player)
                        active_player, inactive_player = change_turn(active_player, p1, p2)
                #adding cards to the central pile:
                elif ck.rect.colliderect(active_player.in_hand):
                    touch_moving = played_move ("central_pile", active_player, inactive_player)
                    if not touch_moving:
                        add_to_pile1 (active_player, ck)
                elif inactive_player.rect.colliderect(active_player.in_hand):
                    touch_moving = played_move ("opponent_pile", active_player, inactive_player)
                    if not touch_moving:
                        add_to_pile1 (active_player, inactive_player)
                #if the player doesn't play anything with the card from his pile, return it to the pile;
                #this way the player can change his mind in case he sees that he's about to play the wrong move;
                #other way of solving this would punish the player immediately after picking up the card from his own pile
                #not necessarily with the following line tho
                if active_player.in_hand and active_player.cards and active_player.in_hand != active_player.cards[0] or active_player.in_hand and not active_player.cards:
                    add_to_pile1 (active_player, active_player)
                moving = False
 
            if event.type == pygame.MOUSEMOTION and moving:
                if active_player.in_hand:
                    active_player.in_hand.moving(*event.pos)
                elif active_player.pile_in_hand:
                    active_player.pile_in_hand.moving(*event.pos)

        pygame.display.update()
        FramePerSec.tick(FPS)
    return "p1" if not p1.cards and not p1.pile else "p2"
def post_game(res):
    while True:
        winner = fontfont.render("PLAYER ONE WINS" if res == "p1" else "PLAYER TWO WINS", False, (0, 0, 0))
        screen.blit(winner, (1,1))
        screen.blit (fontfont.render ("PRESS ANY KEY TO PLAY AGAIN", False, (0, 0, 0)), (1, 28))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame.KEYDOWN) or (event.type == pygame.MOUSEBUTTONUP):
                sprites_group.empty()
                ck.pile.clear()
                sprites_group.add(back1,back2)
                reslt = main()
                post_game (reslt)
                
                
        pygame.display.update()
        FramePerSec.tick(FPS)