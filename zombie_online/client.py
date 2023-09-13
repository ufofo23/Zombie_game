import pygame
from pygame.locals import *
from network import Network
from player import Player

class Tiles:
    def __init__(self, left, top, width, height, kda_tile):
        self.kda_tile = kda_tile

        Tiles.img_src = pygame.image.load(
            f"./pygame_project/zombie_project/zombiegame/png/Tiles/Tile ({self.kda_tile}).png"
        ).convert_alpha()
        Tiles.img_src = pygame.transform.scale(Tiles.img_src, (50, 50))
        self.image = Tiles.img_src
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)

    def draw(self):
        for i in range(self.width // 50):
            for j in range(self.height // 50):
                screen.blit(self.image, dest=(self.left + i * 50, self.top + j * 50))

    def collided(self, character):
        if self.rect.collidepoint(character.centerx, character.bottom):
            return 0
        
class TilesGroup:
    def __init__(self):
        self.tiles = []

    def add(self, tile):
        self.tiles.append(tile)

    def draw(self, *args):
        for t in self.tiles:
            t.draw(*args)

    def c(self, *args):
        for t in self.tiles:
            if t.collided(*args) == 0:
                return t
        return None
    
class Blocks:
    def __init__(self, left, top, width, height, kda_block):
        self.kda_block = kda_block

        Blocks.img_src = pygame.image.load(
            f"./pygame_project/zombie_project/zombiegame/png/Tiles/Tile ({self.kda_block}).png"
        ).convert_alpha()
        Blocks.img_src = pygame.transform.scale(Blocks.img_src, (50, 50))
        self.image = Blocks.img_src
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)

    def draw(self):
        for i in range(self.width // 50):
            for j in range(self.height // 50):
                screen.blit(self.image, dest=(self.left + i * 50, self.top + j * 50))

    def collided(self, character):
        if self.rect.colliderect(character):
            return 0
        
class BlocksGroup:
    def __init__(self):
        self.blocks = []

    def add(self, block):
        self.blocks.append(block)

    def draw(self, *args):
        for t in self.blocks:
            t.draw(*args)

    def c(self, *args):
        for b in self.blocks:
            if b.collided(*args) == 0:
                return b
        return None
    
class Tombs:
    def __init__(self, left, top, kda_tomb):
        self.kda_tomb = kda_tomb
        Tombs.img_src = pygame.image.load(
            f"./pygame_project/zombie_project/zombiegame/png/Objects/TombStone ({self.kda_tomb}).png"
        ).convert_alpha()
        Tombs.img_src = pygame.transform.scale(Tombs.img_src, (70, 70))
        self.image = Tombs.img_src
        self.left = left
        self.top = top
        self.rect = pygame.Rect(self.left, self.top, 70, 70)

    def draw(self):
        screen.blit(self.image, dest=(self.left, self.top))

    def tel(self, character):
        if self.rect.colliderect(character):
            return self.rect.colliderect(character)
        return None
    
class TombsGroup:
    def __init__(self):
        self.tombs = {}
    
    def add(self, num, tomb):
        self.tombs[f"{num}"] = tomb

    def draw(self, *args):
        for t in range(len(self.tombs)):
            self.tombs[f"{t+1}"].draw(*args)
    
    def t(self, character):
        for t in range(len(self.tombs)):
            if self.tombs[f"{t+1}"].tel(character):
                if (t+1) % 2 == 0:
                    character.center = (self.tombs[str(t)].rect.centerx, self.tombs[str(t)].rect.centery - 50)
                elif (t+1) % 2 == 1:
                    character.center = (self.tombs[str(t+2)].rect.centerx, self.tombs[str(t+2)].rect.centery - 50)
                return character.center
        return None
    
class Door:
    def __init__(self, left, top, width, height, kda_doorx, kda_doory):
        self.kda_doorx = kda_doorx
        self.kda_doory = kda_doory
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        Door.img_src = pygame.image.load(
            "./pygame_project/zombie_project/zombiegame/stone_gate.png"
        ).convert_alpha()
        Door.img_src = Door.img_src.subsurface((self.kda_doorx * 160, self.kda_doory * 160, 160, 160))
        # Door.img_src = pygame.transform.scale(Door.img_src, (self.width, self.height))
        self.image = Door.img_src
        self.rect = pygame.Rect((self.left, self.top, self.width, self.height))

    def draw(self):
        screen.blit(self.image, dest=(self.left, self.top))

    def collided(self, character):
        if self.rect.colliderect(character):
            return True

class Key:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        Key.img_src = pygame.image.load(
            "./pygame_project/zombie_project/zombiegame/key.png"
        ).convert_alpha()
        # key_img = pygame.transform.scale(key_img, (self.width, self.height))
        self.image = Key.img_src
        self.rect = pygame.Rect((self.left, self.top, self.width, self.height))

    def draw(self):
        screen.blit(self.image, dest=(self.left, self.top))

    def pick(self, character):
        if self.rect.colliderect(character):
            return True

class KeysGroup:
    def __init__(self):
        self.keys = []

    def add(self, key):
        self.keys.append(key)

    def draw(self, *args):
        for k in self.keys:
            k.draw(*args)

    def k(self, *args):
        global key_exist
        num = -1
        for k in self.keys:
            num += 1
            if k.pick(*args):
                key_exist[num] = 0
                return True
        return None
    
def redrawWindow(screen,p,p2):
    p.draw(screen)
    p2.draw(screen)

    pygame.display.update()

#파이게임 초기화
pygame.init()

width = 1280
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
clock = pygame.time.Clock()

#그룹 인스턴스
tiles_group = TilesGroup()
blocks_group = BlocksGroup()
tombs_group = TombsGroup()
keys_group = KeysGroup()

# 타일 지정
tiles_group.add(Tiles(0, 150, 350, 50, 15))  # 왼쪽 위
tiles_group.add(Tiles(350, 150, 50, 50, 16))
tiles_group.add(Tiles(930, 150, 350, 50, 15))  # 오른쪽 위
tiles_group.add(Tiles(880, 150, 50, 50, 14))
tiles_group.add(Tiles(0, 650, 450, 50, 2))  # 왼쪽 아래
tiles_group.add(Tiles(0, 700, 450, 100, 5))
tiles_group.add(Tiles(450, 650, 50, 50, 3))
tiles_group.add(Tiles(450, 700, 50, 100, 6))
tiles_group.add(Tiles(150, 685, 50, 50, 18))
tiles_group.add(Tiles(300, 705, 50, 50, 20))
tiles_group.add(Tiles(830, 650, 450, 50, 2))  # 오른쪽 아래
tiles_group.add(Tiles(830, 700, 450, 100, 5))
tiles_group.add(Tiles(780, 650, 50, 50, 1))
tiles_group.add(Tiles(780, 700, 50, 100, 4))
tiles_group.add(Tiles(1000, 750, 50, 50, 19))
tiles_group.add(Tiles(1100, 685, 50, 50, 20))
tiles_group.add(Tiles(900, 690, 50, 50, 21))
blocks_group.add(Blocks(615, 0, 50, 350, 17))  # 가운데 세로
tiles_group.add(Tiles(565, 350, 150, 50, 15))  # 가운데 가로
tiles_group.add(Tiles(715, 350, 50, 50, 16))
tiles_group.add(Tiles(515, 350, 50, 50, 14))

# 비석
tombs_group.add(1, Tombs(400, 580, 2))
tombs_group.add(2, Tombs(1190, 80, 2))
tombs_group.add(3, Tombs(20, 80, 1))
tombs_group.add(4, Tombs(810, 580, 1))

# 문
gate1 = Door(1130, 520, 160, 160, 3, 2)
gate2 = Door(1130, 520, 160, 160, 1, 0)
gate3 = Door(1130, 520, 160, 160, 3, 3)

# 열쇠
keys_group.add(Key(555, 300, 50, 50))
keys_group.add(Key(675, 300, 50, 50))
key_exist = [1, 1]


# 배경
background = pygame.image.load("./pygame_project/zombie_project/zombiegame/png/BG.png").convert()
background = pygame.transform.scale(background, (1280, 800))

# 좀비 중력
gravity = 2.0
zombie_vy = 0.0
zombie_vx = 0.0

# 글자 출력
ending_font = pygame.font.SysFont("comicsans", 200)

def main():
    screen.fill((128, 128, 128))
    font = pygame.font.SysFont("comicsans", 60)
    text = font.render("Waiting for opponents...", 1, (255,0,0))
    screen.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    pygame.display.update()

    run = True
    n = Network()
    startPos = n.getP()
    print("Completed connection")
    print(startPos)
    p = Player(startPos[0], startPos[1])
    p2 = Player(startPos[0], startPos[1])

    while run:
        # 배경 생성
        screen.blit(background, dest=(0, 0))

        # 타일 생성
        tiles_group.draw()
        blocks_group.draw()

        # 비석 생성
        tombs_group.draw()
        
        # 열쇠 생성
        global key_exist
        print(key_exist)
        # for _ in range(len(keys_group.keys)):
        #     key_exist.append(1)

        for k in range(len(keys_group.keys)):
            if key_exist[k] == 1:
                keys_group.keys[k].draw()

        # 열쇠 픽업
        keys_group.k(p.zombie)

        # 문 생성
        if not 1 in key_exist:
            gate3.draw()
        elif 1 in key_exist and 0 in key_exist:
            gate2.draw()
        else:
            gate1.draw()

        # 좀비 중력 & 점프
        p.vy += gravity
        if ht := tiles_group.c(p.zombie):
            p.vy = 0
            p.zombie.y = ht.top - p.zombie.height + 1
            if pygame.key.get_pressed()[K_SPACE]:
                p.vy = -15

        if blocks_group.c(p.zombie):
            p.vx = -p.vx
            p.zombie.x += p.vx

        p.zombie.y += p.vy

        #좀비 텔레포트
        if pygame.key.get_pressed()[K_UP] and tiles_group.c(p.zombie):
            tombs_group.t(p.zombie)

        startPos = n.send(p.inform())
        p2.zombie.x = startPos[0]
        p2.zombie.y = startPos[1]
        p2.direct = startPos[2]

        p.vx = 0
        p2.vx = 0
        p2.update()

        #열쇠 IO
        key_exist = n.send(key_exist)

        #클리어 스테이지
        if p2.zombie.x > 1280:
            happy_ending_text = ending_font.render("Stage Clear", 1, (0, 0, 0))
            screen.blit(happy_ending_text, (width/2 - happy_ending_text.get_width()/2, height/2 - happy_ending_text.get_height()/2))
            pygame.display.flip()
            pygame.time.wait(3000)
            run = False
            pygame.quit()
            
        if not 1 in key_exist:
            if event.type == KEYDOWN and event.key == K_UP and gate3.collided(p.zombie):
                happy_ending_text = ending_font.render("Stage Clear", 1, (0, 0, 0))
                screen.blit(happy_ending_text, (width/2 - happy_ending_text.get_width()/2, height/2 - happy_ending_text.get_height()/2))
                pygame.display.flip()
                p.zombie.x = 1300
                n.send(p.inform())
                pygame.time.wait(3000)
                run = False
                pygame.quit()

        # 클리어 실패
        if p.zombie.y > 800 or p2.zombie.y > 800:
            sad_ending_text = ending_font.render("You Dead", 1, (255, 0, 0 ))
            screen.blit(sad_ending_text, (width/2 - sad_ending_text.get_width()/2, height/2 - sad_ending_text.get_height()/2))
            pygame.display.flip()
            pygame.time.wait(3000)
            run = False
            pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(screen, p, p2)

        pygame.display.flip()

        clock.tick(30)


def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        screen.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play!", 1, (255,0,0))
        screen.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_width()/2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
    while True:    
        main()


menu_screen()