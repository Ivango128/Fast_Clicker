import pygame
from random import randint
import time

pygame.init()

back = (255, 229, 45)
window_w = 500
window_h = 500
main_window = pygame.display.set_mode((window_w, window_h))
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

counter = LableCard(400, 10, 100, 30, back)
counter.points = 0
counter.frame_color = back
counter.set_text(f'Счет: {counter.points}')

restart_btn = LableCard(200, 350, 120, 40, back)
restart_btn.set_text('Restart')

timer = LableCard(0, 10, 100, 30, back)
timer.seconds = 0
timer.frame_color = back
timer.set_text(f'Время: {timer.seconds}')

start_time = time.time()
curent_time = time.time()

wait = 0
run = True
isFinish = True
while run:
    next_time = time.time()
    if isFinish:
        counter.draw_text(0,0)
        timer.draw_text(0,0)
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
            if restart_btn.collidepoint(x,y):
                isFinish = True
                wait = 0
                counter.points = 0
                counter.set_text(f'Счет: {counter.points}')
            for i in range(len(list_cards)):
                if list_cards[i].collidepoint(x, y):
                    if i == index_card:
                        counter.points +=1
                        counter.set_text(f'Счет: {counter.points}')
                        list_cards[i].fill_new_color(green)
                    else:
                        list_cards[i].fill_new_color(red)

    if counter.points > 2:
        win_text = LableCard(0, 0, window_w, window_h, (3, 61, 0))
        win_text.fill_color = (205, 255, 161)
        win_text.frame_color = (205, 255, 161)
        win_text.set_text('Ты победил!')
        win_text.draw_text(window_w/2.5,window_h/2.5)
        restart_btn.draw_text(25,5)
        isFinish = False

    if next_time - curent_time > 1:
        curent_time = next_time
        timer.seconds +=1
        timer.set_text(f'Время: {timer.seconds}')

    if next_time - start_time > 5:
        lose_text = LableCard(0, 0, window_w, window_h, (3, 61, 0))
        lose_text.fill_color = (205, 255, 161)
        lose_text.frame_color = (205, 255, 161)
        lose_text.set_text('Ты проиграл!')
        lose_text.draw_text(window_w / 2.5, window_h / 2.5)
        restart_btn.draw_text(25, 5)
        isFinish = False


    clock.tick(60)
    pygame.display.update()

