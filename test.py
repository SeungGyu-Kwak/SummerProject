import pygame # 파이 게임 모듈 임포트

pygame.init() # 파이 게임 초기화

# 화면 크기 설정
SCREEN_WIDTH = 600 # 화면 가로크기
SCREEN_HEIGHT = 600 # 화면 세로크기
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 화면 크기 설정

clock = pygame.time.Clock()

# 게임 타이틀 설정
pygame.display.set_caption("My Game")

# 변수선언
backGroundColor = (214,230,240)
girl_image = pygame.image.load('asset/image/lion.png')


while True: # 게임 루프 # 게임루프입니다.

    screen.fill(backGroundColor) # 단색으로 채워 화면 지우기

    # 변수 업데이트

    event = pygame.event.poll() # 이벤트 처리
    if event.type == pygame.QUIT: # if user clicked close
        break

    screen.blit(girl_image, (300 - girl_image.get_width() / 2, 600 - girl_image.get_height()))

    # 화면 그리기
    pygame.display.update()  # 모든 화면 그리기 업데이트
    clock.tick(30)  # 30 FPS (초당 프레임 수), 초당 30번의 화면을 출력해주겠다는 것.

pygame.quit()