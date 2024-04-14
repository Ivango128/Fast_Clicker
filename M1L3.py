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

    def fill_new_color(self, new_color):
        pygame.draw.rect(main_window, new_color, self.rect)

    def outline(self):
        pygame.draw.rect(main_window, self.frame_color, self.rect, self.thickness)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

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

green = (43, 255, 6)
red = (255, 6, 6)
x = 20
for i in range(4):
    card = LableCard(x, 200, 100, 150, (255, 255, 255))
    card.set_text('Click')
    list_cards.append(card)
    x+=120

wait = 0
run = True
while run:
    if wait == 0:
        main_window.fill(back)
        index_card = randint(0, 3)
        for i in range(len(list_cards)):
            if index_card == i:
                list_cards[i].draw_text(25, 65)
            else:
                list_cards[i].draw()
        wait = 20

    else:
        wait -=1

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            x, y = e.pos
            for i in range(len(list_cards)):
                if list_cards[i].collidepoint(x, y):
                    if i == index_card:
                        list_cards[i].fill_new_color(green)
                    else:
                        list_cards[i].fill_new_color(red)


    clock.tick(60)
    pygame.display.update()

