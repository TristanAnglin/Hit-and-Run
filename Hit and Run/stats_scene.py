from scene import *

import time
import ui

import globals
class StatsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        # create timer, so that after 2 seconds move to next scene
        self.start_time = time.time()
        
        # add MT blue background color
        self.background = SpriteNode('assets/sprites/background.JPG', 
                                     position = self.size / 2,
                                     parent = self,
                                     scale = 1.25)
                                     
        
                                     
        self.game_label = LabelNode(text = 'Stats',
                                     font=('Markerfelt-Wide', 40),
                                     parent = self,
                                     position = (self.size_of_screen_x - 55, self.size_of_screen_y - 40),
                                     color = 'grey')
                                     
        self.labels = LabelNode(text = 'HEALTH\nDAMAGE\nCRIT DAMAGE\nCRIT CHANCE\nREGEN\nDODGE CHANCE\nATTACK SPEED\nLIFESTEAL',
                                     font=('CopperPlate-Light', 35),
                                     parent = self,
                                     position = (150, self.screen_center_y),
                                     color = 'grey')
                                     
                                     
                                     
        self.stat_labels = LabelNode(text=str(globals.fullhealth) + 'hp\n' + str(globals.playerdmglowest) + '-' + str(globals.playerdmghighest) + 'dmg\n' + str(globals.playercritdmg) + '%\n' + str(globals.playercritchance) + '%\n' + str(globals.overtimeregen) + 'hp /s\n' + str(globals.playerdodge) + '%\n' + str(globals.playeratkspeed) + 's\n' + str(globals.playerlifesteal) + 'hp /kill',
                            font = ('CopperPlate-Light', 35),
                            parent = self,
                            position = (self.size_of_screen_x - 250, self.screen_center_y),
                            color = '#c53434')
                                     
                                     
                                     
        back_button_position = self.size
        back_button_position.x = 75
        back_button_position.y = back_button_position.y - 110
        self.back_button = SpriteNode('assets/sprites/backw.PNG',
                                       parent = self,
                                       position = back_button_position,
                                       scale = 0.17,
                                       color = 'grey')
                                       
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        # after 2 seconds, move to main menu scene
        pass
    
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
