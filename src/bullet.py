import pygame as pg   
import math
import file_paths as fp 

class Bullet:
    def __init__(self,pos_x,pos_y,rotation):
        self.texture=pg.image.load(fp.bulletpath).convert_alpha()
        self.alive=True
        self.boom=False
        self.y_speed=0
        self.gravity=0.12
        self.l_speed=12
        self.x=pos_x
        self.y=pos_y
        self.r=rotation
        self.og_r=rotation
        self.draw_texture=pg.transform.rotate(self.texture,self.r)
    def update(self,terrain):
        if not self.alive:
            return False
        self.y_speed+=self.gravity
        self.x+=int(self.l_speed*math.cos(self.og_r*math.pi/180))
        self.y+=int(self.y_speed-(self.l_speed*math.sin(self.og_r*math.pi/180)))
        self.r=int(math.atan((self.l_speed*math.sin(self.og_r*math.pi/180)-self.y_speed)/(self.l_speed*math.cos(self.og_r*math.pi/180)))*(180/math.pi))
        self.draw_texture=pg.transform.rotate(self.texture,self.r)
        xoffset=self.draw_texture.get_rect().size[0]
        if self.r< -90:
            xoffset=-xoffset
        yoffset=self.draw_texture.get_rect().size[1]
        if(self.x+xoffset>1600 or self.x+xoffset<0):
            self.alive=False
            return str("OutOfBounds")
        elif(self.y+yoffset>=900-terrain.get_height(self.x+xoffset)): 
            terrain.boom(self.x)
            self.boom=True
            self.alive=False
        return self.alive
    def draw(self,screen):
        rect=self.draw_texture.get_rect()
        rect.center=(self.x,self.y)
        screen.blit(self.draw_texture,rect)
        
