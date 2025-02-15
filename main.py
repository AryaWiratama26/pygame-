import pygame

# Init

pygame.init()
arena_lebar = 500
arena_tinggi = 500
window = pygame.display.set_mode((arena_lebar,arena_tinggi))


isRun = True
while isRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    window.fill((255,255,255))
    pygame.display.update()

pygame.quit()            

# Input

# Update

# Render