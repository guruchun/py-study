# ----------------------------------------------------------
# 완료
# - 배경 움직이기
#   . 배경 이미지 그리기
#   . 2장을 겹치고 움직이는 속도를 다르게해서 원근효과 주기
#   . 각 이미지를 이어붙여서 끊김없이 스크롤하기
# - 전투기 띄우기
#   . 전투기 움직이기, 키보드 방향키 사용
#   . 방향키 누른 상태이면 계속 이동
#   . 동시에 누르면 대각선으로 이동
# - 전투기에서 총쏘기
#   . 총알 보이기
#   . 총알 움직이기
# - 배경음악, 효과음
#   . 배경음악: 무한 반복
#   . 효과음: 발사, 격추, 충돌
# - 적기 출현
#   . 적기 출현 위치: 랜덤
#   . 시간이 지나면 적기의 이동속도 증가, 더 많은 적기의 출현
# ----------------------------------------------------------
# 할일
# - 적기 출현
#   . 여러 종류의 적기 이미지
#   . 적기의 이동, 곡선 경로 적용
#   . Class를 만들어서 분리하기
# - 총으로 격추하기: 총알 위치로 격추 상태 체크, 격추이면 적기 폭발 이미지로 변경, 잠시 후 사라짐
# - 피격, 적기와 충돌 체크: 전투기 폭파 후 게임 종료
# - 적기도 총 쏘기
# ----------------------------------------------------------

import pygame
from pygame import mixer 
from pygame import key
# TODO use random package
import random

# variables
pad_width = 1500
pad_height = 1024

class Enemy:
    Shapes = ["enemy", "enemy1", "enemy2", "enemy3"]
    # ShapeSizes = []
    Width = 30
    Height = 40

    # shape images
    ShapeImages = {}
    # for shape in Shapes:
    #     file_name = "res/" + shape + ".png"
    #     temp = pygame.image.load(file_name).convert_alpha()
    #     image = pygame.transform.scale(temp, (Width, Height))
    #     ShapeImages[shape] = temp
    #
    # # explosion image
    # temp = pygame.image.load("res/explosion.png").convert_alpha()
    # FiredImage = pygame.transform.scale(temp, (Width, Height))

    # for adjusting next drawing position
    timer = 20
    timerMax = 20
    delta_y = 1

    def __init__(self, shape):
        # TODO-
        self.shape = shape
        self.x = pad_width
        self.y = randint(0, pad_height-Enemy.Height)
        self.speed = randint(2, 5)

        self.fired = False

    def get_pos_x(self):
        return self.x

    def get_width(self):
        return self.w

    def set_fired(self):
        self.fired = True

    def draw(self, parent):
        timer += 1
        if timer > timerMax:
            timer = 0
            delta_y = random.randint(-1,1)
            timerMax = random.randint(0,50)
        ship_y = ship_y + delta_y
        ship_x += 1
        self.x -= self.speed
        self.y += randint(-5, 5)
        if self.y < 0:
            self.y = 0
        # pad_height = parent.get_height()
        if self.y > (pad_height - self.h):
            self.y = pad_height - self.h
        parent.blit(Enemy.ShapeImages[self.shape], (self.x, self.y))


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

# initialize pygame module
pygame.init()

# create game window
game_pad = pygame.display.set_mode((pad_width, pad_height))
pygame.display.set_caption("PyGame-42")

mixer.init()
mixer.music.load('res/bgm_BossMain.wav')
# play background music
#mixer.music.play()
# [TODO] 배경음악 무한 반복
mixer.music.play(-1, 0.0)
mixer.music.set_volume(0.5)

# create sound effects
shoot = mixer.Sound("res/shoot.wav")

# prepare background resources
# using 2 background images
bgImage1 = pygame.image.load("res/city_back_gray.png").convert()
bgImage2 = pygame.image.load("res/city_back_clean.png").convert_alpha()
bgImage1_h = bgImage1.get_height()
bgImage1_w = bgImage1.get_width()
# scaling image2 by 70% size of bgImage1
bgImage2 = pygame.transform.scale(bgImage2, (bgImage1_w*0.7, bgImage1_h*0.7))
bgImage2_h = bgImage2.get_height()
bgImage2_w = bgImage2.get_width()
bgImage2_y = bgImage1_h * 0.3
# set drawing 2 positions for each background
bgImage1_x1 = 0
bgImage1_x2 = bgImage1_w
bgImage2_x1 = 0
bgImage2_x2 = bgImage2_w

# create battle-ship
ship = pygame.image.load("res/ship.png").convert_alpha()
ship = pygame.transform.scale(ship, (60, 45))
ship_x = 0
ship_y = game_pad.get_height()/2

# create bullet
bullet = pygame.image.load("res/bullet.png").convert_alpha()
bullet = pygame.transform.scale(bullet, (70, 20))
# create bullet list
bullets = []

# [TODO] create enemy
enemy = pygame.image.load("res/enemy.png").convert_alpha()
enemy = pygame.transform.scale(enemy, (40, 35))
enemies = []

# create FPS timer
clock = pygame.time.Clock()

# infinite loop until close event
running = True
runningTime = 0
while running:
    # check the pressed arrow-keys
    keys = key.get_pressed()
    if keys[pygame.K_UP]:
        ship_y = ship_y - 2
    elif keys[pygame.K_DOWN]:
        ship_y = ship_y + 2
    elif keys[pygame.K_LEFT]:
        ship_x = ship_x - 2
    elif keys[pygame.K_RIGHT]:
        ship_x = ship_x + 2
            
    # check event list
    for event in pygame.event.get():
        # check QUIT event
        if event.type == pygame.QUIT:
            running = False
        # 스페이스바(총쏘기) 눌림 체크
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 현재 위치에 총알 추가
                bullets.append([ship_x + 30, ship_y + 10])
                # 효과음
                shoot.play()
                
    # draw 2 images by new position
    # 이미지를 그릴때마다 좌측으로 5씩 이동
    # 배경 이미지가 화면에서 벗어나면 위치를 리셋
    
    # 개선: draw image by reset position without blink
    # concatenate same 2 images
    bgImage1_x1 = bgImage1_x1 - 1
    bgImage1_x2 = bgImage1_x2 - 1
    if (bgImage1_x1 + bgImage1_w < 0):
        bgImage1_x1 = bgImage1_w
    if (bgImage1_x2 + bgImage1_w < 0):
        bgImage1_x2 = bgImage1_w
    game_pad.blit(bgImage1, (bgImage1_x1, 0))
    game_pad.blit(bgImage1, (bgImage1_x2, 0))
    
    bgImage2_x1 = bgImage2_x1 - 3
    bgImage2_x2 = bgImage2_x2 - 3
    if (bgImage2_x1 + bgImage2_w < 0):
        bgImage2_x1 = bgImage2_w
    if (bgImage2_x2 + bgImage2_w < 0):
        bgImage2_x2 = bgImage2_w
    game_pad.blit(bgImage2, (bgImage2_x1, bgImage2_y))
    game_pad.blit(bgImage2, (bgImage2_x2, bgImage2_y))    

    # draw battle-ship
    game_pad.blit(ship, (ship_x, ship_y))

    # draw bullets
    # 총알의 위치를 우측으로 조금씩 이동
    if len(bullets) > 0:
        for i, xy in enumerate(bullets):
            xy[0] += 5
            game_pad.blit(bullet, xy)
            # [TODO] 화면에서 벗어나면 삭제
            if xy[0] > pad_width:
                bullets.remove(xy)

    runningTime = runningTime + 1
    # [TODO] increase enemy show-up speed
    enemyLevel = min(int(runningTime/60), 49)
    # [TODO] add new enemy
    if (runningTime % (50-enemyLevel) == 0):
        enemies.append([pad_width, random.randint(0,pad_height)])

    # [TODO] draw enemies
    if len(enemies) > 0:
        #print("enemies", len(enemies))
        for i, xy in enumerate(enemies):
            xy[0] -= 3
            xy[1] += random.randint(0,5)
            xy[1] -= random.randint(0,5)
            game_pad.blit(enemy, xy)
            # [TODO] 화면에서 벗어나면 삭제
            if xy[0] < 0:
                enemies.remove(xy)
    
    # output game_pad on display
    pygame.display.update()

    # wait next frame with 60 FPS
    clock.tick(60)

# quit application
pygame.quit()
