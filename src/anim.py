import pygame as pg
import file_paths as fp

class Anim:
    ShotFrames=[]
    ShotFrames.append(pg.image.load(fp.shot1))
    ShotFrames.append(pg.image.load(fp.shot2))
    ShotFrames.append(pg.image.load(fp.shot3))
    ShotFrames.append(pg.image.load(fp.shot4))
    ExpFrames=[]
    ExpFrames.append(pg.image.load(fp.explosion1))
    ExpFrames.append(pg.image.load(fp.explosion2))
    ExpFrames.append(pg.image.load(fp.explosion3))
    ExpFrames.append(pg.image.load(fp.explosion4))
    ExpFrames.append(pg.image.load(fp.explosion5))
    ExpFrames.append(pg.image.load(fp.explosion6))
    ExpFrames.append(pg.image.load(fp.explosion7))
    ExpFrames.append(pg.image.load(fp.explosion8))
    TraceFrames=[]
    TraceFrames.append(pg.image.load(fp.trace1))
    TraceFrames.append(pg.image.load(fp.trace2))
    TraceFrames.append(pg.image.load(fp.trace3))
    TraceFrames.append(pg.image.load(fp.trace4))
    TraceFrames.append(pg.image.load(fp.trace5))
    def __init__(self,pos_x,pos_y,rotation):
        self.x=pos_x
        self.y=pos_y
        self.r=rotation
        self.frame=0
        self.texture=0

class ExplosionAnim(Anim):
    def __init__(self,pos_x):
        Anim.__init__(self,pos_x,0,0)
        self.texture=Anim.ExpFrames[int(self.frame)]
    def update(self,terrain):
        self.texture=Anim.ExpFrames[int(self.frame)]
        if self.frame==0:
            self.y=900-terrain.get_height(self.x)
        self.frame+=0.3
        if(int(self.frame)>len(Anim.ExpFrames)-1): 
            self.frame-=0.3
            return False
        return True
    def draw(self,screen):
        screen.blit(self.texture,(self.x-55,self.y-123))
class ShotAnim(Anim):
    def __init__(self,pos_x,pos_y,rotation):
        Anim.__init__(self,pos_x,pos_y,rotation)
        self.texture=Anim.ShotFrames[int(self.frame)]
    def update(self,terrain):
        self.texture=Anim.ShotFrames[int(self.frame)]
        self.frame+=0.3
        if(int(self.frame)>len(Anim.ShotFrames)-1): 
            self.frame-=0.3
            return False
        return True
    def draw(self,screen):
        drawable=pg.transform.rotate(self.texture,self.r)
        rect=drawable.get_rect()
        rect.center=(self.x,self.y)
        screen.blit(drawable,rect)

class TraceAnim(Anim):
    def __init__(self,pos_x,pos_y,rotation):
        Anim.__init__(self,pos_x,pos_y,rotation)
        self.texture=Anim.TraceFrames[int(self.frame)]
    def update(self,terrain):
        self.texture=Anim.TraceFrames[int(self.frame)]
        self.frame+=0.3
        if(int(self.frame)>len(Anim.TraceFrames)-1): 
            self.frame-=0.3
            return False
        return True
    def draw(self,screen):
        drawable=pg.transform.rotate(self.texture,self.r)
        rect=drawable.get_rect()
        rect.center=(self.x,self.y)
        screen.blit(drawable,rect)
                
