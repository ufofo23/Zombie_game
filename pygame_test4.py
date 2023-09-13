import pygame
from pygame.locals import *

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
        for k in self.keys:
            if k.pick(*args):
                self.keys.remove(k)
                return True
        return None
    
pygame.init()

pygame.display.set_caption("Test04")
screen = pygame.display.set_mode((1280, 800))

clock = pygame.time.Clock()

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

# 배경
background = pygame.image.load("./pygame_project/zombie_project/zombiegame/png/BG.png").convert()
background = pygame.transform.scale(background, (1280, 800))

# 좀비
zombie_sprites = []
zombie_sprites_rev = []
for i in range(1, 10):
    img = pygame.image.load(f"./pygame_project/zombie_project/zombiegame/png/male/Walk ({i}).png").convert_alpha()
    w, h = img.get_size()
    img = pygame.transform.scale(img, (w // 4, h // 4))
    img = img.subsurface((4, 17, 88, 112))
    img_rev = pygame.transform.flip(img, True, False)
    zombie_sprites.append(img)
    zombie_sprites_rev.append(img_rev)
    zombie = img.get_rect().move(30, 500)
    zombie_rev = img_rev.get_rect().move(30, 500)
zombie_sprite_id = 0

# 좀비 점프
gravity = 2.0
zombie_vy = 0.0
zombie_vx = 0.0

#글자 출력
ending_font = pygame.font.SysFont("System", 200)

running = True
direct = True
while running:
    # 종료
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 배경색
    width, height = screen.get_size()
    screen.fill((255, 255, 255))

    # 배경 생성
    screen.blit(background, dest=(0, 0))

    # 타일 생성
    tiles_group.draw()
    blocks_group.draw()

    # 비석 생성
    tombs_group.draw()

    # 열쇠 생성
    keys_group.draw()

    # 열쇠 픽업
    keys_group.k(zombie)

    # 문 생성
    if len(keys_group.keys) == 0:
        gate3.draw()
    elif len(keys_group.keys) == 1:
        gate2.draw()
    else:
        gate1.draw()    
    
    # 좀비 생성
    zombie_sprite_id += 0.5
    zombie_sprite_id %= len(zombie_sprites)

    # 좀비 움직임
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        if zombie.left > 0:
            zombie_vx = -5
            zombie.x += zombie_vx
        direct = False

    elif keys[K_RIGHT]:
        if zombie.right < 1280:
            zombie_vx = 5
            zombie.x += zombie_vx
        direct = True

    if direct:
        screen.blit(zombie_sprites[int(zombie_sprite_id)], dest=zombie)
    else:
        screen.blit(zombie_sprites_rev[int(zombie_sprite_id)], dest=zombie)

    #클리어 스테이지
    if event.type == KEYDOWN and event.key == K_UP and gate3.collided(zombie) and len(keys_group.keys) == 0:
        happy_ending_text = ending_font.render("Stage Clear", 1, (0, 0, 0))
        screen.blit(happy_ending_text, (250, 330))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False
    
    if zombie.top > 800:
        sad_ending_text = ending_font.render("You Dead", 1, (255, 0, 0))
        screen.blit(sad_ending_text, (330, 330))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    #좀비 텔레포트
    if event.type == KEYDOWN and event.key == K_UP and tiles_group.c(zombie):
        tombs_group.t(zombie)
            
    # 좀비 중력 & 점프
    zombie_vy += gravity
    if ht := tiles_group.c(zombie):
        zombie_vy = 0
        zombie.y = ht.top - zombie.height + 1
        if pygame.key.get_pressed()[K_SPACE]:
            zombie_vy = -15

    if hb := blocks_group.c(zombie):
        zombie_vx = -zombie_vx
        zombie.x += zombie_vx   

    zombie.y += zombie_vy

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
