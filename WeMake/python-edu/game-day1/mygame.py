# TODO -----------------------------------------------------
# 1. 함수를 사용해 모듈화하기
#    a. init() 함수 분리
#    b. run() 함수 분리
#    c. main() 함수 분리
# 2. 배경 움직이기
#    a. 배경 이미지 생성
#    b. 배경 이미지 좌표 계산
#    c. 상하영역을 나눠서 다른 속도로 배경 스크롤
# ----------------------------------------------------------

import pygame

# global variables
pad_width = 540
pad_height = 512
BgColor = (255, 255, 255)

# TODO-1a
# init graphics
pygame.init()
game_pad = pygame.display.set_mode((pad_width, pad_height))
pygame.display.set_caption("My PyGame")

# prepare resources
# TODO-2a
bgImage = pygame.image.load("res/bg_cloud.png").convert()
bgImage = pygame.transform.scale(bgImage, (pad_width, pad_height))

# TODO-3

clock = pygame.time.Clock()

# TODO-1b
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # TODO-4
        # TODO-5a

    # draw background
    game_pad.fill(BgColor)

    # TODO-2b
    game_pad.blit(bgImage, (0, 0))
    # TODO-3
    # TODO-5b
    # update display
    pygame.display.update()
    clock.tick(60)

pygame.quit()

# TODO-1c
