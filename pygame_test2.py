import pygame
from pygame.locals import *

class Tiles:
    def __init__(self, left, top, width, height, kda_tile):
        self.kda_tile = kda_tile

        Tiles.img_src = pygame.image.load(
            f"C:\\Users\\Gwan\\Desktop\\zombiegame\\png\\Tiles\\Tile ({self.kda_tile}).png"
        ).convert_alpha()
        Tiles.img_src = pygame.transform.scale(
            Tiles.img_src, (50, 50)
        )

        self.image = Tiles.img_src
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)

    def draw(self):
        for i in range(self.width//50):
            for j in range(self.height//50):
                screen.blit(self.image, dest=(self.left + i*50, self.top + j*50))

    def collided(self, character):
        return self.rect.colliderect(character)

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
            if t.collided(*args) : 
                return True
        return False
        
        
pygame.init()

pygame.display.set_caption('Test02')
screen = pygame.display.set_mode((1280, 800))
zombie = pygame.Rect(0, 0, 50, 50)

zombie.center = 25, 615

clock = pygame.time.Clock()

tiles_group = TilesGroup()

#타일 지정
tiles_group.add(Tiles(0, 150, 350, 50, 15)) # 왼쪽 위
tiles_group.add(Tiles(350, 150, 50, 50, 16))
tiles_group.add(Tiles(930, 150, 350, 50, 15)) # 오른쪽 위
tiles_group.add(Tiles(880, 150, 50, 50, 14))
tiles_group.add(Tiles(0, 650, 450, 50, 2)) # 왼쪽 아래
tiles_group.add(Tiles(0, 700, 450, 100, 5))
tiles_group.add(Tiles(450, 650, 50, 50, 3))
tiles_group.add(Tiles(450, 700, 50, 100, 6))  
tiles_group.add(Tiles(830, 650, 450, 50, 2)) # 오른쪽 아래
tiles_group.add(Tiles(830, 700, 450, 100, 5))
tiles_group.add(Tiles(780, 650, 50, 50, 1))
tiles_group.add(Tiles(780, 700, 50, 100, 4))
tiles_group.add(Tiles(615, 0, 50, 350, 17)) # 가운데 세로
tiles_group.add(Tiles(565, 350, 150, 50, 15)) # 가운데 가로
tiles_group.add(Tiles(715, 350, 50, 50, 16))
tiles_group.add(Tiles(515, 350, 50, 50, 14))


running = True
while running:
    #종료
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 배경색
    width, height = screen.get_size()
    screen.fill((255, 255, 255))

    #타일 생성
    tiles_group.draw()
    
    #캐릭터 생성
    pygame.draw.rect(screen, (0, 255, 0), zombie)

    # 캐릭터 움직임
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        tiles_group.c(zombie)
        if zombie.left > 0:
            zombie = zombie.move(-5, 0)
            if tiles_group.c(zombie):
                zombie = zombie.move(5, 0)
    if keys[K_RIGHT]:
        if zombie.right < 1280:
            zombie = zombie.move(5, 0)
            if tiles_group.c(zombie):
                zombie = zombie.move(-5, 0)
    if keys[K_DOWN]:
        if zombie.bottom < 800:
            zombie = zombie.move(0, 5)
            if tiles_group.c(zombie):
                zombie = zombie.move(0, -5)
    if keys[K_UP]:
        if zombie.top > 0:
            zombie = zombie.move(0, -5)
            if tiles_group.c(zombie):
                zombie = zombie.move(0, 5)

    pygame.display.flip()
  
    clock.tick(30)

pygame.quit()
