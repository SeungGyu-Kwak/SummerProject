import pygame # 파이 게임 모듈 임포트
from lion import Lion
from bomb import Bomb
import random

pygame.init() # 파이 게임 초기화

# 화면 크기 설정
size = [600, 700]
SCREEN_WIDTH = size[0] # 화면 가로크기
SCREEN_HEIGHT = size[1] # 화면 세로크기
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 화면 크기 설정

# 라이언 객체 생성
def createLion():
    lion = Lion()
    lion.put_img()  # 이미지 위치 설정
    lion.x = round(size[0] / 2 - lion.sx / 2)  # 처음 라이언 x위치
    lion.y = size[1] - lion.sy  # 처음 라이언 y위치
    lion.move = 5
    return lion

# 폭탄 객체 생성
def createBomb():
    bombs = []
    for i in range(2):
        bomb = Bomb()
        bomb.put_img()  # 이미지 위치 설정
        bomb.x = random.randint(0, 600 - bomb.sx)
        bomb.speed = random.randint(3, 9)
        bomb.y = -100
        bombs.append(bomb)

    return bombs

# BGM 설정 메소드
def backGroundSound():
    pygame.mixer.init()
    pygame.mixer.music.load('asset/music/music.mid')  # 배경 음악
    pygame.mixer.music.play(-1)  # -1: 무한 반복, 0: 한번

# gameover sound 설정
def gameoverSound():
    game_over_sound = pygame.mixer.Sound('asset/music/gameover.wav')
    return game_over_sound

def collisionSound():
    collision_sound = pygame.mixer.Sound('asset/music/fail.wav')
    return collision_sound