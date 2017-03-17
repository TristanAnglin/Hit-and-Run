# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *

import time
import ui
import sound

from spell_scene import *
from stats_scene import *
from shop_scene import *
from game_scene import *
from shoprub_scene import *
from globals import *

class MainMenuScene(Scene):
    def setup(self):
        self.run_label_down = False
        self.shop_label_down = False
        self.stats_label_down = False
        self.spells_label_down = False
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        # this method is called, when user moves to this scene
        self.coinz = globals.coins
        self.rubiez = globals.rubies
        self.counter = 0
        # add MT blue background color
        self.background = SpriteNode('./assets/sprites/background.JPG', 
                                     position = self.size / 2,
                                     parent = self,
                                     scale = 1.25)
                                     
        self.smoke_run = SpriteNode('assets/sprites/Right.png', 
                                     position = self.size / 2,
                                     parent = self,
                                     color = '#b3b3b3',
                                     scale = 0.55)
                                     
        self.smoke_shop = SpriteNode('assets/sprites/Store.png', 
                                     position = (self.size_of_screen_x - 75, self.size_of_screen_y - 75),
                                     parent = self,
                                     color = '#b3b3b3',
                                     scale = 0.55)
        self.smoke_spells = SpriteNode('assets/sprites/spellicon.PNG', 
                                     position = (self.size_of_screen_x - 75, 75),
                                     parent = self,
                                     color = '#b3b3b3',
                                     scale = 0.55)
                                     
        self.smoke_stats = SpriteNode('assets/sprites/Menu.png', 
                                     position = (75, self.size_of_screen_y - 75),
                                     parent = self,
                                     color = '#b3b3b3',
                                     scale = 0.55)
                                     
        self.coins_label = LabelNode(text = str(self.coinz),
                                     font=('CopperPlate-Bold', 25),
                                     parent = self,
                                     anchor_point = (0, 0.5),
                                     position = (190, self.size_of_screen_y - 75),
                                     color = 'gold')
        self.coins_img = SpriteNode('assets/sprites/coins.PNG', 
                                     position = (170, self.size_of_screen_y - 75),
                                     parent = self,
                                     scale = 0.14)
        
        self.rubylabel = (LabelNode(text = str(self.rubiez),
                                     font = ('CopperPlate-Bold', 25),
                                     parent = self,
                                     color = '#ff0043',
                                     anchor_point = (0, 0.5),
                                     position = (170, self.size_of_screen_y - 115)))
                                     
        self.ruby_img = SpriteNode('assets/sprites/gem.PNG', 
                                     position = (150, self.size_of_screen_y - 115),
                                     parent = self,
                                     scale = 0.15)
        self.exp_img = SpriteNode('assets/sprites/exporb.PNG', 
                                     position = (150, self.size_of_screen_y - 35),
                                     parent = self,
                                     scale = 0.24,
                                     color = '#9aff84')
                                     
        self.exp_label = (LabelNode(text = 'Lv' + str(globals.playerlevel) + ' (' + str(globals.playerexp) + ' / ' + str(globals.playerexpnext) + ')',
                                     font = ('CopperPlate-Bold', 25),
                                     parent = self,
                                     color = '#00ff9b',
                                     anchor_point = (0, 0.5),
                                     position = (170, self.size_of_screen_y - 35)))
    def update(self):
        # this method is called, hopefully, 60 times a second
        self.counter = self.counter + 1
        if self.counter >= 30:
            self.counter = 0
            self.rubiez = globals.rubies
            self.rubylabel.text = str(self.rubiez)
            self.coinz = globals.coins
            self.coins_label.text = str(self.coinz)
            self.exp_label.text = 'Lv' + str(globals.playerlevel) + ' (' + str(globals.playerexp) + ' / ' + str(globals.playerexpnext) + ')'
            if globals.playerexp >= globals.playerexpnext:
                globals.coins = globals.coins + (50 * globals.playerlevel)
                globals.playerexp = globals.playerexp - globals.playerexpnext
                globals.playerlevel = globals.playerlevel + 1
                globals.rubies = globals.rubies + 1
                if globals.playerlevel <= 5:
                    globals.playerexpnext = int(round(globals.playerexpnext * 1.1))
                elif globals.playerlevel <= 15:
                    globals.playerexpnext = int(round(globals.playerexpnext * 1.25))
                elif globals.playerlevel <= 30:
                    globals.playerexpnext = int(round(globals.playerexpnext * 1.4))
                elif globals.playerlevel <= 50:
                    globals.playerexpnext = int(round(globals.playerexpnext * 1.65))
            
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
        
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.smoke_spells.frame.contains_point(touch.location):
            self.spells_label_down = True
            sound.play_effect('assets/Chop.caf')
            self.present_modal_scene(SpellsScene())
        if self.smoke_stats.frame.contains_point(touch.location):
            self.stats_label_down = True
            sound.play_effect('assets/Chop.caf')
            self.present_modal_scene(StatsScene())
        if self.smoke_shop.frame.contains_point(touch.location):
            self.shop_label_down = True
            sound.play_effect('assets/Chop.caf')
            self.present_modal_scene(HitAndRunShopScene())
        if self.smoke_run.frame.contains_point(touch.location):
            self.run_label_down = True
            sound.play_effect('assets/Chop.caf')
            run(GameScene(), show_fps = True, orientation = PORTRAIT, multi_touch = True, anti_alias = False)
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
