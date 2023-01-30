from sys import exit

import pygame as pg


# HEALTH BAR.
class StaticHealthBar:

    def __init__(self):
        # CORE.
        BAR_WIDTH, BAR_HEIGHT = 400, 25
        self.MAX_HEALTH, self.cur_health = 1000, 500
        self.RATIO = BAR_WIDTH / self.MAX_HEALTH
        # RECT.
        self.rect = pg.Rect(25, 25, 0, BAR_HEIGHT)
        self.frame_rect = pg.Rect(25, 25, BAR_WIDTH, BAR_HEIGHT)

    def update(self, quantity: int):
        self.cur_health += quantity
        if self.cur_health < 0:
            self.cur_health = 0
        elif self.cur_health > self.MAX_HEALTH:
            self.cur_health = self.MAX_HEALTH

    def ratio(self, value: int):
        return int(value * self.RATIO)

    def draw(self):
        # UPDATE INFORMATION.
        self.rect.width = self.ratio(self.cur_health)
        # DRAW.
        pg.draw.rect(screen, '#FF0000', self.rect)
        pg.draw.rect(screen, '#FFFFFF', self.frame_rect, 3)


class AnimatingHealthBar:

    def __init__(self):
        # CORE.
        BAR_WIDTH, BAR_HEIGHT = 400, 25
        self.MAX_HEALTH, self.cur_health = 1000, 0
        self.RATIO = BAR_WIDTH / self.MAX_HEALTH
        # RECT
        self.rect = pg.Rect(25, 75, 0, BAR_HEIGHT)
        self.frame_rect = pg.Rect(25, 75, BAR_WIDTH, BAR_HEIGHT)
        # ANIMATION.
        self.aim_health, self.SPEED = 500, 5
        self.gap_rect = pg.Rect(0, 75, 0, BAR_HEIGHT)

    def update(self, quantity: int):
        self.aim_health += quantity
        if self.aim_health < 0:
            self.aim_health = 0
        if self.aim_health > self.MAX_HEALTH:
            self.aim_health = self.MAX_HEALTH

    def ratio(self, value: int):
        return int(value * self.RATIO)

    def draw(self):
        # GAP INFORMATION.
        gap_color = '#FF0000'
        # GET HEALTH | DAMAGE.
        if self.cur_health < self.aim_health:
            self.cur_health += self.SPEED
            gap_color = '#00FF00'
        elif self.cur_health > self.aim_health:
            self.cur_health -= self.SPEED
            gap_color = '#FFFF00'
        # UPDATE INFORMATION.
        self.rect.width = self.ratio(self.cur_health)
        gap_width = self.ratio(self.aim_health - self.cur_health)
        self.gap_rect.x = self.rect.right + (0 if gap_width > 0 else gap_width)
        self.gap_rect.width = abs(gap_width)
        # DRAW.
        pg.draw.rect(screen, '#FF0000', self.rect)
        pg.draw.rect(screen, gap_color, self.gap_rect)
        pg.draw.rect(screen, '#FFFFFF', self.frame_rect, 3)


# DISPLAY.
pg.init()
screen = pg.display.set_mode((450, 125))
pg.display.set_caption('Health Bar Simulation')
pg.display.set_icon(pg.image.load('image/HEART.png').convert_alpha())
# SYSTEM.
clock = pg.time.Clock()

# ENTITY.
player_1 = StaticHealthBar()
player_2 = AnimatingHealthBar()

# MAIN.
while True:
    # EVENT.
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                player_1.update(200)
                player_2.update(200)
            if event.key == pg.K_DOWN:
                player_1.update(-200)
                player_2.update(-200)
    # UPDATE & DRAW.
    screen.fill('#000000')
    player_1.draw()
    player_2.draw()
    # SYSTEM.
    pg.display.update()
    clock.tick(60)
