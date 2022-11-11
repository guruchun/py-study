# TODO -----------------------------------------------------
# 1. 배경그림을 다시 그릴 때마다 좌측으로 5씩 이동합니다.
#  a. 배경그림의 좌표를 변수에 저장합니다.
# 2. 배경그림이 화면에서 벗어나면 좌표를 0으로 리셋합니다.
# 3. 배경 그림을 2개 출력합니다.
#  a. 앞배경은 화면 높이의 70%만 차지하도록 조절합니다.
#  b. 앞배경은 5씩, 뒷배경은 2씩 좌측으로 이동합니다.
#     앞배경의 높이가 줄었으므로 출력위치도 조절합니다.
# 4. 배경의 좌표가 리셋될 때 흰색 배경이나 깜박이 없도록 합니다.
# ----------------------------------------------------------

import pygame

# variables
pad_width = 1024
pad_height = 768
# TODO-1a
bg1_x = 0
#bg2_x = 0

# initialize pygame module
pygame.init()

# create game window
game_pad = pygame.display.set_mode((pad_width, pad_height))
pygame.display.set_caption("PyGame-10a")

# prepare background resources
bgImage = pygame.image.load("bg_city.png").convert()
# TODO-3
# using 2 background images
#bgImage1 = pygame.image.load("city_back.png").convert()
#bgImage2 = pygame.image.load("city_front.png").convert()
# TODO-3a
# scaling image2 by 70% size: bgImage2.get_width()
#bgImageX = pygame.transform.scale(bgImageX, (bgImageX.get_width()*%, bgImageX.get_height()*%))

# create FPS timer
clock = pygame.time.Clock()

# ininite loop until close event
running = True
while running:
    # check event list
    for event in pygame.event.get():
        # check QUIT event
        if event.type == pygame.QUIT:
            running = False

    # draw image
    # TODO-1
    # 이미지를 그릴때마다 좌측으로 5씩 이동
    bg1_x -= 5
    # TODO-2
    # 배경이미지가 화면에서 벗어나면 위치를 리셋
#    if (bgImage.get_width() + bg1_x < 0):
    if (bgImage.get_width() + bg1_x < game_pad.get_width()):
        bg1_x = 0
    game_pad.blit(bgImage, (bg1_x, 0))
    # TODO-3b
    # draw 2 images by new position

    # TODO-4
    # draw 2 images by reset position without blink

    # output game_pad on display
    pygame.display.update()

    # wait next frame with 60 FPS
    clock.tick(60)

# quit application
pygame.quit()
