import pygame
pygame.init()

window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Pixel Art")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((30, 30, 30))  # dark gray background
    pygame.display.flip()

pygame.quit()


        
