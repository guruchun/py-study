# TODO -----------------------------------------------------
# 1. 클래스를 사용해 모듈화하기
#    a. 폭파시킬 적 Enemy 클래스 만들기
# 2. 랜덤 위치에서 Enemy 생성하기
# 3. up/down 키 처리
# 4. 비행기 움직이기: up/down 키로 이동, 누른 상태는 up/down 계속
#    a. 비행기 좌표 계산
#    b. 비행기 그리기
# ----------------------------------------------------------

import pygame
from random import *

# global constants
pad_width = 800
pad_height = 512
ColorRed = (255, 0, 0)
ColorGreen = (0, 255, 0)


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

        # default bullet
        self.bullet = pygame.image.load("res/bullet.png")
        self.bh = self.bullet.get_height()

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

    # TODO change_weapon(w_type), add_weapon(w_type, weapon_file)
    def set_weapon(self, file_name):
        self.bullet = pygame.image.load(file_name)
        self.bh = self.bullet.get_height()

    def fire(self):
        self.shoot.play()
        return [self.x + self.w,
                int(self.y + self.h/2 - self.bh/2)]

    def draw(self, parent, move_y):
        self.y += move_y
        if self.y < 0:
            self.y = 0
        # pad_height = parent.get_height()
        if self.y > (pad_height - self.h):
            self.y = pad_height - self.h
        parent.blit(self.image, (self.x, self.y))


# 클래스를 사용해 Enemy 그리기 모듈화
class Enemy:
    EnemyTypes = ["enemy", "enemy1", "enemy2", "enemy3"]
    EnemyImages = []

    def __init__(self, enemy_type):
        # TODO-
        # if same image object, memory is wasting...
        file_name = "res/" + enemy_type + ".png"
        temp = pygame.image.load(file_name).convert_alpha()
        self.image = pygame.transform.scale(temp, (40, 30))
        self.h = self.image.get_height()
        self.w = self.image.get_width()
        self.x = pad_width
        self.y = randint(0, pad_height-self.h)
        self.speed = randint(1, 5)

        self.fired = False
        temp = pygame.image.load("res/explosion.png").convert_alpha()
        self.fired_image = pygame.transform.scale(temp, (40, 30))

    def get_pos_x(self):
        return self.x

    def get_width(self):
        return self.w

    def set_fired(self):
        self.fired = True

    def draw(self, parent):
        self.x -= self.speed
        self.y += randint(-5, 5)
        if self.y < 0:
            self.y = 0
        # pad_height = parent.get_height()
        if self.y > (pad_height - self.h):
            self.y = pad_height - self.h
        parent.blit(self.image, (self.x, self.y))


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


def check_hit():
    # for i, item in enumerate(fireList):
    #     fx = item[0] + bullet_w  # right x of bullet
    #     fy = item[1]
    #     for j, jtem in enumerate(enemyList):
    #         ex = jtem[0]
    #         ey = jtem[1]
    #         if fx > ex and fx < ex + enemy_size:
    #             if (fy > ey and fy < ey + enemy_size) or (fy + bullet_h > ey and fy + bullet_h < ey + enemy_size):
    #                 # print ("hit", fx, fy, ex, ey)
    #                 if len(answerList) > 20 and answerList.count(jtem[2]) > 0:
    #                     answerList.remove(jtem[2])
    #                 else:
    #                     answerList.append(jtem[2])
    #                 hit.play()
    #                 fireList.remove(item)
    #                 enemyList.remove(jtem)
    #                 shotList.append([fx, fy, 30])
    #                 break;
    pass


def main():

    # initialize pygame window
    pygame.init()
    game_pad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption("My PyGame")

    # create ScrollBackground
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

    # create Battleship
    ship = BattleShip("res/ship.png")
    ship.set_size(50, 30)
    ship.set_pos(30, pad_height/2-ship.get_height()/2)
    # create bullet image
    bullet = pygame.image.load("res/bullet.png").convert_alpha()
    bullet = pygame.transform.scale(bullet, (30, 10))

    # TODO-
    # create Enemy

    # TODO-
    # create background music & sound effect
    pygame.mixer.init()
    hit = pygame.mixer.Sound("res/hit.wav")
    crash = pygame.mixer.Sound("res/boom.wav")
    hit.set_volume(0.2)
    crash.set_volume(0.2)
    pygame.mixer.music.load('res/bgm_BossMain.wav')
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.25)

    # get pygame clock
    clock = pygame.time.Clock()

    # drawing values
    s_move_y = 0
    enemy_time = 0

    # drawing objects
    bullets = []
    enemies = []

    # play values
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
                    bullets.append(ship.fire())

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    s_move_y = 0

        # TODO-
        # create enemy
        play_level = 1 + int(play_score / 20)
        enemy_time_max = 20 - play_level
        enemy_time = (enemy_time + 1) % enemy_time_max
        if enemy_time == 0:
            enemies.append(Enemy(enemy_types[0]))

        # TODO-
        crashed = check_crash()
        if crashed:
            # draw crash status
            # change ship image
            continue

        check_hit()

        # draw background color
        # game_pad.fill(BgColor)

        # draw scrolling background
        bg_image1.draw(game_pad)
        bg_image2.draw(game_pad)

        # draw battle ship
        ship.draw(game_pad, s_move_y)

        # draw bullets: list of [x, y]
        if len(bullets) > 0:
            for i, xy in enumerate(bullets):
                game_pad.blit(bullet, xy)
                xy[0] += 5
                if xy[0] > pad_width:
                    bullets.remove(xy)

        # TODO-
        # draw enemies
        if len(enemies) > 0:
            for i, e in enumerate(enemies):
                e.draw(game_pad)
                if e.get_pos_x() < e.get_width()*(-1):
                    enemies.remove(e)
                    energy_bar -= 1

        # TODO-
        # draw shot enemies

        # TODO-
        # draw energy bar

        # update display
        pygame.display.update()
        clock.tick(60)

    pygame.quit()


# python 파일을 실행할때만 main()을 호출한다.
if __name__ == "__main__":
    main()
