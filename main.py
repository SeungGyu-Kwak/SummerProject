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
font1 = pygame.font.Font('Maplestory+OTF+Light.otf', 30)  # 폰트 설정
font2 = pygame.font.Font('Maplestory+OTF+Light.otf', 70)  # 폰트 설정

# 게임 타이틀 설정
pygame.display.set_caption("My Game")

# 변수선언
done = False
backGroundColor = (214,230,240)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
score = 0 # 점수
game_over = False

# 라이언 객체 생성
lion = Lion()
lion.put_img() # 이미지 위치 설정
lion.x = round(size[0]/2 - lion.sx/2) # 처음 라이언 x위치
lion.y = size[1] - lion.sy # 처음 라이언 y위치
lion.move = 5

# 폭탄 객체 생성
bombs = []
for i in range(1):
    bomb = Bomb()
    bomb.put_img()  # 이미지 위치 설정
    bomb.x = random.randint(0, 600 - bomb.sx)
    bomb.y = -100
    bombs.append(bomb)

# 충돌 판정 함수
def collision_check(A, B):
    if A.y < B.y + B.sy and B.y < A.y + A.sy and A.x < B.x + B.sx and B.x < A.x + A.sx:
        return True
    else:
        return False

# 음악설정
pygame.mixer.init()
pygame.mixer.music.load('asset/music/music.mid') #배경 음악
pygame.mixer.music.play(-1) #-1: 무한 반복, 0: 한번
game_over_sound = pygame.mixer.Sound('asset/music/game_over.wav')

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
            bomb.fall ()

            if bomb.isFallen (): # 폭탄 계속 나오게 설정
                bombs.remove(bomb)
                bomb.x = random.randint(0, 600 - bomb.sx)
                bomb.y = - 100
                bombs.append(bomb)
                score += 1 # 폭탄이 내려가면 점수 카운트



    # 4. 그리기
    lion.show()
    for bomb in bombs:
        bomb.show()

    score_image = font1.render('점수 {}'.format(score), True, YELLOW) # 점수 화면
    screen.blit(score_image, (20, 20))

    # (1) 충돌 판정
    for bomb in bombs:
        game_over = lion.isCollison(bomb)
        if game_over:
            pygame.mixer.music.stop()
            break

    if game_over:
        game_over_image = font2.render('게임 종료', True, RED)
        screen.blit(game_over_image, game_over_image.get_rect(centerx=SCREEN_WIDTH // 2, centery= SCREEN_HEIGHT // 2))
        game_over_sound.play()

    # 5. 업데이트
    pygame.display.update()  # 모든 화면 그리기 업데이트 (없으면 화면 출력 안됨)

    # 화면 그리기
    screen.fill(backGroundColor)


pygame.quit()