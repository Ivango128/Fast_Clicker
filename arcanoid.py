import pygame

pygame.init()

back = (0, 193, 190)
window_w = 500
window_h = 500
main_window = pygame.display.set_mode((window_w, window_h))
main_window.fill(back)

clock = pygame.time.Clock()


class RectCard():
    def __init__(self, x=0, y=0, width=10, height=10, color=back, frame_color=(0, 0, 0), thickness=2):
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
        self.lable = pygame.font.SysFont('Arial', 28).render(text, True, (0, 0, 0))

    def draw_text(self, shift_x, shift_y):
        self.fill()
        self.outline()
        main_window.blit(self.lable, (self.rect.x + shift_x, self.rect.y + shift_y))

    def draw(self):
        self.fill()
        self.outline()


class SpriteImg(RectCard):
    def __init__(self, x, y, width, height, puth_img, color=back, frame_color=(0, 0, 0), thickness=0):
        super().__init__(x, y, width, height, color, frame_color, thickness)
        self.image = pygame.image.load(puth_img)

    def draw_img(self):
        main_window.blit(self.image, (self.rect.x, self.rect.y))


# размер монстра 50х50
# 50*9 = 450 9 монстров
# 500 - 450 = 50 общее растояние между монстрами
# 50 // (9-1) = 6 остаток 2
# от левого отсупить 1

width_monstr = 50
height_monstr = 50
count_monsters = 9

rast_monstr = width_monstr + ((window_w - (count_monsters * width_monstr)) // (count_monsters - 1))
y = 1

row = 3

monsters = []

for i in range(row):
    x = (window_w - (count_monsters * width_monstr)) % (count_monsters - 1) // 2 + width_monstr * i // 2
    for j in range(count_monsters):
        monster = SpriteImg(x, y, width_monstr, height_monstr, 'enemy.png')
        monsters.append(monster)
        x += rast_monstr
    y += height_monstr + 1
    count_monsters -= 1

ball = SpriteImg(200, 300, 50, 50, 'ball.png')
platform = SpriteImg(200, 400, 100, 25, 'platform.png')


run = True
while run:
    for monster in monsters:
        monster.draw_img()
    ball.draw_img()
    platform.draw_img()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    clock.tick(60)
    pygame.display.update()