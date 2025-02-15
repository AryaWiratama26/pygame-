import pygame


class Kotak:
    
    def __init__(self,pos_awal,arah_x = 1,arah_y = 1,warna=(0,0,255)):
        self.pos = pos_awal
        self.arah_x = arah_x # Arah positif kanan
        self.arah_y = arah_y # Arah positif bawah
        self.warna = warna
        
    def move(self, arah_x, arah_y):
        self.arah_x = arah_x
        self.arah_y = arah_y
        self.pos = (self.pos[0] + self.arah_x, self.pos[1] + self.arah_y)
        print(self.pos)