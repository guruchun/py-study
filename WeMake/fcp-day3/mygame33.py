# ----------------------------------------------------------
# 완료
# - 배경 움직이기, 2장으로 원근효과 주기
# - 전투기 띄우기, 전투기 움직이기, 키보드 방향키 사용
# ----------------------------------------------------------
# 목표
# - 이론: Class와 함수(def)
# - 배경이미지 개선
#   . 이미지 스크롤이 끝나면 자연스럽게 다시 이미지 시작위치와 연결
#   . 부드럽게 움직이도록 FPS를 60에서 120으로 변경
# - 전투기 이동: 방향키 누른 상태에서 계속 이동
#   . 좀 이상하게 동작한다. 개선해 보자.
#   . 총쏘면서 이동하기
#   . 동시에 누르면 대각선으로 이동하기
# - 배경음악, 효과음
#   . 배경음악: 무한 반복
#   . 효과음: 발사
# ----------------------------------------------------------
# 할일
# - 적기 출현, 적기의 이동(곡선 경로)
# - 총으로 격추하기: 총알 위치로 격추 상태 체크, 격추이면 적기 이미지 변경
# - 적기도 총 쏘기
# - 피격, 적기와 충돌 체크: 전투기 폭파 후 게임 종료
# ----------------------------------------------------------

import pygame
from pygame import key
from pygame import mixer
import random

# variables
pad_width = 1500
pad_height = 1024
# TODO-1a
bg1_x = 0
bg2_x = 0

# initialize pygame module
pygame.init()

# create game window
game_pad = pygame.display.set_mode((pad_width, pad_height))
pygame.display.set_caption("PyGame-33")

# create background music
mixer.init()
mixer.music.load('res/bgm_BossMain.wav')

# play background music
#mixer.music.play()
# 무한 반복
mixer.music.play(-1, 0.0)
mixer.music.set_volume(0.5)

# create sound effects
shoot = mixer.Sound("res/shoot.wav")

# prepare background resources
# using 2 background images
bgImage1 = pygame.image.load("res/city_back_gray.png").convert()
bgImage1_h = bgImage1.get_height()
bgImage1_w = bgImage1.get_width()
bgImage1_x1 = 0
bgImage1_x2 = bgImage1_w

bgImage2 = pygame.image.load("res/city_back_clean.png").convert_alpha()
# scaling image2 by 70% size of bgImage1
bgImage2 = pygame.transform.scale(bgImage2, (bgImage1_w*0.7, bgImage1_h*0.7))
bgImage2_h = bgImage2.get_height()
bgImage2_w = bgImage2.get_width()
bgImage2_x1 = 0
bgImage2_x2 = bgImage2_w
bgImage2_y = bgImage1_h * 0.3

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

# create FPS timer
clock = pygame.time.Clock()

# ininite loop until close event
running = True
timer = 20
timerMax = 20
delta_y = 1
while running:
    # check the pressed arrow-keys
    keys = key.get_pressed()
    if keys[pygame.K_UP]:
        ship_y = ship_y - 2
    if keys[pygame.K_DOWN]:
        ship_y = ship_y + 2
    if keys[pygame.K_LEFT]:
        ship_x = ship_x - 2
    if keys[pygame.K_RIGHT]:
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
##    timer += 1
##    if timer > timerMax:
##        timer = 0
##        delta_y = random.randint(-1,1)
##        timerMax = random.randint(0,50)
##    ship_y = ship_y + delta_y
    
    ship_x += 1
    game_pad.blit(ship, (ship_x, ship_y))

    # draw bullets
    # 총알의 위치를 우측으로 조금씩 이동
    if len(bullets) > 0:
        for i, xy in enumerate(bullets):
            xy[0] += 3
            game_pad.blit(bullet, xy)

    # output game_pad on display
    pygame.display.update()

    # wait next frame with 60 FPS
    clock.tick(100)

# quit application
pygame.quit()
