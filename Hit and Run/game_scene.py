from scene import *

import time
import ui
import random
import sound
import globals

class MonsterObj(object):
    pass

class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        #Positions and defaults
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        self.fixed_time_step = 'Nill'
        #Stats and counters
        self.currentkills = 0
        self.rubychanceadd = 0
        self.currentrubies = 0
        self.default = 'run'
        self.currentround = 1
        self.currentcoins = 0
        self.runspeed = 2.4
        self.swingspeed = 2.3
        self.currentarmor = 50
        self.currentatk = 0.5
        self.currentroundkills = 0
        self.state = globals.currentstate
        self.monsterspawned = 0
        self.monsterattack = 0
        self.timerregen = 0
        self.rotationc = 0
        self.timerdmglabel = 0
        self.timerroundup = 0
        self.health = int(globals.fullhealth)
        self.fullhp = globals.fullhealth
        self.roundkills = self.currentround * 3
        self.monster_attack_speed = 4.0
        self.monster_attack_rate = 3.0
        self.dodge = globals.playerdodge
        self.timerblock = 0
        self.crit = globals.playercritchance
        self.stopwatch = 0
        self.timersteal = 0
        self.monsterbatattack = 0
        self.monsterbatrotation = 0
        self.dmg = 0
        self.rangeheal = int(self.screen_center_x)*1.05 - int(self.screen_center_x)
        #Lists
        self.monstereffects = []
        self.Monsters = []
        self.monstersbat = []
        self.dmglabels = []
        self.roundup = []
        self.regenover5 = []
        self.blocklabels = []
        self.lifesteal = []
        #self.monsterhp = []
        self.resuming = []
        self.pausing = []
        self.dea = 0
        self.totaldmg = 0
        self.paused = False
        #Times
        self.monstehatk = time.time()
        self.regentime = time.time()
        self.passivecoins = time.time()
        self.currenttimeh = 0
        #CharaterStuff
        self.characterscale = 1.2
        self.characterpos = Vector2(self.screen_center_x, 200)
        #Bars
        self.bar = 25
        self.healthmaxpixels = 300
        self.pixels = int(self.healthmaxpixels * self.health / self.fullhp)
        self.percent = (self.health * 100) / self.fullhp
        #---------------------------------
        self.soulmaxpixels = 300
        self.sbar = 50
        self.soulpixels = self.soulmaxpixels * self.currentroundkills / self.roundkills
        #---------------------------------
        self.fullatk = globals.playeratkspeed
        self.attackmaxpixels = 300
        self.atbar = self.size_of_screen_x - 50
        self.waitattack = time.time()
        self.attackpixels = min((1 - (self.waitattack - self.currenttimeh) / self.fullatk), 1) * self.attackmaxpixels
        #---------------------------------
        self.armormaxpixels = 300
        self.arbar = 60
        self.armorpixels = self.armormaxpixels * self.currentarmor / 50
        #Image and Label Setups
        self.background1 = SpriteNode('./assets/sprites/backtest.PNG', 
                                     position = (self.screen_center_x, 0),
                                     parent = self,
                                     anchor_point = (0.5,0),
                                     size = (self.size_of_screen_x * 1.5, self.size_of_screen_y * 3),
                                     scale = 1.3)
                                     
        self.background1.texture.filtering_mode = FILTERING_NEAREST
        #self.background = SpriteNode('./assets/sprites/backtest.PNG', 
                                     #position = (self.screen_center_x, self.background1.position.y * 2),
                                     #parent = self,
                                     #size = (self.size_of_screen_x * 1.5, self.size_of_screen_y * 2),
                                     #scale = 1.3)
        self.shrub1 = (SpriteNode('./assets/sprites/shrub.PNG', 
                                      position = (self.screen_center_x - self.screen_center_x/2, 100),
                                      parent = self,
                                      scale = 1))
        
        self.attackback = (SpriteNode('./assets/sprites/game/updownpipe.PNG', 
                                      position = (self.atbar, 300),
                                      parent = self,
                                      scale = 1,
                                      size = (20, 300)))
        self.attackright = (SpriteNode('./assets/sprites/game/updowntop.PNG', 
                                       position = (self.atbar, 457),
                                       parent = self,
                                       scale = 1.25,
                                       size = (20, 15)))
        self.attackleft = (SpriteNode('./assets/sprites/game/updownbottom.PNG', 
                                      position = (self.atbar, 143),
                                      parent = self,
                                      scale = 1.25,
                                      size = (20, 15)))
        self.attackbar = (SpriteNode('./assets/sprites/game/updownbar.PNG', 
                                     position = (self.atbar, 150),
                                     parent = self,
                                     scale = 1,
                                     anchor_point = (0.5, 0),
                                     color = '#ce5eff',
                                     size = (20, self.attackpixels)))
        self.armorback = (SpriteNode('./assets/sprites/game/emptybar.JPG', 
                                     position = (self.screen_center_x, self.arbar),
                                     parent = self,
                                     scale = 1,
                                     size = (self.armormaxpixels, 20)))
        self.armorright = (SpriteNode('./assets/sprites/game/barright.PNG', 
                                      position = (self.screen_center_x + 157, self.arbar),
                                      parent = self,
                                      scale = 1.25,
                                      size = (15, 20)))
        self.armorleft = (SpriteNode('./assets/sprites/game/barleft.PNG', 
                                     position = (self.screen_center_x - 157, self.arbar),
                                     parent = self,
                                     scale = 1.25,
                                     size = (15, 20)))
        self.armorbar = (SpriteNode('./assets/sprites/dodgebar.PNG', 
                                    position = (self.screen_center_x - 150, self.arbar),
                                    parent = self,
                                    anchor_point = (0, 0.5),
                                    scale = 1,
                                    color = '#ffdc5e',
                                    size = (self.armorpixels, 20)))
        self.hpback = (SpriteNode('./assets/sprites/game/emptybar.JPG', 
                                  position = (self.screen_center_x, self.bar),
                                  parent = self,
                                  scale = 1.25,
                                  size = (300, 30)))
        self.hpright = (SpriteNode('./assets/sprites/game/barright.PNG', 
                                   position = (self.screen_center_x + 195, self.bar),
                                   parent = self,
                                   scale = 1.25,
                                   size = (15, 38)))
        self.hpleft = (SpriteNode('./assets/sprites/game/barleft.PNG', 
                                  position = (self.screen_center_x - 195, self.bar),
                                  parent = self,
                                  scale = 1.25,
                                  size = (15, 38)))
        self.hpbar = (SpriteNode('./assets/sprites/game/health.PNG', 
                                 position = (self.screen_center_x - 187, self.bar),
                                 parent = self,
                                 scale = 1.25,
                                 color = '#cbbcbc',
                                 anchor_point = (0, 0.5),
                                 size = (self.pixels, 28)))
        self.hpbar.texture.filtering_mode = FILTERING_NEAREST
        self.hplabel = (LabelNode(text = '[' + str(self.health) + ' / ' + str(globals.fullhealth) + '] ' + str(self.percent) + '%',
                                  position = (self.screen_center_x, self.bar + 2),
                                  color = '#000000',
                                  font = ('CopperPlate-Bold', 18),
                                  parent = self))
        
        self.dmgtotallabel = (LabelNode(text = '0',
                                     font = ('CopperPlate-Bold', 25),
                                     parent = self,
                                     color = '#dcd4d4',
                                     anchor_point = (0, 0.5),
                                     position = (self.sbar + 20, self.screen_center_y + 40)))
                                     
        self.sword_img = SpriteNode('assets/sprites/sword.PNG', 
                                     position = (self.sbar, self.screen_center_y + 40),
                                     parent = self,
                                     color = '#ffffff',
                                     scale = 0.1)
        
        self.killslabel = (LabelNode(text = str(self.currentkills),
                                     font = ('CopperPlate-Bold', 25),
                                     parent = self,
                                     color = '#000000',
                                     anchor_point = (0, 0.5),
                                     position = (self.sbar + 20, self.screen_center_y + 90)))
                                     
        self.skull_img = SpriteNode('assets/sprites/skull.PNG', 
                                     position = (self.sbar, self.screen_center_y + 90),
                                     parent = self,
                                     scale = 0.125)
                                     
        self.roundlab = (LabelNode(text = str(self.currentround),
                                     font = ('AvenirNext-Heavy', 60),
                                     parent = self,
                                     color = '#000000',
                                     anchor_point = (0, 0.5),
                                     position = (self.sbar, self.size_of_screen_y - 100)))
                                     
        self.coinslabel = (LabelNode(text = str(self.currentcoins),
                                     font = ('CopperPlate-Bold', 25),
                                     parent = self,
                                     color = 'gold',
                                     anchor_point = (0, 0.5),
                                     position = (self.sbar + 20, self.screen_center_y + 140)))
                                     
        self.coins_img = SpriteNode('assets/sprites/coins.PNG', 
                                     position = (self.sbar - 3, self.screen_center_y + 140),
                                     parent = self,
                                     scale = 0.14)
                                     
        self.rubylabel = (LabelNode(text = str(self.currentrubies),
                                     font = ('CopperPlate-Bold', 25),
                                     parent = self,
                                     color = '#ff0043',
                                     anchor_point = (0, 0.5),
                                     position = (self.sbar + 20, self.screen_center_y + 190)))
                                     
        self.ruby_img = SpriteNode('assets/sprites/gem.PNG', 
                                     position = (self.sbar, self.screen_center_y + 190),
                                     parent = self,
                                     scale = 0.15)
                                     
        self.soulbarback = (SpriteNode('./assets/sprites/game/updownpipe.PNG', 
                                       position = (self.sbar, 300),
                                       parent = self,
                                       scale = 1,
                                       size = (20, 300)))
        self.soulbarright = (SpriteNode('./assets/sprites/game/updowntop.PNG', 
                                        position = (self.sbar, 457),
                                        parent = self,
                                        scale = 1.25,
                                        size = (20, 15)))
        self.soulbarleft = (SpriteNode('./assets/sprites/game/updownbottom.PNG', 
                                       position = (self.sbar, 143),
                                       parent = self,
                                       scale = 1.25,
                                       size = (20, 15)))
        self.soulbar = (SpriteNode('./assets/sprites/game/updownbar.PNG', 
                                   position = (self.sbar, 150),
                                   parent = self,
                                   scale = 1,
                                   anchor_point = (0.5, 0),
                                   color = '#5effea',
                                   size = (20, self.soulpixels)))
        self.soulbar.texture.filtering_mode = FILTERING_NEAREST
        self.charater = (SpriteNode('./assets/sprites/game/defaultguy.PNG',
                                    position = (self.screen_center_x, 120),
                                    scale = self.characterscale,
                                    blend_mode = BLEND_NORMAL,
                                    parent = self))
        self.charater.texture.filtering_mode = FILTERING_NEAREST
        self.pause_button = SpriteNode('assets/sprites/game/pause.PNG',
                                       position = (self.size_of_screen_x - self.size_of_screen_x*0.025, self.size_of_screen_y - self.size_of_screen_y*0.13),
                                       parent = self,
                                       scale = 0.067,
                                       color = 'lightgrey')
        self.hit_button = SpriteNode(position = (self.size_of_screen_x - 300, 0 + 5),
                   anchor_point = (0.5, 0),
                   size = (self.size_of_screen_x - 300, self.size_of_screen_y -  500),
                   parent = self,
                   scale = 1.25,
                   color = '#bababa',
                   alpha = 0.0)
        self.charater.run_action(Action.move_to(self.charater.position.x, 200, 1.5))
        self.runtime = time.time()
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.pause_button.frame.contains_point(touch.location) and self.paused == False and self.dea != 1:
            self.paused = True
            
            self.pausing.append(SpriteNode(position = self.size / 2,
                   size = (self.size_of_screen_x, self.size_of_screen_y),
                   parent = self,
                   scale = 1.25,
                   color = '#ffffff',
                   alpha = 0.4))
                   
            self.pausing.append(SpriteNode('assets/sprites/resumeback.PNG',
                   position = self.size / 2,
                   parent = self,
                   scale = 1.15,
                   size = (200, 100),
                   alpha = 1))
                   
                   
            self.resuming.append(LabelNode(text = 'RESUME',
                   position = self.size / 2,
                   parent = self,
                   scale = 1.25,
                   color = '#dc7300',
                   font = ('AvenirNext-Heavy', 20)))
        if self.hit_button.frame.contains_point(touch.location) and self.health != globals.fullhealth + 1:
           if self.charater.position.y >= 200:
               if self.waitattack < time.time():
                    self.state = 'attack'
                    self.rotationc = 1
        if len(self.resuming) > 0 and self.resuming[0].frame.contains_point(touch.location):
            self.paused = False
            for remres in self.resuming:
                remres.remove_from_parent()
                self.resuming.remove(remres)
            for rempau in self.pausing:
                rempau.remove_from_parent()
                self.pausing.remove(rempau)
            for rempau in self.pausing:
                rempau.remove_from_parent()
                self.pausing.remove(rempau)
    def update(self):
        # this method is called, hopefully, 60 times a second
        self.basics()
        if self.dea != 1:
            self.scrollingback()
        if len(self.dmglabels) > 0 or len(self.regenover5) > 0 or len(self.blocklabels) > 0 or len(self.lifesteal) > 0:
            self.labels()
        self.waves()
        self.monsterspawning()
        self.characterstates()
        if len(self.Monsters) > 0:
            self.hit_monster()
        self.deadornah()
        self.regenpassive()
        self.passivecoin()
        if time.time() - self.monstehatk >= 0.2:
            self.monstehatk = time.time()
            self.monsterattacks()
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
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
        
    def monsterattacks(self):
        for monster in self.Monsters:
            if monster.sprite.position.y <= 300 and self.health > 0 and self.health <= globals.fullhealth:
                self.dodgechanceroll = random.randint(1, 100)
                if self.dodgechanceroll <= self.dodge and self.currentarmor > 0:
                    self.currentarmor = self.currentarmor - 1
                else:
                    self.monstadmg = round((monster.hp * 0.1 / 1.1)*10)/10
                    self.health = round((self.health - self.monstadmg)*10)/10
    def scrollingback(self):
        self.background1.run_action(Action.move_to(self.background1.position.x, self.background1.position.y - 2, 0))
        if self.backy1 <= (self.size_of_screen_y * -2.78):
            self.background1.run_action(Action.move_to(self.background1.position.x, -22, 0))
            
    def labels(self):
        
        if len(self.dmglabels) > 0:
            for dmglabel in self.dmglabels:
                self.timerdmglabel = time.time()
                dmglabel.run_action(Action.fade_to(0, 1.2))
                dmglabel.run_action(Action.move_to(dmglabel.position.x, 250, 0.5))
                if dmglabel.position.y <= 260:
                    dmglabel.remove_from_parent()
                    self.dmglabels.remove(dmglabel)
        if len(self.blocklabels) > 0:
            for armormove in self.blocklabels:
                self.timerblock = 0
                armormove.run_action(Action.fade_to(0, 1.2))
                armormove.run_action(Action.move_to(armormove.position.x, 150, 0.5))
                if armormove.position.y <= 160:
                    armormove.remove_from_parent()
                    self.blocklabels.remove(armormove)
        if len(self.lifesteal) > 0:
            for lifesteals in self.lifesteal:
                self.timersteal = 0
                lifesteals.run_action(Action.fade_to(0, 0.5))
                lifesteals.run_action(Action.move_to(lifesteals.position.x, self.bar - 12, 0.5))
                if lifesteals.position.y <= self.bar - 10:
                    lifesteals.remove_from_parent()
                    self.lifesteal.remove(lifesteals)
        if len(self.regenover5) > 0:
            for regenovertime in self.regenover5:
                self.timerregen = 0
                regenovertime.run_action(Action.fade_to(0, 0.5))
                regenovertime.run_action(Action.move_to(regenovertime.position.x, self.bar - 12, 0.5))
                if regenovertime.position.y <= self.bar - 10:
                    regenovertime.remove_from_parent()
                    self.regenover5.remove(regenovertime)
                    
    def basics(self):
        self.healthmaxpixels = 300
        self.pixels = self.healthmaxpixels * self.health / self.fullhp
        self.percent = int(round((self.health * 100) / self.fullhp))
        #self.backy = self.background.position.y
        self.backy1 = self.background1.position.y
        #---------------------------------
        self.soulpixels = self.soulmaxpixels * self.currentroundkills / self.roundkills
        #---------------------------------
        self.attackpixels = (min((1 - (self.waitattack - time.time()) / self.fullatk), 1) * self.attackmaxpixels)
        #---------------------------------
        self.armorpixels = self.armormaxpixels * self.currentarmor / 100
        self.coinslabel.text = str(self.currentcoins)
        self.rubylabel.text = str(self.currentrubies)
        self.killslabel.text = str(self.currentkills)
        self.soulbar.size = (20, self.soulpixels)
        self.armorbar.size = (self.armorpixels, 20)
        self.hpbar.size = (self.pixels, 28)
        self.attackbar.size = (20, self.attackpixels)
        self.shrub1.position.y = self.backy1 + 500
        self.hplabel.text = '[' + str(float(self.health)) + ' / ' + str(globals.fullhealth) + '] ' + str(self.percent) + '%'
        self.dmgtotallabel.text = str(self.totaldmg)
        if self.charater.position.y >= 200:
            self.runspeed = 2.9
        #run(show_fps = True, PORTRAIT)
        self.timerroundup = self.timerroundup + 1
        self.timerblock = self.timerblock + 1
        self.timersteal = self.timersteal + 1
        self.rotationc = self.rotationc + 1
        self.monsterattack = self.monsterattack + 1
        self.timerregen = self.timerregen + 1
        self.roundlab.text = str(self.currentround)
        self.monsterbatattack = self.monsterbatattack + 1
        self.monsterbatrotation = self.monsterbatrotation + 1
        
    def waves(self):
        if len(self.monstereffects) >= 1:
            for monsterfx in self.monstereffects:
                monsterfx.run_action(Action.scale_to(0, 0.3))
                monsterfx.run_action(Action.move_to(self.soulbar.position.x, self.soulbar.position.y + self.soulpixels, 0.1))
                
                for monsterfx in self.monstereffects:
                    if monsterfx.position.x <= self.soulbar.position.x + 10:
                        monsterfx.remove_from_parent()
                        self.monstereffects.remove(monsterfx)
        
        if self.currentroundkills == self.roundkills and self.state == 'run':
            self.state = 'run'
            self.currentround = self.currentround + 1
            if self.rubychanceadd < 100:
                self.rubychanceadd = self.rubychanceadd + 1
            if self.monster_attack_rate < 90.0:
                self.monster_attack_rate = self.monster_attack_rate + 1.0
            if self.monster_attack_speed > 2.0:
                self.monster_attack_speed = self.monster_attack_speed - 0.1
            self.currentroundkills = 0
            self.roundkills = self.currentround * 3
            self.monsterspawned = 0
            self.timerroundup = 0
            self.roundup.append(LabelNode(text = 'ROUND ' + str(self.currentround),
                                      position = (self.screen_center_x, self.screen_center_y + 100),
                                      color = 'black',
                                      alpha = 1.0,
                                      font = ('AvenirNext-Heavy', 50),
                                      parent = self))
            for roundups in self.roundup:
                roundups.run_action(Action.fade_to(0, 2))
                roundups.run_action(Action.move_to(roundups.position.x, self.screen_center_y - 50, 2))
                if roundups.position.y <= self.screen_center_x - 40:
                    roundups.remove_from_parent()
                    self.roundup.remove(roundups)
                    
    def test(self):
        pass
    def hit_monster(self):
        for monster in self.Monsters:
            if monster.sprite.position.y <= 310 and self.state == 'attack' and self.rotationc == 6:
                self.critchanceroll = random.randint(1, 100)
                if self.critchanceroll <= self.crit:
                    self.soundrandom = random.randint(1,2)
                    if self.soundrandom <= 2:
                        sound.play_effect('assets/Hit_2.caf')	
                    self.rubychance = random.randint(1, 1000)
                    if self.rubychance <= 10 + self.rubychanceadd:
                        self.currentrubies = self.currentrubies + 1
                        sound.play_effect('arcade:Explosion_6')
                    self.dmg = random.randint(globals.playerdmglowest + globals.playerdmglowest*(globals.playercritdmg/100), globals.playerdmghighest + globals.playerdmghighest*(globals.playercritdmg/100))
                    self.totaldmg = self.totaldmg + self.dmg
                    self.dmglabels.append(LabelNode(text = str(self.dmg),
                                      position = (self.screen_center_x - random.randint(1, 100) + random.randint(1, 100), 350 - random.randint(1,50) + random.randint(1,50)),
                                      color = '#b00000',
                                      alpha = 1.0,
                                      font = ('AvenirNext-Heavy', 18),
                                      parent = self))
                        
                else:
                    self.soundrandom = random.randint(1,2)
                    if self.soundrandom <= 2:
                        sound.play_effect('assets/Hit_2.caf')	
                    self.rubychance = random.randint(1, 1000)
                    if self.rubychance <= 10 + self.rubychanceadd:
                        self.currentrubies = self.currentrubies + 1
                        sound.play_effect('arcade:Explosion_6')
                    self.dmg = random.randint(globals.playerdmglowest, globals.playerdmghighest)
                    self.totaldmg = self.totaldmg + self.dmg
                    self.dmglabels.append(LabelNode(text = str(self.dmg),
                                      position = (self.screen_center_x - random.randint(1, 100) + random.randint(1, 100), 350 - random.randint(1,50) + random.randint(1,50)),
                                      color = '#ff0000',
                                      alpha = 1.0,
                                      font = ('AvenirNext-Heavy', 15),
                                      parent = self))
                monster.hp = monster.hp - int(self.dmg)
                if monster.hp <= 0:
                    self.monstereffects.append(SpriteNode('shp:wavering',
                                               color = '#26ffe3',
                                               scale = 0.35,
                                               parent = self,
                                               position = (monster.sprite.position.x, monster.sprite.position.y)))
                    monster.sprite.remove_from_parent()
                    self.Monsters.remove(monster)
                    self.health = min(self.health + globals.playerlifesteal, globals.fullhealth)
                    self.lifesteal.append(LabelNode(text = '+' + str(globals.playerlifesteal),
                                                    position = (self.screen_center_x - self.screen_center_x/2.5 - random.randint(0, int(self.rangeheal)) + random.randint(0, int(self.rangeheal) * 4), self.bar + 12),
                                      color = '#00ff59',
                                      alpha = 1.0,
                                      font = ('AvenirNext-Heavy', 10),
                                      parent = self))
                    self.currentkills = self.currentkills + 1
                    self.currentroundkills = self.currentroundkills + 1
                    self.currentcoins = self.currentcoins + random.randint((2 + self.currentround),(9 + self.currentround))
                            
    def regenpassive(self):
        if time.time() - self.regentime >= 0.1 and self.health < globals.fullhealth and self.health != 0:
            sound.play_effect('digital:TwoTone1')
            self.regentime = time.time()
            self.addheal = round((globals.overtimeregen/10.0)*10) / 10
            self.health = self.health + self.addheal
            if self.health > globals.fullhealth and self.dea == 0:
                self.health = globals.fullhealth
            self.regenover5.append(LabelNode(text = '+' + str(self.addheal),
                                      position = (self.screen_center_x + self.screen_center_x/2.5 + random.randint(0, int(self.rangeheal)) - random.randint(0, int(self.rangeheal) * 4), self.bar + 12),
                                      color = '#00ff16',
                                      alpha = 1.0,
                                      font = ('AvenirNext-Heavy', 10),
                                      parent = self))
    def characterstates(self):
        #CharaterActions
        if self.state == 'attack':
            self.charater.position = (self.screen_center_x, 210)
            if self.rotationc <= self.swingspeed:
                self.charater.texture = Texture('./assets/sprites/game/swing1.PNG')
            elif self.rotationc > self.swingspeed and self.rotationc <= (self.swingspeed * 2):
                self.charater.texture = Texture('./assets/sprites/game/swing2.PNG')
            elif self.rotationc > (self.swingspeed * 2) and self.rotationc <= (self.swingspeed * 3):
                self.charater.texture = Texture('./assets/sprites/game/swing3.PNG')
            elif self.rotationc > (self.swingspeed * 3) and self.rotationc <= (self.swingspeed * 4):
                self.charater.texture = Texture('./assets/sprites/game/swing4.PNG')
            elif self.rotationc > (self.swingspeed * 4) and self.rotationc <= (self.swingspeed * 5):
                self.charater.texture = Texture('./assets/sprites/game/swing5.PNG')
            elif self.rotationc > (self.swingspeed * 5) and self.rotationc <= (self.swingspeed * 6):
                self.charater.texture = Texture('./assets/sprites/game/swing6.PNG')
            elif self.rotationc > (self.swingspeed * 6):
                self.charater.texture = Texture('./assets/sprites/game/swing6.PNG')
                self.rotationc = 1
                self.state = self.default
                
            self.waitattack = self.fullatk + time.time()
        elif self.state == 'run':
            self.charater.position = (self.screen_center_x, 200)
            if self.rotationc <= self.runspeed:
                self.charater.texture = Texture('./assets/sprites/game/step1.PNG')
            elif self.rotationc > self.runspeed and self.rotationc <= (self.runspeed * 2):
                self.charater.texture = Texture('./assets/sprites/game/step2.PNG')
            elif self.rotationc > (self.runspeed * 2) and self.rotationc <= (self.runspeed * 3):
                self.charater.texture = Texture('./assets/sprites/game/step3.PNG')
            elif self.rotationc > (self.runspeed * 3) and self.rotationc <= (self.runspeed * 4):
                self.charater.texture = Texture('./assets/sprites/game/step4.PNG')
            elif self.rotationc > (self.runspeed * 4) and self.rotationc <= (self.runspeed * 5):
                self.charater.texture = Texture('./assets/sprites/game/step5.PNG')
            elif self.rotationc > (self.runspeed * 5) and self.rotationc <= (self.runspeed * 6):
                self.charater.texture = Texture('./assets/sprites/game/step6.PNG')
            elif self.rotationc > (self.runspeed * 6) and self.rotationc <= (self.runspeed * 7):
                self.charater.texture = Texture('./assets/sprites/game/step7.PNG')
            elif self.rotationc > (self.runspeed * 7) and self.rotationc <= (self.runspeed * 8):
                self.charater.texture = Texture('./assets/sprites/game/step8.PNG')
            elif self.rotationc > (self.runspeed * 8):
                self.charater.texture = Texture('./assets/sprites/game/step8.PNG')
                self.rotationc = 0
                
        elif self.state == 'stand':
            self.charater.position = (self.screen_center_x, 200)
            self.charater.texture = Texture('./assets/sprites/game/defaultguy.PNG')
        
        elif self.state == 'dead':
            self.charater.position = (self.screen_center_x, 200)
            self.charater.color = 'lightgrey'
            self.charater.texture = Texture('assets/sprites/game/dead.PNG')
            
    def passivecoin(self):
        if time.time() - self.passivecoins >= 1 and self.dea == 0:
            sound.play_effect('rpg:Footstep00')
            self.currentcoins = self.currentcoins + (1 * self.currentround)
            if self.currentarmor < 100 and self.dea != 1:
                self.currentarmor = self.currentarmor + (0.5*self.currentround)
            self.passivecoins = time.time()
    def deadornah(self):
        if self.state != 'dead' and self.health > globals.fullhealth:
            self.health = globals.fullhealth
        if self.health <= 0:
            self.health = globals.fullhealth + 1
            self.state = 'dead'
            self.dea = 1
            self.monsterspawned = self.roundkills 
            globals.coins = globals.coins + self.currentcoins
            globals.rubies = globals.rubies + self.currentrubies
            self.removescene = time.time()
            if time.time() - self.removescene > 3:
                self.dismiss_modal_scene()
            self.death = (SpriteNode(position = (self.screen_center_x, self.screen_center_y),
                                     parent = self,
                                     scale = 1,
                                     size = (self.size_of_screen_x * self.size_of_screen_x, self.size_of_screen_y * self.size_of_screen_x),
                                     alpha = 0.5))
            self.dead = LabelNode(text = 'you died!',
                                       position = (self.screen_center_x, self.screen_center_y),
                                       parent = self,
                                       scale = 1.25,
                                       color = '#a50000',
                                       font = ('CopperPlate-Light', 55))
    def monsterspawning(self):
        #MonsterSpawn
        self.creationrate = random.randint(1, 120)
        if self.monsterspawned < self.roundkills and self.creationrate <= self.monster_attack_rate:
            self.monsterspawned = self.monsterspawned + 1
            self.add_monster()
            
    def add_monster(self):
        monster = MonsterObj()
        if random.randint(0,1) == 1:
            monster.hp = random.randint(30, 60) * self.currentround / 2
            monster.sprite = SpriteNode('./assets/sprites/game/straightreaper.PNG',
                                    position = (random.randint(300, self.size_of_screen_x - 300), self.size_of_screen_y + 100),
                                    scale = 0.85,
                                    alpha = 0.95,
                                    parent = self)
        else:
            monster.hp = random.randint(10, 30) * self.currentround / 2
            monster.sprite = SpriteNode('./assets/sprites/eyeball.PNG',
                                    position = (random.randint(300, self.size_of_screen_x - 300), self.size_of_screen_y + 100),
                                    scale = 1,
                                    alpha = 0.95,
                                    parent = self)
        self.Monsters.append(monster)
        monster.sprite.run_action(Action.move_to(self.screen_center_x + random.randint(0, 75) - random.randint(0, 75), 280, self.monster_attack_speed))
