import pygame # 파이 게임 모듈 임포트
import random
from lion import Lion
from bomb import Bomb

pygame.init() # 파이 게임 초기화

# 화면 크기 설정
size = [600, 700]
SCREEN_WIDTH = size[0] # 화면 가로크기
SCREEN_HEIGHT = size[1] # 화면 세로크기
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 화면 크기 설정

# 게임 내 필요한 설정
clock = pygame.time.Clock()
pygame.key.set_repeat(10, 10) # 누르고 있는 키의 반복을 제어. (지연시간, 간격), 밀리세컨드

# 게임 타이틀 설정
pygame.display.set_caption("My Game")

# 변수선언
done = False
backGroundColor = (214,230,240)


# 라이언 객체 생성
lion = Lion()
lion.put_img() # 이미지 위치 설정
lion.x = round(size[0]/2 - lion.sx/2) # 처음 라이언 x위치
lion.y = size[1] - lion.sy # 처음 라이언 y위치
lion.move = 5

# 폭탄 객체 생성
bombs = []
for i in range(3):
    bomb = Bomb()
    bomb.put_img()  # 이미지 위치 설정
    bomb.x = random.randint(0, 600 - bomb.sx)
    bomb.y = -100
    bombs.append(bomb)

# 게임 루프
while not done:
    # 1. FPS 설정
    clock.tick(60)  # 30 FPS (초당 프레임 수), 초당 30번의 화면을 출력해주겠다는 것.

    # 2. 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if user clicked close
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lion.x -= lion.move
            elif event.key == pygame.K_RIGHT:
                lion.x += lion.move

    # 3. 입력, 시간에 따른 변화
    for bomb in bombs:
        bomb.y += 5
        if bomb.y > 800:
            bombs.remove(bomb)
            bomb.x = random.randint(0, 600 - bomb.sx)
            bomb.y = - 100
            bombs.append(bomb)

    # 화면 밖으로 나가지 않도록 설정
    if lion.x < 0:
        lion.x = 0
    elif lion.x > size[0] - lion.sx:
        lion.x = size[0] - lion.sx

    # 4. 그리기
    lion.show()
    for bomb in bombs:
        bomb.show()


    # 5. 업데이트
    pygame.display.update()  # 모든 화면 그리기 업데이트 (없으면 화면 출력 안됨)

    # 화면 그리기
    screen.fill(backGroundColor)



pygame.quit()