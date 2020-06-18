import pygame as pg
import file_paths as fp

class Skybox:
    def __init__(self):
        self.texture=pg.image.load(fp.skypath).convert()
    def draw(self,screen):
        screen.blit(self.texture,(0,0))