# import pygame # 파이 게임 모듈 임포트
# from lion import Lion
# import random
#
#
# pygame.init() # 파이 게임 초기화
#
# font = pygame.font.Font(None,36)
# score = 0
# font2 = pygame.font.Font('Maplestory+OTF+Light.otf', 70)  # 폰트 설정
#
# # 화면 크기 설정
# SCREEN_WIDTH = 600 # 화면 가로크기
# SCREEN_HEIGHT = 700 # 화면 세로크기
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 화면 크기 설정
#
# clock = pygame.time.Clock()
# pygame.key.set_repeat(10, 10) # 누르고 있는 키의 반복을 제어. (지연시간, 간격), 밀리세컨드
#
# # 게임 타이틀 설정
# pygame.display.set_caption("My Game")
#
# # 변수선언
# done = False
# backGroundColor = (214,230,240)
# game_over = False
# lion_image = pygame.image.load('asset/image/lion.png')
# lion = lion_image.get_rect(centerx=300, bottom=700) # lion 이라는 객체 생성
#
# bomb_image = pygame.image.load('asset/image/bomb.png')
# bombs = []
# for i in range(3):
#     bomb = bomb_image.get_rect(left=random.randint(0, 600), top=-100)
#     bombs.append(bomb)
#
# # clock.tick(60)  # 30 FPS (초당 프레임 수), 초당 30번의 화면을 출력해주겠다는 것.
# while not done: # 게임 루프
#
#     screen.fill(backGroundColor) # 단색으로 채워 화면 지우기
#
#     # 변수 업데이트
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: # if user clicked close
#             done = True
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 lion.left -= 5
#             elif event.key == pygame.K_RIGHT:
#                 lion.left += 5
#
#     for bomb in bombs:
#         bomb.top += 5
#         if bomb.top > 800:
#             bombs.remove(bomb)
#             bomb.left = random.randint(0, 600-bomb.width)
#             bomb.top = - 100
#             bombs.append(bomb)
#             score += 1
#
#     for bomb in bombs:
#         if bomb.colliderect(lion):
#             game_over = True
#
#     # 라이언이 프레임 밖으로 안나가게 설정
#     if lion.left < 0:
#         lion.left = 0
#     elif lion.right > 600:
#         lion.right = 600
#
#     for bomb in bombs:
#         screen.blit(bomb_image, bomb)
#
#     screen.blit(lion_image, lion)
#     screen.blit(bomb_image, bomb)
#
#     score_image = font.render('점수 {}'.format(score), True, (255,255, 0))
#     screen.blit(score_image, (10, 10))
#
#     if game_over:
#         game_over_image = font2.render('게임 종료', True, (255, 0, 0))
#         screen.blit(game_over_image, (300, 400))
#     # 화면 그리기
#     pygame.display.update()  # 모든 화면 그리기 업데이트 (없으면 화면 출력 안됨)
#     clock.tick(60)  # 30 FPS (초당 프레임 수), 초당 30번의 화면을 출력해주겠다는 것.
#
# pygame.quit()

#슈팅 게임
import random
import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, K_UP,K_DOWN,K_SPACE,K_a,Rect

pygame.init()
pygame.display.set_caption('SHOOT_GAME')
pygame.key.set_repeat(15,15)
SURFACE = pygame.display.set_mode((1000,600))
FPSCLOCK = pygame.time.Clock()
Big_font = pygame.font.SysFont(None, 80)
Small_font = pygame.font.SysFont(None, 40)

class Draw:
    def __init__(self,col,rect,speed = 0):
        self.col = col
        self.rect = rect
        self.speed = speed
    def move(self):
        self.rect.centerx += self.speed
    def draw_E(self):
        pygame.draw.ellipse(SURFACE,self.col,self.rect)
    def draw_R(self):
        pygame.draw.rect(SURFACE,self.col,self.rect)


def Game_Border():
    Start_Point = [(100,150),(100,150),(100,550),(900,150)]
    End_Point = [(100,550),(900,150),(900,550),(900,550)]
    for index in range(len(Start_Point)):
        pygame.draw.line(SURFACE,(255,255,255),Start_Point[index],End_Point[index])

def main():
    rock_speed = -5
    RockWIDTH = 50
    RockHEIGHT = 50
    xpos = 880
    ypos = random.randint(0,8)
    Rock = []
    game_start = False
    Miss = 0
    Score = 0
    Beam_Count = 0
    Cir = Draw((255, 255, 255), Rect(50,300, 30,30))
    Beam = Draw((255, 255, 0), Rect(Cir.rect.centerx, Cir.rect.centery, 5, 5), 10)
    while True:
        message_Title = Big_font.render("SHOOT_GAME", True, (255, 255, 255))  # 게임제목 적기
        message_Score = Small_font.render("Score: {}".format(Score), True, (255, 255, 255))  # 스코어
        message_Miss = Small_font.render("Miss_Point: {}".format(Miss), True, (255, 255, 255))  # 놓친장애물수
        message_game_start = Small_font.render("Game_start : Click the Space_Bar", True, (255, 255, 255))  # 게임시작
        message_game_over = Big_font.render("Game_over_Score : {}".format(Score), True, (255, 255, 255))  # 게임오버
        message_caution = Small_font.render("Missile_Button : A , Missile is only one ", True, (255, 255, 255))
        SURFACE.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    rock_speed = -5
                    Miss = 0
                    Score = 0
                    game_start = True
                elif event.key == K_UP:
                    Cir.rect.centery -= 10
                elif event.key == K_DOWN:
                    Cir.rect.centery += 10
                elif event.key == K_a:
                    if Beam_Count == 0:
                        Beam_Count =1
                        Beam.rect.center = Cir.rect.center
                    else:
                        Beam.draw_E()
                        #Beam.move() a를 계속 누르고 잇으면 빔속도가 빨라진다.
        if  game_start:
            SURFACE.blit(message_Title, (350, 20))  # 화면상에 제목 표시
            SURFACE.blit(message_Score, (750, 160))  # 화면상에 스코어 표시
            SURFACE.blit(message_caution,(280,100)) #화면상에 주의사항 표시
            SURFACE.blit(message_Miss,(700,200)) #놓친블럭수 표시
            Game_Border()
            Cir.draw_E()

            if Cir.rect.centery <= 170:
                Cir.rect.centery = 170
            elif Cir.rect.centery >= 530:
                Cir.rect.centery = 530

            if Beam_Count == 1:
                Beam.draw_E()
                Beam.move()
                if Beam.rect.centerx >= 900:
                    Beam.rect.center = Cir.rect.center
                    Beam_Count = 0

            if len(Rock) == 0:
                Rock.append(Draw((0, 255, 0), Rect(xpos, ypos * 40 + 170, RockWIDTH - ypos*3 , RockHEIGHT - ypos*3), rock_speed))
            elif len(Rock) ==1:
                Rock[0].draw_R()
                Rock[0].move()
                if Rock[0].rect.colliderect(Beam.rect):
                    Beam.rect.center = Cir.rect.center
                    Beam_Count = 0
                    Score +=100
                    rock_speed -=0.25
                    del Rock[0]
                    ypos = random.randint(0, 8)
                elif Rock[0].rect.centerx <= 100:
                    Beam.rect.center = Cir.rect.center
                    Beam_Count = 0
                    Miss +=1
                    del Rock[0]
                    ypos = random.randint(0, 8)
            if Miss == 3:
                game_start = False

        elif not game_start and Miss ==3:
            SURFACE.blit(message_game_over, (250, 200))
            SURFACE.blit(message_game_start, (300, 300))
        else:
            SURFACE.blit(message_Title, (320, 200))
            SURFACE.blit(message_game_start, (300, 300))

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()