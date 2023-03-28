from pygame_setup import *
from collections import deque

class Card(pygame.sprite.Sprite):
    def __init__(self, number, suit):
        super().__init__()
        self.suit = suit
        self.number = number
        self.image = pygame.image.load("karte/"+str(number)+suit+".png")
        self.surf = pygame.Surface((103, 138))
    def draw(self, surface, y):
        self.y = y
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT*self.y))
        surface.blit(self.image, self.rect)
    def draw_for_touch(self, surface, y):
        self.y = y
        self.rect = self.surf.get_rect (center = (SCREEN_WIDTH*1/5, SCREEN_HEIGHT*self.y))
        surface.blit(self.image, self.rect)
    def moving (self, mouse_x, mouse_y):
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.rect = self.surf.get_rect(center=(mouse_x, mouse_y))
    def draw_in_player_pile (self, surface, y):
        self.y = y
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH*4/5,SCREEN_HEIGHT*self.y))
        surface.blit(self.image, self.rect)
    def draw_in_central_pile (self, surface):
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
        surface.blit(self.image, self.rect)

    
class Square():
    def __init__(self,x,y):
        self.height = 160
        self.width = 125
        self.x = x-self.width//2
        self.y = y-self.height//2
    def draw(self, surface):
        pygame.draw.rect(surface, rect_color, (self.x,self.y,self.width,self.height))
        
class Card_backs(pygame.sprite.Sprite):
    def __init__(self,y):
        super().__init__()
        self.y = y
        self.image = pygame.image.load("karte/Back Red 1.png")
        self.surf = pygame.Surface((103, 138))
        self.rect = (self.surf.get_rect(center=(SCREEN_WIDTH/5,SCREEN_HEIGHT*y)))
    def draw(self, surface):
        surface.blit(self.image, self.rect)
class Player(object):
    def __init__(self, ID, own_cards):
        self.ID = ID
        self.cards = own_cards
        self.rect = Rect((SCREEN_WIDTH*4/5-(70/2),SCREEN_HEIGHT*self.ID-(106/2),70,106))
        self.square_rect = Rect((SCREEN_WIDTH*1/5-(125/2),SCREEN_HEIGHT*self.ID-(160/2),125,160))
        self.pile = deque()
        self.in_hand = None
        
class Central_pile (object):
    def __init__(self):
        self.pile = deque()
        self.rect = Rect((SCREEN_WIDTH/2-(70/2),SCREEN_HEIGHT/2-(106/2),70,106))
