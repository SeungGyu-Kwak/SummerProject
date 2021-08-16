import pygame # 파이 게임 모듈 임포트
import random
from time import sleep
from game_manager import createLion, createBomb, backGroundSound, gameoverSound, collisionSound


pygame.init() # 파이 게임 초기화

# 화면 크기 설정
size = [600, 700]
SCREEN_WIDTH = size[0] # 화면 가로크기
SCREEN_HEIGHT = size[1] # 화면 세로크기
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 화면 크기 설정

# 게임 내 필요한 설정
clock = pygame.time.Clock()
pygame.key.set_repeat(10, 10) # 누르고 있는 키의 반복을 제어. (지연시간, 간격), 밀리세컨드
font1 = pygame.font.Font('Maplestory+OTF+Light.otf', 30)  # 폰트 설정
font2 = pygame.font.Font('Maplestory+OTF+Light.otf', 70)  # 폰트 설정
font3 = pygame.font.Font('Maplestory+OTF+Light.otf', 30)  # 폰트 설정

# 게임 타이틀 설정
pygame.display.set_caption("My Game")

# 변수선언
done = False
backGroundColor = (214,230,240)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
score = 0 # 점수
life = 3 # 수명
game_over = False
is_gameover = False


# 라이언 객체 생성
lion = createLion()

# 폭탄 객체 생성
bombs = createBomb()

# 음악설정
backGroundSound()
game_over_sound = gameoverSound()
collision_sound = collisionSound()


# 게임 루프
while not done:
    # 1. FPS 설정
    clock.tick(60)  # 30 FPS (초당 프레임 수), 초당 30번의 화면을 출력해주겠다는 것.

    # 2. 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if user clicked close
            done = True
        if event.type == pygame.KEYDOWN:
            lion.shift (event.key)

    # 3. 입력, 시간에 따른 변화
    if not game_over:
        for bomb in bombs:
            bomb.fall()
            if bomb.isFallen(): # 폭탄 계속 나오게 설정
                bombs.remove(bomb)
                bomb.reCreate()
                bombs.append(bomb)
                score += 1 # 폭탄이 내려가면 점수 카운트

    # 4. 그리기
    lion.show()
    for bomb in bombs:
        bomb.show()

    score_image = font1.render('점수: {}'.format(score), True, YELLOW) # 점수 화면
    screen.blit(score_image, (20, 20))

    life_image = font3.render('수명: {}'.format(life), True, RED) # 수명
    screen.blit(life_image, (500, 20))

    # (1) 충돌 판정
    for bomb in bombs:
        collision = lion.isCollision(bomb)
        if collision:
            life -= 1
            bombs.remove(bomb)
            bomb.reCreate()
            bombs.append(bomb)
            if life == 0:
                pygame.mixer.music.stop()
                game_over_sound.play()
                game_over = True
                break
            else:
                collision_sound.play()

    if game_over:
        game_over_image = font2.render('게임 종료', True, RED)
        screen.blit(game_over_image, game_over_image.get_rect(centerx=SCREEN_WIDTH // 2, centery= SCREEN_HEIGHT // 2))


    # 5. 업데이트
    pygame.display.update()  # 모든 화면 그리기 업데이트 (없으면 화면 출력 안됨)

    # 화면 그리기
    screen.fill(backGroundColor)


pygame.quit()