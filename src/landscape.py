import pygame
import random,math
from PIL import Image,ImageDraw
import file_paths as fp

class Landscape:
    def __init__(self, min_height, max_height, total_points):
        self.min_height=min_height
        self.max_height=max_height
        self.total_points=total_points+1
        self.grid_size=1600/total_points
        self.height_map=[]
        self.BoomEffect=pygame.mixer.Sound("../assets/sounds/tankyBoom.wav")
    def generate(self):
        self.height_map=[]
        last_x=0
        last_height=(self.max_height + self.min_height)/2
        self.height_map.append(last_height)
        direction=1
        run_length=0
        for n in range(1,self.total_points):
            rand_dist=int(random.randint(0,100)/70)*direction
            height=last_height+rand_dist
            self.height_map.append(int(height))
            if height<self.min_height: direction=-1
            elif height>self.max_height: direction=1
            last_height=height
            if run_length<=0:
                run_length=random.randint(1,100)
                direction=random.randint(1,2)
                if direction==2: direction=-1
            else:
                run_length-=1
        
        #check if proper
        avg_height=(self.min_height+self.max_height)/2
        if self.height_map[0]>self.height_map[self.total_points-1]+100 or self.height_map[0]<self.height_map[self.total_points-1]-100:
            self.generate()

    def get_height(self,x):
        x_point=int(x/self.grid_size)
        return self.height_map[x_point]
    
    def set_height(self,x,height):
        x_point=int(x/self.grid_size)
        self.height_map[x_point]=height

    def boom(self,x):
        self.BoomEffect.play()
        r=50
        h=self.get_height(int(x))
        for pos in range(int(x)-r,int(x)+r):
            if pos>0 and pos<1600:
                dy=math.cos(math.asin((pos-int(x))/r))*r
                if h-dy<20:
                    self.set_height(pos,20)
                elif self.get_height(pos)>h-dy:
                    self.set_height(pos,h-dy)
        self.update_texture_part(x,r,h)
    
    def update_texture(self):
        last_x=0
        texture=Image.open(fp.Landscapepath)
        texture=texture.crop((0,0,1600,900))
        mask=Image.new("L",texture.size,0)
        im2=Image.new("RGBA",texture.size,(0,0,0,0))
        for n in range(0,self.total_points):
            height=self.height_map[n]
            x_pos=int(n*self.grid_size)
            pos=(x_pos,height)
            ImageDraw.Draw(mask).rectangle(((x_pos,900-height),(x_pos+self.grid_size,900)),fill=255)
            last_x=x_pos 
    
        texture=Image.composite(texture,im2,mask)
        texture.save(fp.modifiedlandscape,"PNG")
        self.texture=pygame.image.load(fp.modifiedlandscape).convert_alpha()
    def update_texture_part(self,x,r,h):
        last_x=0
        strFormat='RGBA'
        raw_str=pygame.image.tostring(self.texture,strFormat,False)
        texture=Image.frombytes(strFormat,self.texture.get_size(),raw_str)
        mask=Image.new("L",texture.size,255)
        im2=Image.new("RGBA",texture.size,(0,0,0,0))
        ImageDraw.Draw(mask).rectangle(((x-r,0),(x+r,900-h)),fill=0)
        ImageDraw.Draw(mask).ellipse(((x-r,900-h-r),(x+r,900-h+r)),fill=0)
        ImageDraw.Draw(mask).rectangle(((x-r,900-20),(x+r,900)),fill=255)
        texture=Image.composite(texture,im2,mask)
        raw_str=texture.tobytes("raw",strFormat)
        self.texture=pygame.image.fromstring(raw_str, texture.size, strFormat).convert_alpha()

    def draw(self,surface):
        surface.blit(self.texture.convert_alpha(),(0,0))