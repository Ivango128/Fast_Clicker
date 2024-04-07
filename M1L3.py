import pygame
from random import randint
import time

pygame.init()

back = (255, 229, 45)
main_window = pygame.display.set_mode((500, 500))
main_window.fill(back)

clock = pygame.time.Clock()


class RectCard():
    def __init__(self, x=0, y=0, width=10, height=10, color=back, frame_color=(0,0,0), thickness=2):
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.x = x
        self.rect.y = y
        self.fill_color = color
        self.frame_color = frame_color
        self.thickness = thickness

    def fill(self):
        pygame.draw.rect(main_window, self.fill_color, self.rect)

    def outline(self):
        pygame.draw.rect(main_window, self.frame_color, self.rect, self.thickness)

class LableCard(RectCard):
    def set_text(self, text):
        self.lable = pygame.font.SysFont('Arial', 28).render(text, True, (0,0,0))

    def draw_text(self, shift_x, shift_y):
        self.fill()
        self.outline()
        main_window.blit(self.lable, (self.rect.x + shift_x, self.rect.y + shift_y))

    def draw(self):
        self.fill()
        self.outline()

list_cards = list()

x = 20
for i in range(4):
    card = LableCard(x, 200, 100, 150, (255, 255, 255))
    card.set_text('Click')
    list_cards.append(card)
    x+=120

wait = 20
while True:
    index_card = randint(0, 3)
    main_window.fill(back)
    for i in range(len(list_cards)):
        if index_card == i and wait !=0:
            list_cards[i].draw_text(25, 65)
        else:
            list_cards[i].draw()

    wait -=1
    clock.tick(60)
    pygame.display.update()

