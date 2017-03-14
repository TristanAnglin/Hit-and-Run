from scene import *

import time
import ui
import sound
import globals 

class HitAndRunShopScene(Scene):
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
        self.maxedatk = 0
        self.maxeddodge = 0
        self.counter = 0
        self.checkatk = 0
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
                                     
        self.back3_square1 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y + self.screen_center_y/1.6))
        self.buy1_label = LabelNode(text = 'Buy',
                                     font=('CopperPlate-Bold', 35),
                                     parent = self,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y + self.screen_center_y/1.6),
                                     color = 'grey')
        self.back3_square2 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y + self.screen_center_y/2.7))
        self.buy2_label = LabelNode(text = 'Buy',
                                     font=('CopperPlate-Bold', 35),
                                     parent = self,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y + self.screen_center_y/2.7),
                                     color = 'grey')
        self.back3_square3 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y + self.screen_center_y/9.25))
        self.buy3_label = LabelNode(text = 'Buy',
                                     font=('CopperPlate-Bold', 35),
                                     parent = self,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y + self.screen_center_y/9.25),
                                     color = 'grey')
        self.back3_square4 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y - self.screen_center_y/6.5))
        self.buy4_label = LabelNode(text = 'Buy',
                                     font=('CopperPlate-Bold', 35),
                                     parent = self,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y - self.screen_center_y/6.5),
                                     color = 'grey')
        self.back3_square5 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y - self.screen_center_y/2.4))
        self.buy5_label = LabelNode(text = 'Buy',
                                     font=('CopperPlate-Bold', 35),
                                     parent = self,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y - self.screen_center_y/2.4),
                                     color = 'grey')
        self.back3_square6 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y - self.screen_center_y/1.465))
        self.buy6_label = LabelNode(text = 'Buy',
                                     font=('CopperPlate-Bold', 35),
                                     parent = self,
                                     position = (self.screen_center_x + self.screen_center_x/2, self.screen_center_y - self.screen_center_y/1.465),
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
                                     position = (self.screen_center_x - self.screen_center_x/3, self.screen_center_y + self.screen_center_y/1.6))
        self.health_rune = SpriteNode('./assets/sprites/shop/runes/runeGrey_slab_035.png',
                                     parent = self,
                                     color = '#a4a4a4',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/3, self.screen_center_y + self.screen_center_y/1.57))
        self.health_label = LabelNode(text = 'HEALTH',
                                     font=('CopperPlate-Light', 12),
                                     parent = self,
                                     position = (self.screen_center_x - self.screen_center_x/3, self.screen_center_y + self.screen_center_y/1.79),
                                     color = 'grey')
        self.back1_square2 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/3, self.screen_center_y + self.screen_center_y/2.7))
        self.damage_rune = SpriteNode('./assets/sprites/shop/runes/runeGrey_slab_034.png',
                                     parent = self,
                                     color = '#a4a4a4',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/3, self.screen_center_y + self.screen_center_y/2.6))
        self.damage_label = LabelNode(text = 'DAMAGE',
                                     font=('CopperPlate-Light', 12),
                                     parent = self,
                                     position = (self.screen_center_x - self.screen_center_x/3, self.screen_center_y + self.screen_center_y/3.3),
                                     color = 'grey')
        self.back1_square3 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/3, self.screen_center_y + self.screen_center_y/9.25))
        self.lifesteal_rune = SpriteNode('./assets/sprites/shop/runes/runeGrey_slab_019.png',
                                     parent = self,
                                     color = '#a4a4a4',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/3, self.screen_center_y + self.screen_center_y/8.25))
        self.lifesteal_label = LabelNode(text = 'LIFESTEAL',
                                     font=('CopperPlate-Light', 12),
                                     parent = self,
                                     position = (self.screen_center_x - self.screen_center_x/3, self.screen_center_y + self.screen_center_y/24),
                                     color = 'grey')
        self.back1_square4 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/3, self.screen_center_y - self.screen_center_y/6.5))
        self.regen_rune = SpriteNode('./assets/sprites/shop/runes/runeGrey_slab_027.png',
                                     parent = self,
                                     color = '#a4a4a4',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/3, self.screen_center_y - self.screen_center_y/7.35))
        self.regen_label = LabelNode(text = 'REGEN',
                                     font=('CopperPlate-Light', 12),
                                     parent = self,
                                     position = (self.screen_center_x - self.screen_center_x/3, self.screen_center_y/1.279),
                                     color = 'grey')
        self.back1_square5 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/3, self.screen_center_y - self.screen_center_y/2.4))
        self.dodge_rune = SpriteNode('./assets/sprites/shop/runes/runeGrey_slab_025.png',
                                     parent = self,
                                     color = '#a4a4a4',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/3, self.screen_center_y - self.screen_center_y/2.48))
        self.dodge_label = LabelNode(text = 'DODGE',
                                     font=('CopperPlate-Light', 12),
                                     parent = self,
                                     position = (self.screen_center_x - self.screen_center_x/3, self.screen_center_y/1.92),
                                     color = 'grey')
        self.back1_square6 = SpriteNode('./assets/sprites/shop/backsquare.PNG',
                                     parent = self,
                                     color = 'grey',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/3, self.screen_center_y - self.screen_center_y/1.465))
        self.attackspeed_rune = SpriteNode('./assets/sprites/shop/runes/runeGrey_slab_006.png',
                                     parent = self,
                                     color = '#a4a4a4',
                                     scale = 0.65,
                                     position = (self.screen_center_x - self.screen_center_x/3, self.screen_center_y - self.screen_center_y/1.5))
        self.attackspeed_label = LabelNode(text = 'ATK SPEED',
                                     font=('CopperPlate-Light', 12),
                                     parent = self,
                                     position = (self.screen_center_x -self.screen_center_x/3, self.screen_center_y/3.9),
                                     color = 'grey')
        self.back2_square1 = SpriteNode('assets/sprites/game/gamestats.PNG',
                                     parent = self,
                                     color = 'lightgrey',
                                     size = (self.size_of_screen_x/1.95, self.size_of_screen_y/10),
                                     scale = 0.65,
                                     position = (self.back1_square1.position.x + (self.back1_square1.position.x / 1.65), self.screen_center_y + self.screen_center_y/1.6))
        self.price1_label = LabelNode(text = str(globals.price1),
                                     font=('CopperPlate-Bold', 25),
                                     parent = self,
                                     position = (self.back1_square1.position.x + (self.back1_square1.position.x / 1.65), self.screen_center_y + self.screen_center_y/1.6),
                                     color = 'gold')
        self.back2_square2 = SpriteNode('assets/sprites/game/gamestats.PNG',
                                     parent = self,
                                     color = 'lightgrey',
                                     size = (self.size_of_screen_x/1.95, self.size_of_screen_y/10),
                                     scale = 0.65,
                                     position = (self.back1_square1.position.x + (self.back1_square1.position.x / 1.65), self.screen_center_y + self.screen_center_y/2.7))
        self.price2_label = LabelNode(text = str(globals.price2),
                                     font=('CopperPlate-Bold', 25),
                                     parent = self,
                                     position = (self.back1_square1.position.x + (self.back1_square1.position.x / 1.65), self.screen_center_y + self.screen_center_y/2.7),
                                     color = 'gold')
        self.back2_square3 = SpriteNode('assets/sprites/game/gamestats.PNG',
                                     parent = self,
                                     color = 'lightgrey',
                                     size = (self.size_of_screen_x/1.95, self.size_of_screen_y/10),
                                     scale = 0.65,
                                     position = (self.back1_square1.position.x + (self.back1_square1.position.x / 1.65), self.screen_center_y + self.screen_center_y/9.25))
        self.price3_label = LabelNode(text = str(globals.price3),
                                     font=('CopperPlate-Bold', 25),
                                     parent = self,
                                     position = (self.back1_square1.position.x + (self.back1_square1.position.x / 1.65), self.screen_center_y + self.screen_center_y/9.25),
                                     color = 'gold')
        self.back2_square4 = SpriteNode('assets/sprites/game/gamestats.PNG',
                                     parent = self,
                                     color = 'lightgrey',
                                     size = (self.size_of_screen_x/1.95, self.size_of_screen_y/10),
                                     scale = 0.65,
                                     position = (self.back1_square1.position.x + (self.back1_square1.position.x / 1.65), self.screen_center_y - self.screen_center_y/6.5))
        self.price4_label = LabelNode(text = str(globals.price4),
                                     font=('CopperPlate-Bold', 25),
                                     parent = self,
                                     position = (self.back1_square1.position.x + (self.back1_square1.position.x / 1.65), self.screen_center_y - self.screen_center_y/6.5),
                                     color = 'gold')
        self.back2_square5 = SpriteNode('assets/sprites/game/gamestats.PNG',
                                     parent = self,
                                     color = 'lightgrey',
                                     size = (self.size_of_screen_x/1.95, self.size_of_screen_y/10),
                                     scale = 0.65,
                                     position = (self.back1_square1.position.x + (self.back1_square1.position.x / 1.65), self.screen_center_y - self.screen_center_y/2.4))
        self.price5_label = LabelNode(text = str(globals.price5),
                                     font=('CopperPlate-Bold', 25),
                                     parent = self,
                                     position = (self.back1_square1.position.x + (self.back1_square1.position.x / 1.65), self.screen_center_y - self.screen_center_y/2.4),
                                     color = 'gold')
        self.back2_square6 = SpriteNode('assets/sprites/game/gamestats.PNG',
                                     parent = self,
                                     color = 'lightgrey',
                                     size = (self.size_of_screen_x/1.95, self.size_of_screen_y/10),
                                     scale = 0.65,
                                     position = (self.back1_square1.position.x + (self.back1_square1.position.x / 1.65), self.screen_center_y - self.screen_center_y/1.465))
        self.price6_label = LabelNode(text = str(globals.price6),
                                     font=('CopperPlate-Bold', 25),
                                     parent = self,
                                     position = (self.back1_square1.position.x + (self.back1_square1.position.x / 1.65), self.screen_center_y - self.screen_center_y/1.465),
                                     color = 'gold')
        self.coinz = globals.coins
        self.coins_label = LabelNode(text = str(self.coinz),
                                     font=('CopperPlate-Bold', 25),
                                     parent = self,
                                     anchor_point = (0, 0.5),
                                     position = (50, self.size_of_screen_y - 30),
                                     color = 'gold')
        self.refund1 = LabelNode(text = '- Refund -',
                                     font=('CopperPlate-Bold', 20),
                                     parent = self,
                                     position = (self.back1_square1.position.x / 2.7, self.back1_square1.position.y),
                                     color = '#828282')
        self.refund2 = LabelNode(text = '- Refund -',
                                     font=('CopperPlate-Bold', 20),
                                     parent = self,
                                     position = (self.back1_square2.position.x / 2.7, self.back1_square2.position.y),
                                     color = '#828282')
        self.refund3 = LabelNode(text = '- Refund -',
                                     font=('CopperPlate-Bold', 20),
                                     parent = self,
                                     position = (self.back1_square3.position.x / 2.7, self.back1_square3.position.y),
                                     color = '#828282')
        self.refund4 = LabelNode(text = '- Refund -',
                                     font=('CopperPlate-Bold', 20),
                                     parent = self,
                                     position = (self.back1_square4.position.x / 2.7, self.back1_square4.position.y),
                                     color = '#828282')
        self.refund5 = LabelNode(text = '- Refund -',
                                     font=('CopperPlate-Bold', 20),
                                     parent = self,
                                     position = (self.back1_square5.position.x / 2.7, self.back1_square5.position.y),
                                     color = '#828282')
        self.refund6 = LabelNode(text = '- Refund -',
                                     font=('CopperPlate-Bold', 20),
                                     parent = self,
                                     position = (self.back1_square6.position.x / 2.7, self.back1_square6.position.y),
                                     color = '#828282')
        
        self.coins_img = SpriteNode('assets/sprites/coins.PNG', 
                                     position = (29, self.size_of_screen_y - 30),
                                     parent = self,
                                     scale = 0.14)
    def update(self):
        # this method is called, hopefully, 60 times a seco
        self.counter = self.counter + 1
        if globals.lv1 > 1:
            self.refund1.color = 'gold'
        elif globals.lv1 == 1:
            self.refund1.color = 'grey'
            
        if globals.lv2 > 1:
            self.refund2.color = 'gold'
        elif globals.lv2 == 1:
            self.refund2.color = 'grey'
            
        if globals.lv3 > 1:
            self.refund3.color = 'gold'
        elif globals.lv3 == 1:
            self.refund3.color = 'grey'
            
        if globals.lv4 > 1:
            self.refund4.color = 'gold'
        elif globals.lv4 == 1:
            self.refund4.color = 'grey'
            
        if globals.lv5 > 1:
            self.refund5.color = 'gold'
        elif globals.lv5 == 1:
            self.refund5.color = 'grey'
            
        if globals.lv6 > 1:
            self.refund6.color = 'gold'
        elif globals.lv6 == 1:
            self.refund6.color = 'grey'
            
        if self.counter >= 500:
            self.counter = 0
            self.coinz = globals.coins
            self.coins_label.text = str(self.coinz)
        # after 2 seconds, move to main menu scene
        self.price1_label.text = str(globals.price1) + ' [Lv' + str(globals.lv1) + ']'
        self.price2_label.text = str(globals.price2) + ' [Lv' + str(globals.lv2) + ']'
        self.price3_label.text = str(globals.price3) + ' [Lv' + str(globals.lv3) + ']'
        self.price4_label.text = str(globals.price4) + ' [Lv' + str(globals.lv4) + ']'
        
        if self.maxeddodge == 1:
            self.price5_label.text = 'Maxed'
            self.price5_label.color = 'grey'
        else:
            self.price5_label.color = 'gold'
            self.price5_label.text = str(globals.price5) + ' [Lv' + str(globals.lv5) + ']'
        
        if self.maxedatk == 1:
            self.price6_label.text = 'Maxed'
            self.price6_label.color = 'grey'
        else:
            self.price6_label.color = 'gold'
            self.price6_label.text = str(globals.price6) + ' [Lv' + str(globals.lv6) + ']'
        
        if globals.playeratkspeed <= 0.2:
            self.maxedatk = 1
        
        if globals.playerdodge >= 90:
            globals.playerdodge = 90
            self.maxeddodge = 1
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
            
        if self.refund1.frame.contains_point(touch.location) and globals.lv1 > 1:
            self.difference1 = globals.price1
            globals.lv1 = globals.lv1 - 1
            globals.price1 = int(round(globals.price1/1.3))
            globals.fullhealth = int(round(globals.fullhealth/1.25))
            globals.coins = globals.coins + globals.price1
            self.counter = 500
            
        if self.refund2.frame.contains_point(touch.location) and globals.lv2 > 1:
            self.difference2 = globals.price2
            globals.lv2 = globals.lv2 - 1
            globals.price2 = int(round(globals.price2/1.3))
            globals.playerdmglowest = int(round(globals.playerdmglowest/1.25))
            globals.playerdmghighest = int(round(globals.playerdmghighest/1.25))
            globals.coins = globals.coins + globals.price2
            self.counter = 500
            
        if self.refund3.frame.contains_point(touch.location) and globals.lv3 > 1:
            self.difference3 = globals.price3
            globals.lv3 = globals.lv3 - 1
            globals.price3 = int(round(globals.price3/1.3))
            globals.playerlifesteal = float(round((globals.playerlifesteal * 100) / 105) - 0.5)
            globals.coins = globals.coins + globals.price3
            self.counter = 500
            
        if self.refund4.frame.contains_point(touch.location) and globals.lv4 > 1:
            self.difference4 = globals.price4
            globals.lv4 = globals.lv4 - 1
            globals.price4 = int(round(globals.price4/1.3))
            globals.overtimeregen = round((globals.overtimeregen/1.2)*10) / 10
            globals.coins = globals.coins + globals.price4
            self.counter = 500
            
            
        if self.refund5.frame.contains_point(touch.location) and globals.lv5 > 1:
            self.difference5 = globals.price5
            globals.lv5 = globals.lv5 - 1
            globals.price5 = int(round(globals.price5/2))
            globals.playerdodge = int(round(globals.playerdodge/1.25))
            globals.coins = globals.coins + globals.price5
            self.counter = 500
            self.maxeddodge = 0
            
        if self.refund6.frame.contains_point(touch.location) and globals.lv6 > 1:
            self.difference6 = globals.price6
            globals.lv6 = globals.lv6 - 1
            globals.price6 = int(round(globals.price6/2))
            globals.playeratkspeed = globals.playeratkspeed + 0.1
            globals.coins = globals.coins + globals.price6
            self.maxedatk = 0
            self.counter = 500
        
        if self.buy1_label.frame.contains_point(touch.location) or self.back3_square1.frame.contains_point(touch.location):
            self.buy1_label_down = True
            if globals.coins >= globals.price1:
                self.counter = 500
                globals.coins = globals.coins - globals.price1
                globals.lv1 = globals.lv1 + 1
                globals.price1 = int(round(globals.price1*1.3))
                globals.fullhealth = int(round(globals.fullhealth*1.25))
                sound.play_effect('assets/Ding_1.caf')
            else:
                pass
             
        if self.buy2_label.frame.contains_point(touch.location) or self.back3_square2.frame.contains_point(touch.location):
            self.buy2_label_down = True
            if globals.coins >= globals.price2:
                self.counter = 500
                globals.coins = globals.coins - globals.price2
                globals.lv2 = globals.lv2 + 1
                globals.price2 = int(round(globals.price2*1.3))
                globals.playerdmglowest = int(round(globals.playerdmglowest*1.25))
                globals.playerdmghighest = int(round(globals.playerdmghighest*1.25))
                sound.play_effect('assets/Ding_1.caf')
            else:
                pass
            
        if self.buy3_label.frame.contains_point(touch.location) or self.back3_square3.frame.contains_point(touch.location):
            self.buy3_label_down = True
            if globals.coins >= globals.price3:
                self.counter = 500
                globals.coins = globals.coins - globals.price3
                globals.lv3 = globals.lv3 + 1
                globals.price3 = int(round(globals.price3*1.3))
                globals.playerlifesteal = float(round((globals.playerlifesteal + 0.5) * 105)/100)
                sound.play_effect('assets/Ding_1.caf')
            else:
                pass
            
        if self.buy4_label.frame.contains_point(touch.location) or self.back3_square4.frame.contains_point(touch.location):
            self.buy4_label_down = True
            if globals.coins >= globals.price4:
                self.counter = 500
                globals.coins = globals.coins - globals.price4
                globals.lv4 = globals.lv4 + 1
                globals.price4 = int(round(globals.price4*1.3))
                globals.overtimeregen = round((globals.overtimeregen*1.2)*10) / 10
                sound.play_effect('assets/Ding_1.caf')
            else:
                pass
            
        if self.buy5_label.frame.contains_point(touch.location) or self.back3_square5.frame.contains_point(touch.location):
            if self.maxeddodge == 0:
                self.buy5_label_down = True
                if globals.coins >= globals.price5:
                    self.counter = 500
                    globals.coins = globals.coins - globals.price5
                    globals.lv5 = globals.lv5 + 1
                    globals.price5 = int(round(globals.price5*2))
                    globals.playerdodge = int(round(globals.playerdodge*1.25))
                    sound.play_effect('assets/Ding_1.caf')
                else:
                    pass
            
        if self.buy6_label.frame.contains_point(touch.location) or self.back3_square6.frame.contains_point(touch.location):
            if self.maxedatk == 0:
                self.buy6_label_down = True
                if globals.coins >= globals.price6:
                    self.counter = 500
                    globals.coins = globals.coins - globals.price6
                    globals.lv6 = globals.lv6 + 1
                    globals.price6 = int(round(globals.price6 *2))
                    globals.playeratkspeed = (globals.playeratkspeed - 0.1)
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
