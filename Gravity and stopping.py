import pygame,sys
import random
 
pygame.init()
clock = pygame.time.Clock()
FPS = 60


screen_width,screen_height = 600,600

screen = pygame.display.set_mode((screen_width, screen_height))
 
class Block(pygame.Rect):
 
    def __init__(self, x, y, width, height):
        super(Block, self).__init__(x, y, width, height) 
 
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255,0,0)
        self.dy, self.dx, self.gravity = 0, 2, 0.4
        self.speed = [random.random() * 5 - 2.5, random.random() * 5 - 2.5]
 
    def update(self):
        pygame.draw.rect(screen, self.color, self.rect)
        self.dy -= self.gravity 
        self.rect.y -= self.dy 
        self.rect.x += self.dx
 
        if self.rect.y > 550:
            self.dy *= -0.75
            if self.dy < 2:
                self.dy = 0
                self.dx = 0
 
        if self.rect.x > 550 or self.rect.x < 0:
            self.dx *= -1
 
blocks = []
for i in range(1):
    # x = random.randint(0, 600)
    # y = random.randint(0, 200)
    block = Block(100,100,50,50)
    blocks.append(block)
 
while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    for block in blocks: 
        block.update()     

    clock.tick(FPS)
    pygame.display.update()