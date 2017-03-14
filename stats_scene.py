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
                                     
        self.basicslabel = LabelNode(text = '( BASICS )',
                                     font=('CopperPlate-Light', 30),
                                     parent = self,
                                     anchor_point = (0,0.5),
                                     position = (30, self.screen_center_y + self.screen_center_x/1.2),
                                     color = '#ff8500')
        self.basics = LabelNode(text = 'Health\nDamage\nAttack Speed\nDefense',
                                     font=('CopperPlate-Light', 25),
                                     parent = self,
                                     anchor_point = (0,1),
                                     position = (self.basicslabel.position.x + 22, self.basicslabel.position.y - 15),
                                     color = 'grey')
        self.chanceslabel = LabelNode(text = '( CHANCES )',
                                     font=('CopperPlate-Light', 30),
                                     parent = self,
                                     anchor_point = (0,0.5),
                                     position = (self.basicslabel.position.x, self.basics.position.y - 120),
                                     color = '#d100da')
        self.chances = LabelNode(text = 'Critical\nThorns\nEnrage\nDodge',
                                     font=('CopperPlate-Light', 25),
                                     parent = self,
                                     anchor_point = (0,1),
                                     position = (self.basicslabel.position.x + 22, self.chanceslabel.position.y - 15),
                                     color = 'grey')
        self.healinglabel = LabelNode(text = '( HEALING )',
                                     font=('CopperPlate-Light', 30),
                                     parent = self,
                                     anchor_point = (0,0.5),
                                     position = (self.basicslabel.position.x, self.chances.position.y - 120),
                                     color = '#2cff00')
        self.healing = LabelNode(text = 'Lifesteal\nRegeneration',
                                     font=('CopperPlate-Light', 25),
                                     parent = self,
                                     anchor_point = (0,1),
                                     position = (self.basicslabel.position.x + 22, self.healinglabel.position.y - 15),
                                     color = 'grey')
        self.essencelabel = LabelNode(text = '( ESSENCE )',
                                     font=('CopperPlate-Light', 30),
                                     parent = self,
                                     anchor_point = (0,0.5),
                                     position = (self.basicslabel.position.x, self.healing.position.y - 70),
                                     color = '#009bff')
        self.essences = LabelNode(text = 'Mana\nMana Gain\nEnergy\nEnergy Gain',
                                     font=('CopperPlate-Light', 25),
                                     parent = self,
                                     anchor_point = (0,1),
                                     position = (self.basicslabel.position.x + 22, self.essencelabel.position.y - 15),
                                     color = 'grey')
        
        
                                     
                                     
       # self.stat_labels = LabelNode(text=str(globals.fullhealth) + 'hp\n' + str(globals.playerdmglowest) + '-' + str(globals.playerdmghighest) + 'dmg\n' + str(globals.playercritdmg) + '%\n' + str(globals.playercritchance) + '%\n' + str(globals.overtimeregen) + 'hp /s\n' + str(globals.playerdodge) + '%\n' + str(globals.playeratkspeed) + 's\n' + str(globals.playerlifesteal) + '%hp /kill\n' + str(globals.playerenrage) + '%\n' + str(globals.playerthorns) + '%\n' + str(globals.playerarmor) + '%',
                           # font = ('CopperPlate-Light', 25),
                          #  parent = self,
                            #anchor_point = (0,0.5),
                          #  position = (self.screen_center_x - self.screen_center_x/3, self.screen_center_y),
                            #color = '#c53434')
                                     
                                     
                                     
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
