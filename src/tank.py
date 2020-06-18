import pygame 
import anim as a
import bullet as b
import file_paths as fp
import math

class Tank:
    def __init__(self,pos_x,pos_y,game):
        self.game=game
        self.hp=100
        self.range=0
        self.active=False
        self.x=pos_x
        self.y=pos_y
        self.r=0
        self.r_speed=0
        self.x_speed=0
        self.muzzle=0
        self.ShotEffect=pygame.mixer.Sound("../assets/sounds/tankyShot.wav")
    def action(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x_speed=-0.25
            if event.key == pygame.K_RIGHT:
                self.x_speed=0.25
            if event.key == pygame.K_UP:
                self.r_speed=-0.25
            if event.key == pygame.K_DOWN:
                self.r_speed=0.25
            if event.key == pygame.K_SPACE:
                if self.active: 
                    self.shoot()
                    self.ShotEffect.play()
                    self.toggle()
        if event.type == pygame.KEYUP:
            if (not((pygame.key.get_pressed())[pygame.K_LEFT]) and not((pygame.key.get_pressed())[pygame.K_RIGHT])):
                self.x_speed=0
            if (not((pygame.key.get_pressed())[pygame.K_UP]) and not((pygame.key.get_pressed())[pygame.K_DOWN])):
                self.r_speed=0
    def toggle(self):
        if self.active:
            self.active=False
        else: 
            self.active=True
            self.range=400
    def shoot(self):
        return False

class Tank1(Tank):
    def __init__(self,pos_x,pos_y,game):
        Tank.__init__(self,pos_x,pos_y,game)
        self.Body=pygame.image.load(fp.tank1bodypath).convert_alpha()
        self.Gun_original=pygame.image.load(fp.tank1gunpath).convert_alpha()
        self.Gun=self.Gun_original
    def shoot(self):
        x=self.Gun.get_rect().size[0]
        y=self.Gun.get_rect().size[1]
        if self.r>0:
            y=-y
        self.game.bullets.append(b.Bullet(self.muzzle[0],self.muzzle[1],self.r))
        self.game.anim.append(a.ShotAnim(self.muzzle[0],self.muzzle[1],self.r))
    def update(self,terrain):
        self.y=900-terrain.get_height(self.x+28)-25
        if self.active == False:
            return
        nextx=self.x+self.x_speed
        if self.x_speed != 0 and self.range>0:
            self.range-=1
        if terrain.get_height(int(self.x+28+5*self.x_speed))-terrain.get_height(int(self.x+28))<5 and self.range>0:
            self.x=nextx
        self.r-=self.r_speed
        if self.r > 90:
            self.r+=self.r_speed
        if self.r < -20:
            self.r+=self.r_speed
        self.Gun=pygame.transform.rotate(self.Gun_original,self.r)
    def draw(self,screen):
        rect=self.Gun_original.get_rect()
        length=rect.size[0]/2
        rect=self.Gun.get_rect()
        self.muzzle=(int(self.x+41+math.cos(self.r*math.pi/180)*length*2),int(self.y+7-math.sin(self.r*math.pi/180)*length*2))
        rect.center=(int(self.x+41+math.cos(self.r*math.pi/180)*length),int(self.y+7-math.sin(self.r*math.pi/180)*length))
        screen.blit(self.Gun,rect)
        screen.blit(self.Body,(int(self.x),self.y))
        pygame.draw.rect(screen,(163,150,0),pygame.Rect(self.x,self.y-25,self.Body.get_rect().size[0],5))
        pygame.draw.rect(screen,(50,117,26),pygame.Rect(self.x,self.y-20,self.Body.get_rect().size[0],5))
        if self.range>0: 
            pygame.draw.rect(screen,(255,234,0),pygame.Rect(self.x,self.y-25,self.Body.get_rect().size[0]*self.range/400,5))
        if self.hp>0:
            pygame.draw.rect(screen,(100,235,52),pygame.Rect(self.x,self.y-20,self.Body.get_rect().size[0]*self.hp/100,5))

class Tank2(Tank):
    def __init__(self,pos_x,pos_y,game):
        Tank.__init__(self,pos_x,pos_y,game)
        self.Body=pygame.image.load(fp.tank2bodypath).convert_alpha()
        self.Gun_original=pygame.image.load(fp.tank2gunpath).convert_alpha()
        self.Gun=self.Gun_original
    def shoot(self):
        x=self.Gun.get_rect().size[0]
        y=self.Gun.get_rect().size[1]
        if self.r>0:
            y=-y
        self.game.bullets.append(b.Bullet(self.muzzle[0],self.muzzle[1],self.r-180))
        self.game.anim.append(a.ShotAnim(self.muzzle[0],self.muzzle[1],self.r-180))
    def update(self,terrain):
        self.y=900-terrain.get_height(self.x+28)-25
        if self.active == False:
            return
        nextx=self.x+self.x_speed
        if self.x_speed != 0 and self.range>0:
            self.range-=1
        if terrain.get_height(int(self.x+28+5*self.x_speed))-terrain.get_height(int(self.x+28))<5 and self.range>0:
            self.x=nextx
        self.r+=self.r_speed
        if self.r > 20:
            self.r-=self.r_speed
        if self.r < -90:
            self.r-=self.r_speed
        self.Gun=pygame.transform.rotate(self.Gun_original,self.r)
    def draw(self,screen):
        rect=self.Gun_original.get_rect()
        length=rect.size[0]/2
        rect=self.Gun.get_rect()
        self.muzzle=(int(self.x+14+math.cos((180+self.r)*math.pi/180)*length*2),int(self.y+7-math.sin((180+self.r)*math.pi/180)*length*2))
        rect.center=(int(self.x+14+math.cos((180+self.r)*math.pi/180)*length),int(self.y+7-math.sin((180+self.r)*math.pi/180)*length))
        screen.blit(self.Gun,rect)
        screen.blit(self.Body,(int(self.x),self.y))
        pygame.draw.rect(screen,(163,150,0),pygame.Rect(self.x,self.y-25,self.Body.get_rect().size[0],5))
        pygame.draw.rect(screen,(50,117,26),pygame.Rect(self.x,self.y-20,self.Body.get_rect().size[0],5))
        if self.range>0: 
            pygame.draw.rect(screen,(255,234,0),pygame.Rect(self.x,self.y-25,self.Body.get_rect().size[0]*self.range/400,5))
        if self.hp>0:
            pygame.draw.rect(screen,(100,235,52),pygame.Rect(self.x,self.y-20,self.Body.get_rect().size[0]*self.hp/100,5))