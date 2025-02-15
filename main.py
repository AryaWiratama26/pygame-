import pygame
from Game import Arena, Kotak
# Init


arena_lebar = 500
arena_tinggi = 500
arena = Arena(500,500,20,20)

kepala = Kotak((100,100))

isRun = True
while isRun:
    # Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    # Update
    keys = pygame.key.get_pressed()
    for key in keys:
        if keys[pygame.K_RIGHT]:
            kepala.move(1,0)

    
    # Render
    arena.render(100)
    

pygame.quit()            


