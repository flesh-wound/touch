from instances_and_variables import *
#this function calculates the correct move according to the game rules
def correct_move(active_p, inactive_p):
    if not active_p.in_hand:
        if not active_p.pile:
            return "new_card"
        elif ck.pile and active_p.pile and (active_p.pile[-1].number - ck.pile[-1].number == 1 or active_p.pile[-1].number - ck.pile[-1].number == -12):
            return "central_pile"
        elif active_p.pile and inactive_p.pile and active_p.pile[-1].number - inactive_p.pile[-1].number in {1, -12}:
            return "opponent_pile"
        else:
            return "new_card"
    else:
        if not ck.pile and active_p.in_hand.number == 1:
            return "central_pile"
        if ck.pile and active_p.in_hand.number - ck.pile[-1].number in {1, -12}:
            return "central_pile"
        elif inactive_p.pile and active_p.in_hand.number - inactive_p.pile[-1].number in {1, -12}:
            return "opponent_pile"
        else:
            return "own_pile"
#check wether the played move is the correct one and return the card to be added to the active player's pile
#if he played the wrong move
def played_move (mov, active_p, inactive_p):
    if mov != correct_move (active_p, inactive_p):
        if inactive_p.pile:
            return inactive_p.pile[-1] 
        elif inactive_p.cards:
            return inactive_p.cards[-1]
        else:
            return False
    #confirm that the move is correct in order to continue the move:
    else:
        return False
        
def info_turn(active_p, p_1):
    return fontfont.render("player one's turn" if active_p == p_1 else "player two's turn", False, (0, 0, 0))



def change_turn(active_p, p_1, p_2):
    return p_2 if active_p == p_1 else p_1, p_2 if active_p == p_2 else p_1

#draw as in draw from a deck
def draw_card(active_p, p_1):
    active_p.in_hand = active_p.cards[0]
    active_p.in_hand.draw(screen, active_p.ID)
    sprites_group.add (active_p.in_hand)
    #if the deck is spent, signal it by removing the sprite of the card back
    if len(active_p.cards) == 1:
        sprites_group.remove (back1 if active_p == p_1 else back2)
        
#put the active card to the player pile
def add_to_pile1 (active_p, whos_pile):
    whos_pile.pile.append(active_p.in_hand) 
    sprites_group.remove (active_p.in_hand)
    #if it is the drawn card, put it from the deck to the pile
    if active_p.cards and active_p.in_hand == active_p.cards[0]:
        active_p.cards.popleft()
    active_p.in_hand = None
#the function for punishing the player for the wrong move:
def touch_punish (inactive_p, touch_m, p_1):
    #move from discard pile top else from active cards bottom
    if inactive_p.pile:
        inactive_p.pile.pop()
        return 0
    else:
        touch_m.draw_for_touch(screen, inactive_p.ID)
        inactive_p.cards.pop()
        if not inactive_p.cards:
            sprites_group.remove (back1 if inactive_p == p_1 else back2)
        return 6
#instantiate players and deal cards
def deal_cards (dck):
    random.shuffle (dck)
    return Player((1/5), deque(dck[:26])), Player((4/5), deque(dck[26:]))
#function for blitting the rules; this was copied from stackoverflow
def blit_rules (surface, text, pos, font, color=pygame.Color('grey')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
def welcome_screen():
    welcome = True
    while welcome:
        screen.fill(background)
        blit_rules (screen, rules, (20,20), rules_font)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if (event.type == pygame.KEYDOWN) or (event.type == pygame.MOUSEBUTTONUP):
                welcome = False
        pygame.display.update()
        FramePerSec.tick(FPS)