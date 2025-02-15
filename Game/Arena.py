import pygame

class Arena:
    def __init__(self,arena_lebar, arena_tinggi, jumlah_baris, jumlah_kolom):
        pygame.init()
        self.arena_lebar = arena_lebar
        self.arena_tinggi = arena_tinggi
        self.jumlah_baris = jumlah_baris
        self.jumlah_kolom = jumlah_kolom
        self.surface = pygame.display.set_mode((self.arena_lebar,self.arena_tinggi))

    def draw_grid(self):
        jarak_baris = self.arena_lebar // self.jumlah_baris
        jarak_kolom = self.arena_tinggi // self.jumlah_kolom
        for baris_ke in range(self.jumlah_baris):
            x = jarak_baris*baris_ke
            y = jarak_kolom*baris_ke
            pygame.draw.line(self.surface,(0,0,0),(x,0),(x,self.arena_tinggi))
            pygame.draw.line(self.surface,(0,0,0),(0,y),(self.arena_lebar,y))
            
    def render(self):
        self.surface.fill((255,255,255))
        self.draw_grid()
        pygame.display.update()

