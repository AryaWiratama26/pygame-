import pygame

# Init

pygame.init()
arena_lebar = 500
arena_tinggi = 500
window = pygame.display.set_mode((arena_lebar,arena_tinggi))

def draw_grid(surface):
    jumlah_baris = 10
    jumlah_kolom = 10
    jarak_baris = arena_lebar // jumlah_baris
    jarak_kolom = arena_tinggi // jumlah_kolom
    window.fill((255,255,255))
    for baris_ke in range(jumlah_baris):
        x = jarak_baris*baris_ke
        y = jarak_kolom*baris_ke
        pygame.draw.line(surface,(0,0,0),(x,0),(x,arena_tinggi))
        pygame.draw.line(surface,(0,0,0),(0,y),(arena_lebar,y))



isRun = True
while isRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    draw_grid(window)
    pygame.display.update()

pygame.quit()            

# Input

# Update

# Render