import pygame
import sys
import random


pygame.init()


WIDTH, HEIGHT = 800, 800
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)

surface = pygame.display.set_mode([800, 800])
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clicker Game")


font = pygame.font.Font(None, 36)
background_image = pygame.image.load('45.jpg')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

score = 0
targets = []
target_radius = 20
target_speed = 5
clock = pygame.time.Clock()
running = True

def create_target():
    x = random.randint(target_radius, WIDTH - target_radius)
    y = random.randint(target_radius, HEIGHT - target_radius)
    return x, y

def draw_targets():
    for target in targets:
        pygame.draw.circle(screen, RED, target, target_radius)

while running:
    surface.blit(background_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            for target in targets:
                if pygame.math.Vector2(target).distance_to(pygame.math.Vector2(event.pos)) <= target_radius:
                    score += 1
                    targets.remove(target)
       
        if event.type==pygame.QUIT:
            running=False
            

    
    screen.fill(WHITE)

    
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    
    draw_targets()
    for i in range(len(targets)):
        targets[i] = (targets[i][0], targets[i][1] + target_speed)

    
    if random.random() < 0.01:  #
        targets.append(create_target())

    
    targets = [target for target in targets if target[1] - target_radius < HEIGHT]

    
    pygame.display.flip()

    
    clock.tick(FPS)


pygame.quit()
sys.exit()