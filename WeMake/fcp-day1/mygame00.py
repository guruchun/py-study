# TODO -----------------------------------------------------
# 1. 게임창 만들기
# 2. 게임창에 색칠하기
# 3. 모니터에 출력하기
# 4. 게임창 닫기
# 5. 연습: 배경색을 파랑, 노랑으로 바꿔보세요.
# ----------------------------------------------------------

import pygame
import time

# initialize pygame module
pygame.init()

# TODO-1
# 창 만들기(width, height)
game_pad = pygame.display.set_mode((1024, 768))

# TODO-2
# 배경색 칠하기 (r,g,b)
game_pad.fill((0, 255, 0))

# TODO-3
# 창을 실제 모니터에 표시하기
pygame.display.update()

# 게임창을 확인하기 위해 3초 기다림
time.sleep(3)

# TODO-5
# 게임을 종료함
pygame.quit()
