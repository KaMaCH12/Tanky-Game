import pygame as pg
import file_paths as fp

screen_width=1600
screen_height=900


class MainMenu:
    def __init__(self,screen):
        self.BtnEffect=pg.mixer.Sound(fp.btneffect)
        self.running=True
        self.screen=screen
        self.TitleScreenTexture=pg.image.load(fp.TitleScreenPath).convert_alpha()
        self.StartBtnTexture=pg.image.load(fp.StartBtnPath).convert_alpha()
        self.HelpBtnTexture=pg.image.load(fp.HelpBtnPath).convert_alpha()
        self.Startrect=self.StartBtnTexture.get_rect()
        self.Startrect.center=(screen_width/2+screen_width/4-50,screen_height/2-20)
        self.Helprect=self.HelpBtnTexture.get_rect()
        self.Helprect.center=(screen_width/2+screen_width/4-50,screen_height/2+self.Helprect.h)
        self.return_val=0
    def run(self):
        while self.running:
            pg.display.update()
            self.events()
            self.draw(self.screen)
    def events(self):
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    self.running = False
                if event.type==pg.KEYDOWN:
                    if event.key==pg.K_SPACE:
                        self.running = False
                        self.return_val=1
                if event.type==pg.MOUSEBUTTONDOWN:
                    if event.button==1:
                        if self.Startrect.collidepoint(event.pos):
                            self.BtnEffect.play()
                            self.running = False
                            self.return_val=1
                        if self.Helprect.collidepoint(event.pos):
                            self.BtnEffect.play()
                            self.running = False
                            self.return_val=2

    def draw(self,screen):
        screen.blit(self.TitleScreenTexture,(0,0))
        screen.blit(self.StartBtnTexture,self.Startrect)
        screen.blit(self.HelpBtnTexture,self.Helprect)

