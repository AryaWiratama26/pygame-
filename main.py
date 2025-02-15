import pygame

# Init

pygame.init()
arena_lebar = 200
arena_tinggi = 200

pygame.display.set_mode((arena_lebar,arena_tinggi))

isRun = True
while isRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

# Input

# Update

# Render