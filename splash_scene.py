from scene import *
import ui
import time
import random
from main_menu_scene import *

class SplashScene(Scene):
    def setup(self):
        
        # this method is called, when user moves to this scene
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        self.start_time = time.time()
        self.timee = 0
        self.fulltimee = 380
        self.bar = self.screen_center_y - 15
        self.loadmaxpixels = 380
        self.pixels = self.loadmaxpixels * self.timee / self.fulltimee
        self.offset = (self.loadmaxpixels - self.pixels) / 2
        self.percent = (self.timee * 100) / self.fulltimee
        self.background = SpriteNode('./assets/sprites/backgroundload.JPG', 
                                     position = self.size / 2,
                                     parent = self,
                                     size = self.size,
                                     scale = 1.25)
                                     
        self.game_label = LabelNode(text = 'HIT & RUN',
                                    font=('CopperPlate-Bold', 80),
                                    parent = self,
                                    position = (self.screen_center_x, self.size_of_screen_y + 100),
                                    color = 'black')
                                     
        self.loadbarback = (SpriteNode('./assets/sprites/emptybar.JPG', 
                              position = (self.screen_center_x, self.screen_center_y - 15),
                              parent = self,
                              scale = 1,
                              color = '#ffffff',
                              size = (418, 29)))
                              
        self.rsword = SpriteNode('assets/sprites/swordshieldright.PNG', 
                              position = (self.screen_center_x + 300, self.bar),
                              parent = self,
                              scale = 0.3)
                              
        self.lsword = SpriteNode('assets/sprites/swordshieldleft.PNG', 
                              position = (self.screen_center_x - 300, self.bar),
                              parent = self,
                              scale = 0.3)
                              
        self.loadbarimg = SpriteNode('./assets/sprites/splash/loadbar.PNG', 
                              position = (self.screen_center_x, self.bar),
                              parent = self,
                              color = '#ff0000',
                              anchor_point = (0,0.5),
                              size = (self.pixels, 25))
                              
        self.loadbar = (LabelNode(text = str(self.percent) + '%',
                                      position = (self.screen_center_x, self.bar),
                                      color = '#00f215',
                                      font = ('CopperPlate-Bold', 18),
                                      parent = self))
        self.game_label.run_action(Action.move_to(self.screen_center_x, self.screen_center_y + 23, 2.25, TIMING_BOUNCE_OUT))
    def update(self):
        #this method is called, hopefully, 60 times a second
        self.loadmaxpixels = 380
        self.percent = (self.timee * 100) / self.fulltimee
        self.pixels = self.loadmaxpixels * self.timee / self.fulltimee
                              
        if not self.presented_scene and self.percent >= 100:
            self.present_modal_scene(MainMenuScene())
        else:
           self.timee = self.timee + 2
        
        #Increasing in size
        self.loadbarimg.position = (self.screen_center_x - 190, self.bar)
        self.loadbar.text = str(self.percent) + '%'
        self.loadbarimg.size = (self.pixels, 25)
                              
        #Colors on load bar label
        if self.percent <= 5:
            self.loadbar.color = '#FF0000'
            self.loadbarimg.color = '#FF0000'
        elif self.percent <= 10 and self.percent > 5:
            self.loadbar.color = '#FF2000'
            self.loadbarimg.color = '#FF2000'
        elif self.percent <= 15 and self.percent > 10:
            self.loadbar.color = '#FF4000'
            self.loadbarimg.color = '#FF4000'
        elif self.percent <= 20 and self.percent > 15:
            self.loadbar.color = '#FF6000'
            self.loadbarimg.color = '#FF6000'
        elif self.percent <= 25 and self.percent > 20:
            self.loadbar.color = '#FF8000'
            self.loadbarimg.color = '#FF8000'
        elif self.percent <= 30 and self.percent > 25:
            self.loadbar.color = '#FFA000'
            self.loadbarimg.color = '#FFA000'
        elif self.percent <= 35 and self.percent > 30:
            self.loadbar.color = '#FFC000'
            self.loadbarimg.color = '#FFC000'
        elif self.percent <= 40 and self.percent > 35:
            self.loadbar.color = '#FFE000'
            self.loadbarimg.color = '#FFE000'
        elif self.percent <= 45 and self.percent > 40:
            self.loadbar.color = '#FFFF00'
            self.loadbarimg.color = '#FFFF00'
        elif self.percent <= 50 and self.percent > 45:
            self.loadbar.color = '#E0FF00'
            self.loadbarimg.color = '#E0FF00'
        elif self.percent <= 55 and self.percent > 50:
            self.loadbar.color = '#C0FF00'
            self.loadbarimg.color = '#C0FF00'
        elif self.percent <= 60 and self.percent > 55:
            self.loadbar.color = '#A0FF00'
            self.loadbarimg.color = '#A0FF00'
        elif self.percent <= 65 and self.percent > 60:
            self.loadbar.color = '#80FF00'
            self.loadbarimg.color = '#80FF00'
        elif self.percent <= 70 and self.percent > 65:
            self.loadbar.color = '#70FF00'
            self.loadbarimg.color = '#70FF00'
        elif self.percent <= 75 and self.percent > 70:
            self.loadbar.color = '#60FF00'
            self.loadbarimg.color = '#60FF00'
        elif self.percent <= 80 and self.percent > 75:
            self.loadbar.color = '#50FF00'
            self.loadbarimg.color = '#50FF00'
        elif self.percent <= 85 and self.percent > 80:
            self.loadbar.color = '#40FF00'
            self.loadbarimg.color = '#40FF00'
        elif self.percent <= 90 and self.percent > 85:
            self.loadbar.color = '#30FF00'
            self.loadbarimg.color = '#30FF00'
        elif self.percent <= 95 and self.percent > 90:
            self.loadbar.color = '#20FF00'
            self.loadbarimg.color = '#20FF00'
        elif self.percent <= 100 and self.percent > 95:
            self.loadbar.color = '#10FF00'
            self.loadbarimg.color = '#10FF00'
            
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
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
