import pygame as pg

class Message:
    def __init__(self,color,text,rect):
        self.MainFont=pg.font.Font("../fonts/kremlin.ttf",64)
        self.text=self.MainFont.render(text,True,color)
        self.textRect=self.text.get_rect()
        self.textRect.center=rect
    def draw(self,screen):
        pg.draw.rect(screen,(0,0,0),self.textRect)
        screen.blit(self.text,self.textRect)