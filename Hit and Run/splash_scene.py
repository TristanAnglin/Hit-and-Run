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
                                    position = (self.screen_center_x, self.screen_center_y + 75),
                                    color = 'black')
                                     
        self.loadbarback = (SpriteNode('./assets/sprites/game/emptybar.JPG', 
                              position = (self.screen_center_x, self.screen_center_y - 15),
                              parent = self,
                              scale = 1,
                              size = (380, 30)))
        self.loadbarright = (SpriteNode('./assets/sprites/game/barright.PNG', 
                              position = (self.screen_center_x + 195, self.screen_center_y - 15),
                              parent = self,
                              scale = 1.25,
                              size = (10, 30)))
                              
        self.loadbarleft = (SpriteNode('./assets/sprites/game/barleft.PNG', 
                              position = (self.screen_center_x - 195, self.screen_center_y - 15),
                              parent = self,
                              scale = 1.25,
                              size = (10, 30)))
        
        self.rightsword = (SpriteNode('./assets/sprites/splash/swords.PNG', 
                              position = (self.screen_center_x + 225, self.screen_center_y - 15),
                              parent = self,
                              color = 'black',
                              scale = 0.6))
                              
        
        self.leftsword = (SpriteNode('./assets/sprites/splash/swords.PNG', 
                              position = (self.screen_center_x - 225, self.screen_center_y - 15),
                              parent = self,
                              color = 'black',
                              scale = 0.6))
                              
        self.loadbarimg = (SpriteNode('./assets/sprites/splash/loadbar.PNG', 
                              position = (self.screen_center_x - self.offset, self.bar),
                              parent = self,
                              size = (self.pixels, 25)))
                              
        self.loadbar = (LabelNode(text = str(self.percent) + '%',
                                      position = (self.screen_center_x, self.bar),
                                      color = '#00f215',
                                      font = ('CopperPlate-Bold', 18),
                                      parent = self))
    def update(self):
        #this method is called, hopefully, 60 times a second
        self.loadmaxpixels = 380
        self.offset = (self.loadmaxpixels - self.pixels) / 2
        self.percent = (self.timee * 100) / self.fulltimee
        self.pixels = self.loadmaxpixels * self.timee / self.fulltimee
                              
        
        if not self.presented_scene and time.time() - self.start_time > 3.2:
           self.dismiss_modal_scene()
           self.present_modal_scene(MainMenuScene())
        else:
           self.timee = self.timee + 2
        
        #Increasing in size
        self.loadbarimg.position = (self.screen_center_x - self.offset, self.bar)
        self.loadbar.text = str(self.percent) + '%'
        self.loadbarimg.size = (self.pixels, 25)
                              
        #Colors on load bar label
        if self.percent <= 5:
            self.loadbar.color = '#FF0000'
        elif self.percent <= 10 and self.percent > 5:
            self.loadbar.color = '#FF2000'
        elif self.percent <= 15 and self.percent > 10:
            self.loadbar.color = '#FF4000'
        elif self.percent <= 20 and self.percent > 15:
            self.loadbar.color = '#FF6000'
        elif self.percent <= 25 and self.percent > 20:
            self.loadbar.color = '#FF8000'
        elif self.percent <= 30 and self.percent > 25:
            self.loadbar.color = '#FFA000'
        elif self.percent <= 35 and self.percent > 30:
            self.loadbar.color = '#FFC000'
        elif self.percent <= 40 and self.percent > 35:
            self.loadbar.color = '#FFE000'
        elif self.percent <= 45 and self.percent > 40:
            self.loadbar.color = '#FFFF00'
        elif self.percent <= 50 and self.percent > 45:
            self.loadbar.color = '#E0FF00'
        elif self.percent <= 55 and self.percent > 50:
            self.loadbar.color = '#C0FF00'
        elif self.percent <= 60 and self.percent > 55:
            self.loadbar.color = '#A0FF00'
        elif self.percent <= 65 and self.percent > 60:
            self.loadbar.color = '#80FF00'
        elif self.percent <= 70 and self.percent > 65:
            self.loadbar.color = '#60FF00'
        elif self.percent <= 75 and self.percent > 70:
            self.loadbar.color = '#50FF00'
        elif self.percent <= 80 and self.percent > 75:
            self.loadbar.color = '#50FF00'
        elif self.percent <= 85 and self.percent > 80:
            self.loadbar.color = '#40FF00'
        elif self.percent <= 90 and self.percent > 85:
            self.loadbar.color = '#30FF00'
        elif self.percent <= 95 and self.percent > 90:
            self.loadbar.color = '#20FF00'
        elif self.percent <= 100 and self.percent > 95:
            self.loadbar.color = '#10FF00'
            
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
