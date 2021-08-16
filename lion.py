import pygame # 파이 게임 모듈 임포트
pygame.init() # 파이 게임 초기화


# 화면 크기 설정
size = [600, 700]
SCREEN_WIDTH = size[0] # 화면 가로크기
SCREEN_HEIGHT = size[1] # 화면 세로크기
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 화면 크기 설정

# 캐릭터 클래스 생성하기
class Lion(pygame.sprite.Sprite):

    # 생성자
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('asset/image/lion.png')
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.move = 0

    def put_img(self):

        self.sx, self.sy = self.image.get_size() # 현재 이미지에 대한 크기를 각각 sx, sy에 저장

    def show(self):
       screen.blit(self.image, (self.x, self.y))

    def shift (self, key):
        if key == pygame.K_LEFT:
            self.x -= self.move
        elif key == pygame.K_RIGHT:
            self.x += self.move

        # 화면 밖으로 나가지 않도록 설정
        if self.x < 0:
            self.x = 0
        elif self.x > size[0] - self.sx:
            self.x = size[0] - self.sx

    def isCollision (self, bomb):
        if self.y < bomb.y + bomb.sy and \
                bomb.y < self.y + self.sy and \
                self.x < bomb.x + bomb.sx and \
                bomb.x < self.x + self.sx:
            return True
        else:
            return False















    # self.rect = self.image.get_rect(centerx=x, bottom=y)  # lion 이라는 객체 생성
    # 라이언을 스크린에 그리기
    # def draw_Lion(self):
    #     screen.blit(self.image, self.rect)


    # def load_Lion(self):
    #     for event in pygame.event.get():
    #         if event.type == pygame.KEYDOWN:
    #                 if event.key == pygame.K_LEFT:
    #                     Lion.left   -= 5
    #                 elif event.key == pygame.K_RIGHT:
    #                     Lion.left += 5

    # def check_screen(self):
    #     # 라이언이 프레임 밖으로 안나가게 설정
    #     if Lion.left < 0:
    #         Lion.left = 0
    #     elif Lion.right > 600:
    #         Lion.right = 600


