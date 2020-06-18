import pygame as pg 
import tank as tk 
import file_paths as fp
import landscape as ld
import skybox as sb
import anim as a
import texts as t

screen_width=1600
screen_height=900

class Game:
    def __init__(self,screen):
        self.timeout=0
        self.freeze=False
        self.screen=screen
        self.next_player=0
        self.player1=tk.Tank1(0,0,self)
        self.player2=tk.Tank2(screen_width-50,0,self)
        self.skybox=sb.Skybox()
        self.terrain=ld.Landscape(0,600,1600)
        self.terrain.generate()
        self.terrain.update_texture()
        self.clock=pg.time.Clock()
        self.running=True
        self.players=[]
        self.players.append(self.player1)
        self.players.append(self.player2)
        self.bullets=[]
        self.anim=[]
        self.texts=[]
        self.drawable_objects=[]
        self.drawable_objects.append(self.skybox)
        self.drawable_objects.append(self.terrain)
        self.drawable_objects.append(self.player1)
        self.drawable_objects.append(self.player2)
    def update(self):
        pg.display.update()
        if self.players[0].active==False and self.players[1].active==False:
            self.players[self.next_player].toggle()
            self.next_player+=1
            self.next_player%=2
        for obj in self.players:
            obj.update(self.terrain)
            if obj.hp<=0:
                self.end(self.players.index(obj))
        for obj in self.bullets:
            if( obj.update(self.terrain)==False):
                if obj.boom:
                    self.anim.append(a.ExplosionAnim(obj.x))
                    if -77<(self.players[0].x-obj.x) and (self.players[0].x-obj.x)<20:
                        self.players[0].hp-=20
                    if -77<(self.players[1].x-obj.x) and (self.players[1].x-obj.x)<20:
                        self.players[1].hp-=20
                self.bullets.remove(obj)
        for obj in self.anim:
            if (not obj.update(self.terrain)):
                self.anim.remove(obj)
            
    def events(self):
        for event in pg.event.get():
            if event.type==pg.QUIT:
                self.running = False
            if not self.freeze:
                for obj in self.players:
                    obj.action(event)
    def draw(self):
        for obj in self.drawable_objects:
            obj.draw(self.screen)
        for obj in self.bullets:
            obj.draw(self.screen)
            self.anim.append(a.TraceAnim(obj.x,obj.y,obj.r))
        for obj in self.anim:
            obj.draw(self.screen)
    def run(self):
        while self.running:
            self.clock.tick(60)
            self.update()
            self.draw()
            self.events()
            if self.freeze:
                self.timeout+=1
            if self.timeout==180:
                self.running=False
    def end(self,looser):
        if looser==1:
            text=t.Message((0,94,255),"Blue Wins",(1600/2,900/2))
        if looser==0:
            text=t.Message((255,17,0),"Red Wins",(1600/2,900/2))
        self.drawable_objects.append(text)
        self.freeze=True

