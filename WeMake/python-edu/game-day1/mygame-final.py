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
pad_width = 1024
pad_height = 768
BgColor = (255, 0, 255)


# TODO-1a
# init graphics
def init():
    global game_pad, bgImage, bgImage2, clock

    pygame.init()
    game_pad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption("My PyGame")

    # prepare resources
    # TODO-2a: 이어붙일 이미지를 한장 더 생성
    # TODO-2c: 여러장의 이미지
    bgImage = pygame.image.load("res/bg1.png").convert()
    bgImage = pygame.transform.scale(bgImage, (pad_width, pad_height))
    bgImage2 = pygame.image.load("res/bg1.png").convert()
    bgImage2 = pygame.transform.scale(bgImage2, (pad_width, pad_height))

    # TODO-3

    clock = pygame.time.Clock()


# TODO-1b
def run():
    global game_pad, bgImage, bgImage2, clock

    bg1_x = 0
    bg2_x = pad_width
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
        bg1_x -= 5
        bg2_x -= 5
        if bg1_x <= -pad_width:
            bg1_x = pad_width
        if bg2_x <= -pad_width:
            bg2_x = pad_width
        game_pad.blit(bgImage, (bg1_x, 0))
        game_pad.blit(bgImage2, (bg2_x, 0))

        # TODO-3
        # TODO-5b
        # update display
        pygame.display.update()
        clock.tick(60)

    pygame.quit()


# TODO-1c
def main():
    init()
    run()


# python 파일을 실행할때만 main()을 호출한다.
if __name__ == "__main__":
    main()
