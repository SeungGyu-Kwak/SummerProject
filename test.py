import pygame # 파이 게임 모듈 임포트
from lion import Lion
import random


pygame.init() # 파이 게임 초기화

font = pygame.font.Font(None,36)
score = 0
font2 = pygame.font.Font('Maplestory+OTF+Light.otf', 70)  # 폰트 설정

# 화면 크기 설정
SCREEN_WIDTH = 600 # 화면 가로크기
SCREEN_HEIGHT = 700 # 화면 세로크기
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 화면 크기 설정

clock = pygame.time.Clock()
pygame.key.set_repeat(10, 10) # 누르고 있는 키의 반복을 제어. (지연시간, 간격), 밀리세컨드

# 게임 타이틀 설정
pygame.display.set_caption("My Game")

# 변수선언
done = False
backGroundColor = (214,230,240)
game_over = False
lion_image = pygame.image.load('asset/image/lion.png')
lion = lion_image.get_rect(centerx=300, bottom=700) # lion 이라는 객체 생성

bomb_image = pygame.image.load('asset/image/bomb.png')
bombs = []
for i in range(3):
    bomb = bomb_image.get_rect(left=random.randint(0, 600), top=-100)
    bombs.append(bomb)

# clock.tick(60)  # 30 FPS (초당 프레임 수), 초당 30번의 화면을 출력해주겠다는 것.
while not done: # 게임 루프

    screen.fill(backGroundColor) # 단색으로 채워 화면 지우기

    # 변수 업데이트

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if user clicked close
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lion.left -= 5
            elif event.key == pygame.K_RIGHT:
                lion.left += 5

    for bomb in bombs:
        bomb.top += 5
        if bomb.top > 800:
            bombs.remove(bomb)
            bomb.left = random.randint(0, 600-bomb.width)
            bomb.top = - 100
            bombs.append(bomb)
            score += 1

    for bomb in bombs:
        if bomb.colliderect(lion):
            game_over = True

    # 라이언이 프레임 밖으로 안나가게 설정
    if lion.left < 0:
        lion.left = 0
    elif lion.right > 600:
        lion.right = 600

    for bomb in bombs:
        screen.blit(bomb_image, bomb)

    screen.blit(lion_image, lion)
    screen.blit(bomb_image, bomb)

    score_image = font.render('점수 {}'.format(score), True, (255,255, 0))
    screen.blit(score_image, (10, 10))

    if game_over:
        game_over_image = font2.render('게임 종료', True, (255, 0, 0))
        screen.blit(game_over_image, (300, 400))
    # 화면 그리기
    pygame.display.update()  # 모든 화면 그리기 업데이트 (없으면 화면 출력 안됨)
    clock.tick(60)  # 30 FPS (초당 프레임 수), 초당 30번의 화면을 출력해주겠다는 것.

pygame.quit()