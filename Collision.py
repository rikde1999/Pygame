import pygame

pygame.init()

screen_width,screen_height = 800,700
screen = pygame.display.set_mode((screen_width,screen_height))

moving_rect = pygame.Rect(200,300,100,100)
x_speed,y_speed = 4,4

other_rect = pygame.Rect(150,150,200,100)
other_speed = 2
clock = pygame.time.Clock()
def bouncing_Rect():
    global x_speed,y_speed,other_speed
    moving_rect.x += x_speed
    moving_rect.y += y_speed

    if moving_rect.right >= screen_width or moving_rect.left <= 0:
        x_speed *= -1

    if moving_rect.bottom >= screen_height or moving_rect.top <= 0:
        y_speed *= -1
    
    other_rect.y += other_speed
    if other_rect.top <= 0 or other_rect.bottom >= screen_height:
        other_speed *= -1

    collision_tollerance = 20
    if moving_rect.colliderect(other_rect):
        print("collision")
        if abs(other_rect.top - moving_rect.bottom) < collision_tollerance and y_speed > 0:
            y_speed *= -1
        if abs(other_rect.bottom - moving_rect.top) < collision_tollerance and y_speed < 0:
            y_speed *= -1
        if abs(other_rect.right - moving_rect.left) < collision_tollerance and x_speed < 0:
            x_speed *= -1
        if abs(other_rect.left - moving_rect.right) < collision_tollerance and x_speed > 0:
            x_speed *= -1

while True:
    screen.fill((30,30,30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.draw.rect(screen,(255,255,255),moving_rect)
    pygame.draw.rect(screen,(255,0,0),other_rect)

    bouncing_Rect()
    pygame.display.update()
    clock.tick(60)