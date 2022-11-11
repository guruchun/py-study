# TODO -----------------------------------------------------
# 1. Enemy 클래스 만들기
# 2. 배경음악, 효과음
# 2.1 배경음악 플레이
# 2.2 효과음: 발사
# 2.3 효과음: 격추
# 2.4 효과음: 충돌
# 3. Enemy 생성하기
# 3.1 생성하기
# 3.2 그리기
# 4. Enemy 격추 체크해서 이미지 변경
# 5. BattleShip과 Enemy 충돌 체크해서 게임 종료
# ----------------------------------------------------------

import pygame
from random import *

# global constants
pad_width = 800
pad_height = 512
ColorRed = (255, 0, 0)
ColorGreen = (0, 255, 0)


# TODO-1
# 클래스를 사용해 배경그리기 모듈화
class ScrollBackground:
    def __init__(self, file_name):
        # self.file = file_name
        self.x1 = 0
        self.y = 0
        self.m = 3
        self.image = pygame.image.load(file_name).convert_alpha()
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.x2 = self.w

    def __del__(self):
        self.image = None

    def set_pos(self, x, y):
        self.x1 = x
        self.x2 = x + self.w
        self.y = y

    def set_speed(self, speed):
        self.m = speed

    def set_size(self, width, height):
        # temp = pygame.image.load(self.file).convert_alpha()
        # self.image = pygame.transform.scale(temp, (width, height))
        self.image = pygame.transform.scale(self.image, (width, height))
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.x2 = self.x1 + self.w

    def get_size(self):
        return self.w, self.h

    def set_scale(self, scale_x, scale_y):
        # temp = pygame.image.load(self.file).convert_alpha()
        # width = int(temp.get_width()*scale_x)
        # height = int(temp.get_height()*scale_y)
        width = int(self.w * scale_x)
        height = int(self.h * scale_y)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.x2 = self.x1 + self.w
        # print(self.w, temp.get_width(), temp.get_height(), scale_x, scale_y, width, height)

    def draw(self, parent):
        self.x1 -= self.m
        self.x2 -= self.m
        if self.x1 <= self.w*(-1):
            self.x1 = self.w
        if self.x2 <= self.w*(-1):
            self.x2 = self.w
        parent.blit(self.image, (self.x1, self.y))
        parent.blit(self.image, (self.x2, self.y))
        # print(self.x1, self.x2, self.y)


# 클래스를 사용해 비행기 그리기 모듈화
# TODO create with size
class BattleShip:
    def __init__(self, file_name):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load(file_name).convert_alpha()
        self.w = self.image.get_width()
        self.h = self.image.get_height()

        # default bullet (w,h)
        temp = pygame.image.load("res/bullet.png").convert_alpha()
        self.bullet = pygame.transform.scale(temp, (30, 10))
        # (x,y) list of bullets
        self.bullets = []

        # default fire effect
        self.shoot = pygame.mixer.Sound("res/shoot.wav")
        self.shoot.set_volume(0.05)

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def get_pos_x(self):
        return self.x

    def get_pos_y(self):
        return self.y

    def set_size(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))
        self.w = self.image.get_width()
        self.h = self.image.get_height()

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()

    def set_weapon(self, w_type, size):
        temp = pygame.image.load("res/" + w_type + ".png").convert_alpha()
        self.bullet = pygame.transform.scale(temp, size)

    # def get_bullets(self):
    #     return self.bullets

    # create bullet
    def fire(self):
        # TODO-2.1 효과음: 발사
        self.shoot.play()
        x = self.x + self.w
        y = int(self.y + self.h / 2 - self.bullet.get_height() / 2)
        # or .append({'x':x, 'y':y})
        self.bullets.append([x, y])

    def check_collision(self, targets):
        # bullet shot enemy?
        hit_ok = False
        for i, bull_xy in enumerate(self.bullets):
            fx = bull_xy[0] + Bullet.Width  # right x of bullet
            fy = bull_xy[1]
            for j, enemy in enumerate(targets):
                if enemy.killed:
                    continue
                ex = enemy.get_pos_x()
                ey = enemy.get_pos_y()
                if ex < fx < ex + enemy.get_width():
                    if (ey < fy < ey + enemy.get_width()) or \
                            (ey < fy + Bullet.Height < ey + enemy.get_width()):
                        hit_ok = True
                        # hit.play()
                        self.bullets.remove(bull_xy)
                        # enemies.remove(jtem)
                        # fired_enemies.append([fx, fy, 30])
                        enemy.kill()
                        break
        # TODO
        # ship collide with enemy?

        return hit_ok

    def draw(self, parent, move_y):
        # draw ship
        self.y += move_y
        if self.y < 0:
            self.y = 0
        # pad_height = parent.get_height()
        if self.y > (pad_height - self.h):
            self.y = pad_height - self.h
        parent.blit(self.image, (self.x, self.y))

        # draw bullets: list of [x, y]
        if len(self.bullets) > 0:
            for i, xy in enumerate(self.bullets):
                parent.blit(self.bullet, xy)
                xy[0] += 5
                if xy[0] > pad_width:
                    self.bullets.remove(xy)


# 클래스를 사용해 Enemy 그리기 모듈화
class Enemy:
    # shapes
    Shapes = ["enemy", "enemy1", "enemy2", "enemy3"]
    # key=shape, value=image
    ShapeImages = {}
    # fired image list for animation
    FiredImages = []
    FiredImageNext = 0

    # for resizing images
    Size = (0, 0)

    def __init__(self, shape):
        # class 초기화
        if len(Enemy.ShapeImages) == 0:
            Enemy.initialize()

        # TODO-
        self.shape = shape
        # if shape in Enemy.ShapeImages:
        self.w = Enemy.ShapeImages[shape].get_width()
        self.h = Enemy.ShapeImages[shape].get_height()
        self.x = pad_width
        self.y = randint(0, pad_height-self.h)
        self.speed = randint(1, 4)

        # for display the fired status
        self.killed = False
        self.killed_image = 0
        self.killed_timer = 0

    def get_pos_x(self):
        return self.x

    def get_pos_y(self):
        return self.y

    def get_width(self):
        return self.w

    def kill(self):
        self.killed_image = Enemy.FiredImageNext
        self.killed = True
        Enemy.FiredImageNext = (Enemy.FiredImageNext+1) % len(Enemy.FiredImages)

    def killed_timeout(self):
        if self.killed_timer > 60:
            return True
        else:
            return False

    def draw(self, parent):
        self.x -= self.speed
        move_y = randint(-5, 5)
        if abs(move_y) < 3:
            self.y += move_y
        if self.y < 0:
            self.y = 0
        # pad_height = parent.get_height()
        if self.y > (pad_height - self.h):
            self.y = pad_height - self.h

        if self.killed:
            self.killed_timer += 1
            parent.blit(Enemy.FiredImages[self.killed_image], (self.x, self.y))
        else:
            parent.blit(Enemy.ShapeImages[self.shape], (self.x, self.y))

    @classmethod
    def initialize(cls):
        w, h = cls.Size
        # shape images
        for shape in cls.Shapes:
            file_name = "res/" + shape + ".png"
            img = pygame.image.load(file_name).convert_alpha()
            if w > 0 and h > 0:
                img = pygame.transform.scale(img, (w, h))
            cls.ShapeImages[shape] = img

        # explosion image
        # TODO animated images
        img = pygame.image.load("res/explosion.png").convert_alpha()
        if w > 0 and h > 0:
            img = pygame.transform.scale(img, (w, h))
        cls.FiredImages.append(img)

        # explosion --> text character
#        fg = 200, 50, 50
#        bg = 5, 5, 5
#        text = "가장 유능한 사람은 언제나 배움에 힘쓰는 사람이다. 괴테"
#        font = pygame.font.SysFont("Malgun Gothic", 40, bold=True)
#        for s in text:
#            bg_img = pygame.Surface([50, 50])
#            bg_img.fill(bg)
#            pygame.draw.circle(bg_img, (255, 250, 50), (25,25), 25)
#            t = font.render(s, True, fg, bg)
#            t.set_colorkey(bg)
#            bg_img.set_colorkey(bg)
#            bg_img.blit(t, (5, 0))
#            # cls.FiredImages.append(t)
#            cls.FiredImages.append(bg_img)

    @classmethod
    def set_all_size(cls, size):
        cls.Size = size
        # TODO resize all images


# TODO-4
def check_crash():
    # fx = x
    # fy = y
    # for j, jtem in enumerate(enemyList):
    #     ex = jtem[0]
    #     ey = jtem[1]
    #     if fx > ex and fx < ex + enemy_size:
    #         if (fy > ey and fy < ey + enemy_size) or (fy + f_height > ey and fy + f_height < ey + enemy_size):
    #             # print ("hit", fx, fy, ex, ey)
    #             crashed = True
    #             crash.play()
    #             enemyList.remove(jtem)
    #             shotList.append([fx, fy, 30])
    #             pygame.mixer.music.pause()
    #             break;
    return False


# TODO-
class Bullet:
    Image = None
    Width = 0
    Height = 0

    def __init__(self):
        # TODO-
        temp = pygame.image.load("res/bullet.png").convert_alpha()
        Bullet.Image = pygame.transform.scale(temp, (40, 30))
        Bullet.Width = Bullet.Image.get_width()
        Bullet.Height = Bullet.Image.get_height()


def create_background():
    bg_image1 = ScrollBackground("res/city_background_night_gray.png")
    w, h = bg_image1.get_size()
    stretch_ratio = pad_height/h
    bg_image1.set_scale(stretch_ratio, stretch_ratio)
    bg_image1.set_speed(1)

    bg_image2 = ScrollBackground("res/city_background_clean.png")
    stretch_ratio *= 0.6
    bg_image2.set_scale(stretch_ratio, stretch_ratio)
    bg_image2.set_speed(3)
    bg_image2.set_pos(0, int(pad_height-(pad_height*0.6)))
    return [bg_image1, bg_image2]


def create_battle_ship():
    bs = BattleShip("res/ship.png")
    bs.set_size(50, 40)
    bs.set_pos(30, pad_height/2-bs.get_height()/2)
    bs.set_weapon("bullet", (40, 10))
    return bs


# def create_popup_text(text):
#     char_list = []
#     fg = 100, 200, 50
#     bg = 5, 5, 5
#     font = pygame.font.SysFont("Malgun Gothic", 40)
#     for s in text:
#         print(s)
#         t = font.render(s, True, fg, bg)
#         t.set_colorkey(bg)
#         char_list.append(t)
#     return char_list


def main():
    global ship, enemies

    # initialize pygame window
    pygame.init()
    game_pad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption("My PyGame")

    # create scrolling background
    scrolls = create_background()
    # create battle-ship
    ship = create_battle_ship()

    # TODO-2
    # create background music & sound effect
    pygame.mixer.init()
    hit = pygame.mixer.Sound("res/hit.wav")
    crash = pygame.mixer.Sound("res/boom.wav")
    hit.set_volume(0.3)
    crash.set_volume(0.3)
    pygame.mixer.music.load('res/bgm_BossMain.wav')
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.25)

    # get pygame clock
    clock = pygame.time.Clock()

    # drawing values
    s_move_y = 0

    # drawing objects
    enemies = []

    # play values
    enemy_time = 0
    play_score = 0
    energy_bar = 100

    # game main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    s_move_y = -5
                elif event.key == pygame.K_DOWN:
                    s_move_y = 5
                elif event.key == pygame.K_SPACE:
                    ship.fire()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    s_move_y = 0

        # TODO-3
        # create enemy
        play_level = 1 + int(play_score / 20)
        enemy_time_max = 40 - play_level
        enemy_time = (enemy_time + 1) % enemy_time_max
        if enemy_time == 0:
            index = randint(0, 3)
            enemies.append(Enemy(Enemy.Shapes[index]))

        # TODO-4
        crashed = check_crash()
        if crashed:
            # draw crash status
            # change ship image
            continue

        # TODO-5
        ship.check_collision(enemies)

        # TODO-
        # remove destroyed enemies
        for i, enemy in enumerate(enemies):
            if enemy.killed_timeout():
                enemies.remove(enemy)

        # draw background color
        # game_pad.fill(BgColor)

        # draw scrolling background
        for bg in scrolls:
            bg.draw(game_pad)

        # draw battle ship
        ship.draw(game_pad, s_move_y)

        # TODO-3.2
        # draw enemies
        if len(enemies) > 0:
            for i, e in enumerate(enemies):
                e.draw(game_pad)
                if e.get_pos_x() < e.get_width()*(-1):
                    enemies.remove(e)
                    energy_bar -= 1

        # TODO-
        # draw energy bar

        # update display
        pygame.display.update()
        clock.tick(60)

    pygame.quit()


# python 파일을 실행할때만 main()을 호출한다.
if __name__ == "__main__":
    main()
