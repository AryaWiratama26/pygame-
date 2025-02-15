import pygame
from Game import Arena
# Init


arena_lebar = 500
arena_tinggi = 500
arena = Arena(500,500,20,20)



isRun = True
while isRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    
    arena.render()
    

pygame.quit()            

# Input

# Update

# Render