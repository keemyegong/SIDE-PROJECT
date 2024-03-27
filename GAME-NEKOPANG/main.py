
import pygame
import sys
import random

pygame.init() # pygame 모듈 초기화

img_neko = [ 
    None,
    pygame.image.load("neko1.png"),
    pygame.image.load("neko2.png"),
    pygame.image.load("neko3.png"),
    pygame.image.load("neko4.png"),
    pygame.image.load("neko5.png"),
    pygame.image.load("neko6.png"),
    pygame.image.load("neko_niku.png"),
]

map_y = 10
map_x = 8
display_width = 912
display_height = 768
bg = pygame.image.load("neko_bg.png")
cursor = pygame.image.load("neko_cursor.png")

neko = [[] for _ in range(map_y)]
check = [[0 for _ in range(map_x)] for _ in range(map_y)]
search = [[0 for _ in range(map_x)] for _ in range(map_y)]

for y in range(map_y):
    for x in range(map_x):
        neko[y].append(random.choice(range(1,7)))


gameDisplay = pygame.display.set_mode((display_width, display_height)) #스크린 초기화
pygame.display.set_caption("애니팡")  # 타이틀
clock = pygame.time.Clock() #Clock 오브젝트 초기화

class Mouse :
    def __init__(self,cursor,map_y,map_x):
        self.turn = 0
        self.cursor = cursor
        self.map_y = map_y
        self.map_x = map_x

    def get_mouse(self):
        position = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for y in range(map_y):
            for x in range(map_x):
                if x*72+20 < position[0] < (x+1)*72+20 and y*72+20 < position[1] < (y+1)*72+20 :
                    if self.turn == 0 :
                        gameDisplay.blit(self.cursor,(x*72+20,y*72+20))
                        if click[0] :
                            self.turn = 1
                            check[y][x] = 1
                    else :
                        if (0 <= y-1 and check[y-1][x] == 1) or (y+1 < self.map_y and check[y+1][x] == 1) \
                            or (self.map_x > x+1 and check[y][x+1] == 1) or (0 <= x-1 and check[y][x-1] == 1):
                            gameDisplay.blit(self.cursor,(x*72+20,y*72+20)) 
                            if click[0] :
                                self.turn = 0
                                check[y][x] = 1
                                switch_neko()
                                if not check_switch(y, x):
                                    switch_neko()
                                cursor_set()
                        if click[2] :
                            self.turn = 0
                            cursor_set()

def switch_neko(): # neko swap
    swap = []
    for y in range(map_y):
        for x in range(map_x):
            if check[y][x] == 1:
                swap.append((y, x))
                if len(swap) == 2:
                    neko[swap[0][0]][swap[0][1]], neko[swap[1][0]][swap[1][1]] = neko[swap[1][0]][swap[1][1]], neko[swap[0][0]][swap[0][1]]

def check_neko(idx): # 상화좌우 3 조건 맞추면 7로 바꿔주기
    for y in range(map_y):
        cnt = 1
        for x in range(map_x-1):
            if neko[y][x] == neko[y][x+1]:
                cnt += 1 
            else:
                if cnt >= 3:
                    for i in range(cnt):
                        neko[y][x-i] = 7
                        idx = 1
                cnt = 1
        if cnt >= 3:
            for i in range(cnt):
                neko[y][x-i+1] = 7
                idx = 1

    for x in range(map_x):
        cnt = 1
        for y in range(map_y-1):
            if neko[y][x] == neko[y+1][x]:
                cnt += 1     
            else:
                if cnt >= 3:
                    for i in range(cnt):
                        neko[y-i][x] = 7
                        idx = 1
                cnt = 1
        if cnt >= 3:
            for i in range(cnt):
                neko[y-i+1][x] = 7
                idx = 1
    return idx
                        
def cursor_set():
    for y in range(map_y):
        for x in range(map_x):
            check[y][x] = 0

def cursor_draw():
    for y in range(map_y):
        for x in range(map_x):
            if check[y][x] == 1:
                gameDisplay.blit(cursor,(x*72+20, y*72+20))

def neko_draw():
    for y in range(map_y):
        for x in range(map_x):
            if neko[y][x] > 0:
                gameDisplay.blit(img_neko[neko[y][x]], (x*72+20, y*72+20))

def drop_neko():
    for x in range(map_x):
        for y in range(map_y - 1, 0, -1):  # 맨 아래부터 시작
            if neko[y][x] == 0:
                for k in range(y, 0, -1):  # 현재 위치부터 위로 이동
                    if neko[k][x] != 0:  # 위쪽에 네코가 있을 경우
                        neko[y][x] = neko[k][x]  # 현재 위치에 위쪽 네코를 이동
                        neko[k][x] = 0  # 원래 위치는 빈 공간으로 만듦
                        break
                else:  # 가장 위에 있는 경우
                    neko[y][x] = random.choice(range(1, 7))  # 랜덤으로 새로운 네코 생성
    for x in range(map_x):
        if neko[0][x] == 0:
            neko[0][x] = random.choice(range(1, 7))
    # game 함수 while 이 한 번 돌때마다 
    #      빈 공간(0)이 있을 시 위에 있는 네코가 밑으로 내려와야 됨
    #              맨위에 있는 칸이 빈공간일 경우는 랜덤으로 생성시켜야 됨

def sweep_neko():
    for y in range(map_y):
        for x in range(map_x):
            if neko[y][x] == 7:
                neko[y][x] = 0
     # 7이었던 리스트를 0으로 만들어서 빈공간으로 만들어줘야됨

def check_switch(y,x):
    for y in range(10):
        for x in range(8):
            search[y][x] = neko[y][x]

    for y in range(1, 9):
        for x in range(8):
            if search[y][x] > 0:
                if search[y-1][x] == search[y][x] and search[y+1][x] == search[y][x]:
                    return True

    for y in range(10):
        for x in range(1, 7):
            if search[y][x] > 0:
                if search[y][x-1] == search[y][x] and search[y][x+1] == search[y][x]:
                    return True
    return False

    
    # 네코를 옮겼을 경우 조건 만족일 경우(옮겼는데 연속적일 때) return True
    # 아닐 경우(옮겼는데 연속적이지 않을 경우) return False 
   # False일 경우 switch_neko가 작동 안되게 해야됨


def game(): # 메인 게임 함수
    
    tmr = 0 # 시간 관리 변수
    # 마우스 클래스 부르기
    m = Mouse(cursor,map_y,map_x)
    while True:
        tmr += 1 # 매 시간 1초 증가
        for event in pygame.event.get(): # 윈도운 X 누를 시 나오게끔
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        idx = 0
        
        if idx == 0: # 딜레이 주면서 사진 보이기
            idx = check_neko(idx) #고양이를 7로 바꿔주기 
        elif 3 > idx >= 1 : #7(발바닥)을 보여줄시간
            idx += 1
        elif idx == 3 :
            sweep_neko() # 시간 도달 시 삭제
            idx = 0

        gameDisplay.blit(bg,(0,0))
        neko_draw()
        m.get_mouse()
        cursor_draw()
        sweep_neko()
        
        drop_neko()
        pygame.display.update()
        clock.tick(20)  

game()