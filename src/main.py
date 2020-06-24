import pygame as pg
import game 
import main_menu
import help_menu
import file_paths as fp

screen_width=1600
screen_height=900


class Main:
    def __init__(self):
        self.running=True
        pg.init()
        pg.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
        pg.mixer.init()
        pg.mixer.music.load(fp.mainloop)
        pg.mixer.music.set_volume(0.2)
        pg.mixer.music.play(-1)
        self.icon=pg.image.load(fp.Logopath)
        self.screen=pg.display.set_mode((screen_width,screen_height))
        pg.display.set_caption("TANKY Game")
        pg.display.set_icon(self.icon)
    def run(self):
        while self.running:
            self.menu_obj=main_menu.MainMenu(self.screen)
            self.menu_obj.run()
            if self.menu_obj.return_val==1:
                self.game_obj=game.Game(self.screen)
                self.game_obj.run()
            if self.menu_obj.return_val==2:
                self.help_obj=help_menu.HelpMenu(self.screen)
                self.help_obj.run()
            if self.menu_obj.return_val==0:
                self.running=False

main=Main()
main.run()