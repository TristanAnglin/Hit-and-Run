from scene import *

import time
import ui
import sound
import globals 

class ShopRubScene(Scene):
    def setup(self):
        
        self.fixed_time_step = 'Nill'
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        self.buy1_label_down = False
        self.buy2_label_down = False
        self.buy3_label_down = False
        self.buy4_label_down = False
        self.buy5_label_down = False
        self.buy6_label_down = False
        self.counter = 0
        # this method is called, when user moves to this scene
        
        # create timer, so that after 2 seconds move to next scene
        self.start_time = time.time()
        
        # add MT blue background color
        self.background = SpriteNode('assets/sprites/background.JPG', 
                                     position = self.size / 2,
                                     parent = self,
                                     scale = 1.25)
                                     
        self.game_label = LabelNode(text = 'Shop',
                                     font=('Markerfelt-Wide', 40),
                                     parent = self,
                                     position = (self.size_of_screen_x - 50, self.size_of_screen_y - 40),
                                     color = 'grey')
                                     
        
        self.back_button = SpriteNode('assets/sprites/backw.PNG',
                                       parent = self,
                                       position = (75, self.size_of_screen_y - 110),
                                       scale = 0.17,
                                       color = 'grey')
                                       
        self.back1_square1 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/2, self.screen_center_y + self.screen_center_y/1.6))
        self.critchance_rune = SpriteNode('./assets/sprites/runes/runeGrey_slab_032.png',
                                     parent = self,
                                     color = '#a4a4a4',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/2, self.screen_center_y + self.screen_center_y/1.57))
        self.critchance_label = LabelNode(text = 'CRIT CHANCE',
                                     font=('CopperPlate-Light', 12),
                                     parent = self,
                                     position = (self.screen_center_x - self.screen_center_x/2, self.screen_center_y + self.screen_center_y/1.79),
                                     color = 'grey')
        self.back1_square2 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/2, self.screen_center_y + self.screen_center_y/2.7))
        self.critdamage_rune = SpriteNode('./assets/sprites/runes/runeGrey_slab_010.png',
                                     parent = self,
                                     color = '#a4a4a4',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/2, self.screen_center_y + self.screen_center_y/2.6))
        self.critdamage_label = LabelNode(text = 'CRIT DAMAGE',
                                     font=('CopperPlate-Light', 12),
                                     parent = self,
                                     position = (self.screen_center_x - self.screen_center_x/2, self.screen_center_y + self.screen_center_y/3.3),
                                     color = 'grey')
        self.back2_square1 = SpriteNode('assets/sprites/game/gamestats.PNG',
                                     parent = self,
                                     color = 'lightgrey',
                                     size = (self.size_of_screen_x/2, self.size_of_screen_y/10),
                                     scale = 0.65,
                                     position = (self.screen_center_x, self.screen_center_y + self.screen_center_y/1.6))
        self.price1_label = LabelNode(text = str(globals.price1),
                                     font=('CopperPlate-Light', 25),
                                     parent = self,
                                     position = (self.screen_center_x, self.screen_center_y + self.screen_center_y/1.6),
                                     color = '#ff4a4a')
        self.back2_square2 = SpriteNode('assets/sprites/game/gamestats.PNG',
                                     parent = self,
                                     color = 'lightgrey',
                                     size = (self.size_of_screen_x/2, self.size_of_screen_y/10),
                                     scale = 0.65,
                                     position = (self.screen_center_x, self.screen_center_y + self.screen_center_y/2.7))
        self.price2_label = LabelNode(text = str(globals.price2),
                                     font=('CopperPlate-Light', 25),
                                     parent = self,
                                     position = (self.screen_center_x, self.screen_center_y + self.screen_center_y/2.7),
                                     color = '#ff4a4a')
        self.back3_square2 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y + self.screen_center_y/2.7))
        self.back3_square1 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y + self.screen_center_y/1.6))
        self.buy1_label = LabelNode(text = 'Buy',
                                     font=('CopperPlate-Light', 35),
                                     parent = self,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y + self.screen_center_y/1.6),
                                     color = 'grey')
        self.buy2_label = LabelNode(text = 'Buy',
                                     font=('CopperPlate-Light', 35),
                                     parent = self,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y + self.screen_center_y/2.7),
                                     color = 'grey')
                                     
        self.rubyz = globals.rubies
        self.ruby_label = LabelNode(text = str(self.rubyz),
                                     font = ('CopperPlate-Bold', 25),
                                     parent = self,
                                     anchor_point = (0, 0.5),
                                     position = (50, self.size_of_screen_y - 30),
                                     color = '#ff0043')
        self.ruby_img = SpriteNode('assets/sprites/gem.PNG', 
                                     position = (30, self.size_of_screen_y - 30),
                                     parent = self,
                                     scale = 0.15)
    def update(self):
        # this method is called, hopefully, 60 times a seco
        self.counter = self.counter + 1
        
        if self.counter >= 500:
            self.counter = 0
            self.rubyz = globals.rubies
            self.ruby_label.text = str(self.rubyz)
        # after 2 seconds, move to main menu scene
        self.price1_label.text = str(globals.rubprice1) + ' [Lv' + str(globals.rublv1) + ']'
        self.price2_label.text = str(globals.rubprice2) + ' [Lv' + str(globals.rublv2) + ']'
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
            
        if self.buy1_label.frame.contains_point(touch.location) or self.back3_square1.frame.contains_point(touch.location):
            self.buy1_label_down = True
            if globals.rubies >= globals.rubprice1:
                self.counter = 500
                globals.rubies = globals.rubies - globals.rubprice1
                globals.rublv1 = globals.rublv1 + 1
                globals.rubprice1 = int(round(globals.rubprice1*2))
                globals.playercritchance = int(round(globals.playercritchance*1.2))
                sound.play_effect('assets/Ding_1.caf')
            else:
                pass
             
        if self.buy2_label.frame.contains_point(touch.location) or self.back3_square2.frame.contains_point(touch.location):
            self.buy2_label_down = True
            if globals.rubies >= globals.rubprice2:
                self.counter = 500
                globals.rubies = globals.rubies - globals.rubprice2
                globals.rublv2 = globals.rublv2 + 1
                globals.rubprice2 = int(round(globals.rubprice2*2))
                globals.playercritdmg = int(round(globals.playercritdmg*1.04))
                sound.play_effect('assets/Ding_1.caf')
            else:
                pass
            
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
