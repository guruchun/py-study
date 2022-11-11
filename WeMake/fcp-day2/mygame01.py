# TODO -----------------------------------------------------
# 1. 숫자 대신 변수 사용: 화면 크기
# 2. 배경색 -> 배경 이미지
# 3. 3초 후 종료 --> 닫기 버튼 누르면 종료, 그 때까지 무한 반복
#  a. 게임창 닫기 버튼이 눌렸는지 확인
# 4. 1초 60번씩 화면을 다시 그리기
# 5. 게임창을 닫으면 종료함
# ----------------------------------------------------------

import pygame

# TODO-1
# 숫자 -> 변수
pad_width = 1024
pad_height = 768

# initialize pygame module
pygame.init()

# create game window
game_pad = pygame.display.set_mode((pad_width, pad_height))
pygame.display.set_caption("PyGame-01")

# TODO-2a
# prepare background resources
bgImage = pygame.image.load("bg_city.png").convert()
#bgImage = pygame.transform.scale(bgImage, (pad_width, pad_height))

# TODO-4a
# create refresh timer
clock = pygame.time.Clock()

# TODO-3
running = True
while running:
    # TODO-3a
    # pygame 모듈의 기능을 사용해서 이벤트 가져오기
    # 예) 키보드가 눌렸는지, 마우스가 움직였는지 등...
    for event in pygame.event.get():
        # 게임창 닫기 버튼이 눌렸는지 조사
        # 닫기 버튼이 눌렸으면 게임화면 그리기를 종료하기 위해 running울 False로 바꿈
        if event.type == pygame.QUIT:
            running = False
            print("clieked close button")

    # TODO-2b
    # 이미지 그리기
    game_pad.blit(bgImage, (0, 0))

    # 모니터에 출력하기
    # pygame 모듈을 통해 그린 화면을 실제 모니터에 표시함
    pygame.display.update()

    # TODO-4b
    # 1초에 화면이 60회 그려지도록 시간이 남으면 쉬었다가 다음으로 넘어감
    clock.tick(60)
    print("updated")

# TODO-5
# 게임을 종료함
pygame.quit()
