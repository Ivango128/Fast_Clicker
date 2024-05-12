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
        pygame.draw.rect(main_window, self.fill_color, self.rect, border_radius=40)

    def fill_new_color(self, new_color):
        pygame.draw.rect(main_window, new_color, self.rect, border_radius=40)

    def outline(self):
        pygame.draw.rect(main_window, self.frame_color, self.rect, self.thickness, border_radius=40)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

class LableCard(RectCard):
    def set_text(self, text):
        self.lable = pygame.font.SysFont('Arial', 22).render(text, True, (0,0,0))

    def draw_text(self, shift_x, shift_y):
        self.fill()
        self.outline()
        main_window.blit(self.lable, (self.rect.x + shift_x, self.rect.y + shift_y))

    def draw(self):
        self.fill()
        self.outline()

list_questhoins = ['Кто?', 'Хочет?', 'Стать?']
list_answers= [['A: one', 'B: two', 'C: three', 'B: four'],['A: one1', 'B: two1', 'C: three1', 'B: four1'], ['A: one2', 'B: two2', 'C: three2', 'B: four2']]
list_right_answers = [1, 2, 2]

list_cards = list()

green = (43, 255, 6)
red = (255, 6, 6)
x = 20
for i in range(4):
    card = LableCard(x, 400, 110, 75, (255, 255, 255))
    card.set_text('Click')
    list_cards.append(card)
    x+=115

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

curent_question = 0

run = True
isFinish = True
while run:
    next_time = time.time()
    if isFinish:
        main_window.fill(back)
        counter.draw_text(0, 0)
        timer.draw_text(0, 0)

        for i in range(len(list_answers[curent_question])):
            list_cards[i].set_text(list_answers[curent_question][i])
            list_cards[i].draw_text(25, 26)


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
            for i in range(len(list_answers[curent_question])):
                if list_cards[i].collidepoint(x, y):
                    if i == list_right_answers[curent_question]:
                        counter.points +=1
                        counter.set_text(f'Счет: {counter.points}')
                        list_cards[i].fill_new_color(green)
                        curent_question+=1
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

