import pygame as pg
import file_paths as fp

screen_width=1600
screen_height=900


class HelpMenu:
    def __init__(self,screen):
        self.running=True
        self.screen=screen
        self.HelpScreenTexture=pg.image.load(fp.HelpScreenPath).convert_alpha()
    def run(self):
        while self.running:
            pg.display.update()
            self.events()
            self.draw(self.screen)
    def events(self):
            for event in pg.event.get():
                if event.type==pg.KEYDOWN:
                    self.running = False
                if event.type==pg.QUIT:
                    self.running = False
    def draw(self,screen):
        screen.blit(self.HelpScreenTexture,(0,0))

