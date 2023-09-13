import pygame

class Player():
    def __init__(self, x, y, vx=0, vy=0):
        self.vx = vx
        self.vy = vy
        self.vel = 5

        self.zombie_sprites = []
        self.zombie_sprites_rev = []
        for i in range(1, 10):
            self.img = pygame.image.load(
                f"./pygame_project/zombie_project/zombiegame/png/male/Walk ({i}).png"
            ).convert_alpha()
            w, h = self.img.get_size()
            self.img = pygame.transform.scale(self.img, (w // 4, h // 4))
            self.img = self.img.subsurface((4, 17, 88, 112))
            self.img_rev = pygame.transform.flip(self.img, True, False)
            self.zombie_sprites.append(self.img)
            self.zombie_sprites_rev.append(self.img_rev)
            self.zombie = self.img.get_rect().move(30, 500)
            self.zombie.x = x
            self.zombie.y = y
            self.zombie_rev = self.img_rev.get_rect().move(30, 500)
        self.zombie_sprite_id = 0
        self.direct = True

    def draw(self, screen):
        self.zombie_sprite_id += 0.5
        self.zombie_sprite_id %= len(self.zombie_sprites)
        
        if self.direct:
            screen.blit(self.zombie_sprites[int(self.zombie_sprite_id)], dest=self.zombie)
        else:
            screen.blit(self.zombie_sprites_rev[int(self.zombie_sprite_id)], dest=self.zombie)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if self.zombie.left > 0:
                self.vx = -self.vel
            self.direct = False
        if keys[pygame.K_RIGHT]:
            if self.zombie.right < 1280:
                self.vx = self.vel
            self.direct = True
        self.update()

    def update(self):
        self.zombie.x += self.vx

    def inform(self):
        return (self.zombie.x, self.zombie.y, self.direct)