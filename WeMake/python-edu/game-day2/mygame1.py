# TODO -----------------------------------------------------
# 1. 클래스를 사용해 모듈화하기
#    a. 배경처리용 클래스 ScrollBackground 만들기
#    b. 인스턴스 변수: x, y, scroll_size, scroll_orientation
#               함수: set_scroll_size(size)
#    c. ScrollBackground 클래스를 사용하도록 기존 코드 수정
# 2. 비행기 이미지 생성
# 3. up/down 키 처리
# 4. 비행기 움직이기: up/down 키로 이동, 누른 상태는 up/down 계속
#    a. 비행기 좌표 계산
#    b. 비행기 그리기
# ----------------------------------------------------------

import pygame

# global variables
pad_width = 800
pad_height = 512
f_width = 40
f_height = 40
b_width = 30
b_height = 10
# BgColor = (255, 0, 255)


# TODO-1 클래스를 사용해 배경그리기 모듈화하기

# init graphics
def init():
    global game_pad, bgImage, bgImage2, clock, ship, bullet
    global bg_up_width, bg_down_width

    pygame.init()
    game_pad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption("My PyGame")

    # prepare resources
    # image height = 1024
    bg_upper_name = "res/city_background_night_gray.png"
    bg_lower_name = "res/city_background_clean.png"
    bgImage = pygame.image.load(bg_upper_name).convert()
    w = bgImage.get_width()
    bg_up_width = int(w / 2)
    bgImage = pygame.transform.scale(bgImage, (bg_up_width, pad_height))
    bgImage2 = pygame.image.load(bg_lower_name).convert_alpha()
    bg_down_width = int(w * 2 / 3)
    bgImage2 = pygame.transform.scale(bgImage2, (bg_down_width, int(pad_height * 2 / 3)))

    ###
    ship = pygame.image.load("res/ship.png").convert_alpha()
    ship = pygame.transform.scale(ship, (f_width, f_height))

    bullet = pygame.image.load("res/bullet.png").convert_alpha()
    bullet = pygame.transform.scale(bullet, (30, 10))

    # TODO-3

    clock = pygame.time.Clock()


def run():
    global game_pad, bgImage, bgImage2, clock, ship, bullet
    global bg_up_width, bg_down_width

    bg_down_1_x = 0
    bg_down_2_x = bg_down_width
    bg_up_1_x = 0
    bg_up_2_x = bg_up_width
    ###

    x_curr = 50
    y_curr = int(pad_height / 2)
    y_change = 0

    bullets = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            ###
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
                elif event.key == pygame.K_SPACE:
                    bullets.append([x_curr + f_width, y_curr + 20])

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        # draw background color
        # game_pad.fill(BgColor)

        # draw scrolling background
        bg_down_1_x -= 3
        bg_down_2_x -= 3
        if bg_down_1_x <= bg_down_width * (-1):
            bg_down_1_x = bg_down_width
        if bg_down_2_x <= bg_down_width * (-1):
            bg_down_2_x = bg_down_width
        # print(bg_down_1_x, bg_down_2_x)

        bg_up_1_x -= 1
        bg_up_2_x -= 1
        if bg_up_1_x <= bg_up_width * (-1):
            bg_up_1_x = bg_up_width
        if bg_up_2_x <= bg_up_width * (-1):
            bg_up_2_x = bg_up_width
        game_pad.blit(bgImage, (bg_up_1_x, 0))
        game_pad.blit(bgImage, (bg_up_2_x, 0))
        game_pad.blit(bgImage2, (bg_down_1_x, 170))
        game_pad.blit(bgImage2, (bg_down_2_x, 170))

        ###
        y_curr += y_change
        if y_curr < 0:
            y_curr = 0
        if y_curr > (pad_height - 40):
            y_curr = pad_height - 40
        game_pad.blit(ship, (50, y_curr))

        ###
        if len(bullets) > 0:
            for i, xy in enumerate(bullets):
                game_pad.blit(bullet, xy)
                xy[0] += 5
                if xy[0] > pad_width:
                    bullets.remove(xy)

        # TODO-3
        # TODO-5b
        # update display
        pygame.display.update()
        clock.tick(60)

    pygame.quit()


def main():
    init()
    run()


# python 파일을 실행할때만 main()을 호출한다.
if __name__ == "__main__":
    main()
