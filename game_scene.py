from scene import *

import time
import ui
import random
import sound
import globals

class Spells(object):
    pass
class MonsterObj(object):
    pass
class Terrain(object):
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
        self.expmulti = 0.2
        self.fireballs = []
        self.fireballmulti = 1
        self.fanofknives = []
        self.fanofknivesmulti = 1
        self.lifeshield = []
        self.magicmissle = []
        self.magicmisslemulti = 1
        #Stats and counters
        self.currentkills = 0
        self.originarmor = globals.playerarmor
        self.rubychanceadd = 0
        self.currentrubies = 0
        self.fullmana = globals.mana
        self.currentmana = self.fullmana
        self.default = 'run'
        self.currentround = 1
        self.currentcoins = 0
        self.runspeed = 2.4
        self.enrag = 0
        self.originhp = globals.fullhealth
        self.swingspeed = 2.3
        self.currentdodge = 100
        self.origincrit = globals.playercritchance
        self.currentatk = 0.5
        self.currentroundkills = 0
        self.state = globals.currentstate
        self.monsterspawned = 0
        self.monsterattack = 0
        self.timerregen = 0
        self.rotationc = 0
        self.timerdmglabel = 0
        self.timerroundup = 0
        self.scrollspeed = 2
        self.spellonecooldown = 0
        self.spelltwocooldown = 0
        self.spellthreecooldown = 0
        self.currentexp = 0
        self.originregen = globals.overtimeregen
        self.regen = globals.overtimeregen
        self.health = int(globals.fullhealth)
        self.fullhp = globals.fullhealth
        self.roundkills = self.currentround * 3
        self.monster_attack_speed = 4.0
        self.monster_attack_rate = 3.0
        self.dodge = globals.playerdodge
        self.timerdodge = 0
        self.crit = globals.playercritchance
        self.stopwatch = 0
        self.timersteal = 0
        self.dmg = 0
        self.rangeheal = int(self.screen_center_x)*1.05 - int(self.screen_center_x)
        #Lists
        self.Monsters = []
        self.dmglabels = []
        self.roundup = []
        self.regenover5 = []
        self.dodgelabels = []
        self.lifesteal = []
        self.terra = []
        self.resuming = []
        self.pausing = []
        self.terrainstart = []
        self.dea = 0
        self.totaldmg = 0
        self.paused = False
        #Times
        self.enragingtime = time.time()
        self.monstehatk = time.time()
        self.regentime = time.time()
        self.passivecoins = time.time()
        self.terratime = time.time()
        self.sotimer = 0
        self.sttimer = 0
        self.sthtimer = 0
        self.currenttimeh = 0
        #CharaterStuff
        self.characterscale = 1
        self.characterpos = Vector2(self.screen_center_x, 200)
        #Bars
        self.bar = 24
        self.healthmaxpixels = 300
        self.pixels = int(self.healthmaxpixels * self.health / self.fullhp)
        self.percent = (self.health * 100) / self.fullhp
        #---------------------------------
        self.manamaxpixels = 300
        self.sbar = 50
        self.manapixels = self.manamaxpixels * self.currentroundkills / self.roundkills
        #---------------------------------
        self.fullatk = globals.playeratkspeed
        self.attackmaxpixels = 300
        self.atbar = self.size_of_screen_x - 50
        self.waitattack = time.time()
        self.attackpixels = min((1 - (self.waitattack - self.currenttimeh) / self.fullatk), 1) * self.attackmaxpixels
        #---------------------------------
        self.dodgemaxpixels = 300
        self.arbar = 60
        self.dodgepixels = self.dodgemaxpixels * self.currentdodge / 50
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
        self.attackback = (SpriteNode('./assets/sprites/game/updownpipe.JPG', 
                                      position = (self.atbar, 300),
                                      parent = self,
                                      scale = 1,
                                      size = (24, 326)))
        self.attackbar = (SpriteNode('./assets/sprites/game/updownbar.PNG', 
                                     position = (self.atbar, 150),
                                     parent = self,
                                     scale = 1,
                                     anchor_point = (0.5, 0),
                                     color = '#ce5eff',
                                     size = (24, self.attackpixels + 30)))
        self.dodgeback = (SpriteNode('./assets/sprites/emptybar.JPG', 
                                     position = (self.screen_center_x, self.arbar),
                                     parent = self,
                                     scale = 1,
                                     size = (self.dodgemaxpixels + 30, 24)))
        
        self.dodgebar = (SpriteNode('./assets/sprites/dodgebar.PNG', 
                                    position = (self.screen_center_x - 150, self.arbar),
                                    parent = self,
                                    anchor_point = (0, 0.5),
                                    scale = 1,
                                    color = '#ffdc5e',
                                    size = (self.dodgepixels, 20)))
        self.hpback = (SpriteNode('./assets/sprites/emptybar.JPG', 
                                  position = (self.screen_center_x, self.bar),
                                  parent = self,
                                  scale = 1.25,
                                  size = (329, 32)))
        self.hpbar = (SpriteNode('assets/sprites/splash/loadbar.PNG', 
                                 position = (self.screen_center_x - 187, self.bar),
                                 parent = self,
                                 scale = 1.25,
                                 color = '#cbbcbc',
                                 anchor_point = (0, 0.5),
                                 size = (self.pixels, 30)))
        self.hpbar.texture.filtering_mode = FILTERING_NEAREST
        self.hplabel = (LabelNode(text = '[' + str(self.health) + ' / ' + str(globals.fullhealth) + '] ' + str(self.percent) + '%',
                                  position = (self.screen_center_x, self.bar + 5),
                                  color = '#000000',
                                  font = ('CopperPlate-Bold', 18),
                                  parent = self))
        
        self.exptotal = (LabelNode(text = '0',
                                     font = ('CopperPlate-Bold', 25),
                                     parent = self,
                                     color = '#00dc86',
                                     anchor_point = (0, 0.5),
                                     position = (self.sbar + 20, self.screen_center_y + 40)))
                                     
        self.exp_img = SpriteNode('assets/sprites/exporb.PNG', 
                                     position = (self.sbar, self.screen_center_y + 40),
                                     parent = self,
                                     color = '#00ff9b',
                                     scale = 0.22)
                                     
        self.killslabel = (LabelNode(text = str(self.currentkills),
                                     font = ('CopperPlate-Bold', 25),
                                     parent = self,
                                     color = '#dadada',
                                     anchor_point = (0, 0.5),
                                     position = (self.sbar + 20, self.screen_center_y + 90)))
                                     
        self.sword_img = SpriteNode('assets/sprites/sword.PNG', 
                                     position = (self.sbar, self.screen_center_y + 90),
                                     parent = self,
                                     scale = 0.1)
                                     
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
                                     position = (self.sbar, self.screen_center_y + 140),
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
                                     
        self.manabarback = (SpriteNode('./assets/sprites/game/updownpipe.JPG', 
                                       position = (self.sbar, 300),
                                       parent = self,
                                       scale = 1,
                                       size = (24, 326)))
                                       
        self.manabar = (SpriteNode('./assets/sprites/game/updownbar.PNG', 
                                   position = (self.sbar, 150),
                                   parent = self,
                                   scale = 1,
                                   anchor_point = (0.5, 0),
                                   color = '#5effea',
                                   size = (20, self.manapixels)))
                                   
        self.charater = (SpriteNode('./assets/sprites/game/defaultguy.PNG',
                                    position = (self.screen_center_x, 120),
                                    scale = self.characterscale,
                                    blend_mode = BLEND_NORMAL,
                                    parent = self))
        self.charater.texture.filtering_mode = FILTERING_NEAREST
        
        self.pause_button = SpriteNode('assets/sprites/Pause.png',
                                       position = (80, 60),
                                       parent = self,
                                       scale = 0.4,
                                       color = '#b3b3b3')
                                       
        self.manalabel = (LabelNode(text = str(self.currentmana),
                                     font = ('CopperPlate-Bold', 10),
                                     parent = self,
                                     color = '#00ffb9',
                                     anchor_point = (0.5, 0.5),
                                     position = (self.sbar, self.manabar.position.y + self.manapixels)))
                                     
        self.hit_button = SpriteNode(position = (self.screen_center_x, 0),
                   anchor_point = (0, 0),
                   size = (self.screen_center_x, self.screen_center_y),
                   parent = self,
                   scale = 1.25,
                   color = '#bababa',
                   alpha = 0)
        self.charater.run_action(Action.move_to(self.charater.position.x, 200, 1.5))
        if globals.spellone != '':
            self.spellone = SpriteNode(globals.spellone,
                                       position = (int(self.sbar + 60), int(self.dodgebar.position.y + 95)),
                                       parent = self,
                                       anchor_point = (0.5, 0),
                                       scale = 0.35)
            self.spellonecover = SpriteNode('assets/sprites/frame-8-grey.png',
                                       position = (int(self.sbar + 60), int(self.dodgebar.position.y + 95)),
                                       parent = self,
                                       anchor_point = (0.5, 0),
                                       scale = 0.35)
        else:
            self.spellonecover = SpriteNode('assets/sprites/frame-8-grey.png',
                                       position = (int(self.sbar + 60), int(self.dodgebar.position.y + 95)),
                                       parent = self,
                                       alpha = 0,
                                       anchor_point = (0.5, 0),
                                       scale = 0)
            self.spellone = SpriteNode(position = (int(self.sbar + 60), int(self.dodgebar.position.y + 95)),
                                       parent = self,
                                       alpha = 0,
                                       anchor_point = (0.5, 0),
                                       scale = 0)
        if globals.spelltwo != '':
            self.spelltwo = SpriteNode(globals.spelltwo,
                                       position = (int(self.sbar + 60), int(self.spellone.position.y + 100)),
                                       parent = self,
                                       anchor_point = (0.5, 0),
                                       scale = 0.35)
            self.spelltwocover = SpriteNode('assets/sprites/frame-8-grey.png',
                                       position = (int(self.sbar + 60), int(self.dodgebar.position.y + 95 + 100)),
                                       parent = self,
                                       anchor_point = (0.5, 0),
                                       scale = 0.35)
        else:
            self.spelltwocover = SpriteNode('assets/sprites/frame-8-grey.png',
                                       position = (int(self.sbar + 60), int(self.dodgebar.position.y + 95 + 100)),
                                       parent = self,
                                       alpha = 0,
                                       anchor_point = (0.5, 0),
                                       scale = 0)
            self.spelltwo = SpriteNode(position = (int(self.sbar + 60), int(self.spellone.position.y + 95)),
                                       parent = self,
                                       alpha = 0,
                                       anchor_point = (0.5, 0),
                                       scale = 0)
        if globals.spellthree != '':
            self.spellthree = SpriteNode(globals.spellthree,
                                       position = (int(self.sbar + 60), int(self.dodgebar.position.y + 95 + 200)),
                                       parent = self,
                                       anchor_point = (0.5, 0),
                                       scale = 0.35)
            self.spellthreecover = SpriteNode('assets/sprites/frame-8-grey.png',
                                       position = (int(self.sbar + 60), int(self.spelltwocover.position.y + 100)),
                                       parent = self,
                                       anchor_point = (0.5, 0),
                                       scale = 0.35)
        else:
            self.spellthreecover = SpriteNode('assets/sprites/frame-8-grey.png',
                                       position = (int(self.sbar + 60), int(self.spelltwocover.position.y + 100)),
                                       parent = self,
                                       alpha = 0,
                                       anchor_point = (0.5, 0),
                                       scale = 0)
            self.spellthree = SpriteNode(position = (int(self.sbar + 60), int(self.spelltwo.position.y + 95)),
                                       parent = self,
                                       alpha = 0,
                                       anchor_point = (0.5, 0),
                                       scale = 0)
        self.spellonetime = LabelNode('0s',
                                       font = ('CopperPlate-Bold', 25),
                                       position = (int(self.sbar + 60), int(self.dodgebar.position.y + 95)),
                                       parent = self,
                                       color = '#cdcdcd',
                                       anchor_point = (0.5, 0),
                                       scale = 1)
        
        self.spelltwotime = LabelNode('0s',
                                       font = ('CopperPlate-Bold', 25),
                                       position = (int(self.sbar + 60), int(self.spellone.position.y + 100)),
                                       parent = self,
                                       color = '#cdcdcd',
                                       anchor_point = (0.5, 0),
                                       scale = 1)
        
        self.spellthreetime = LabelNode('0s',
                                       font = ('CopperPlate-Bold', 25),
                                       position = (int(self.sbar + 60), int(self.spelltwo.position.y + 100)),
                                       parent = self,
                                       color = '#cdcdcd',
                                       anchor_point = (0.5, 0),
                                       scale = 1)
        
        
        
        self.runtime = time.time()
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.dea == 0:
            if self.spellone.frame.contains_point(touch.location) and self.spellonecooldown <= 0 or self.spellonecover.frame.contains_point(touch.location) and self.spellonecooldown <= 0:
                self.checkspellone()
            if self.spelltwo.frame.contains_point(touch.location) and self.spelltwocooldown <= 0 or self.spelltwocover.frame.contains_point(touch.location) and self.spelltwocooldown <= 0:
                self.checkspelltwo()
            if self.spellthree.frame.contains_point(touch.location) and self.spellthreecooldown <= 0 or self.spellthreecover.frame.contains_point(touch.location) and self.spellthreecooldown <= 0:
                self.checkspellthree()
                self.currentmana = self.currentmana - self.spellthreemana
        
        if self.pause_button.frame.contains_point(touch.location) and self.paused == False and self.dea != 1:
            self.paused = True
            
            self.pausing.append(SpriteNode(position = self.size / 2,
                   size = (self.size_of_screen_x, self.size_of_screen_y),
                   parent = self,
                   scale = 1.25,
                   color = '#ffffff',
                   alpha = 0.4))
                   
            self.pausing.append(SpriteNode('assets/sprites/Right.png',
                   position = self.size / 2,
                   parent = self,
                   scale = 0.4,
                   alpha = 1))
                   
        if self.hit_button.frame.contains_point(touch.location) and self.health != 0 and self.paused == False:
           if self.charater.position.y >= 200:
               if self.waitattack < time.time():
                    self.state = 'attack'
                    self.rotationc = 1
        if len(self.pausing) > 0 and self.pausing[1].frame.contains_point(touch.location):
            self.paused = False
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
            #self.terraspawn()
            #self.terramove()
        self.spellcast()
        if time.time() - self.enragingtime >= 5 and self.enrag == 1:
            self.charater.scale = self.charater.scale - 0.5
            self.enrag = 0
            self.crit = self.origincrit
            self.fullhp = self.originhp
            self.regen = self.originregen
        if len(self.dmglabels) > 0 or len(self.regenover5) > 0 or len(self.dodgelabels) > 0 or len(self.lifesteal) > 0:
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
        self.terraremove()
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
            if monster.sprite.position.y <= 300 and self.health > 0 and self.health <= float(round(self.fullhp* 10) / 10):
                self.dodgechanceroll = random.randint(1, 100)
                if self.dodgechanceroll <= self.dodge and self.currentdodge > 0:
                    self.currentdodge = self.currentdodge - 1
                else:
                    self.monstadmg = round((monster.hp * 0.025)*10)/10 
                    self.monstadmgreduc = self.monstadmg * (globals.playerarmor / 100)
                    self.health = round((self.health - (self.monstadmg - self.monstadmgreduc))*10)/10
                    if self.percent <= 50:
                        self.enrageroll = random.randint(1,100)
                        if self.enrageroll <= globals.playerenrage and self.enrag != 1:
                            self.enraged()
                    self.thornsroll = random.randint(1,100)
                    if self.thornsroll <= globals.playerthorns:
                        self.dmg = (random.randint(globals.playerdmglowest, globals.playerdmghighest)/2)
                        self.totaldmg = self.totaldmg + self.dmg
                        if len(self.dmglabels) < 10:
                            self.dmglabels.append(LabelNode(text = str(self.dmg),
                                      position = (self.screen_center_x - random.randint(1, 100) + random.randint(1, 100), random.randint(350,360)),
                                      color = '#ff00c8',
                                      alpha = 1.0,
                                      font = ('AvenirNext-Heavy', 12),
                                      parent = self))
                        monster.hp = monster.hp - self.dmg
                        if monster.hp <= 0:
                            monster.sprite.remove_from_parent()
                            self.Monsters.remove(monster)
                            self.currentexp = self.currentexp + int(round(random.randint(1,7) * self.currentround) * self.expmulti)
                            self.currentkills = self.currentkills + 1
                            self.currentroundkills = self.currentroundkills + 1
                            self.currentcoins = self.currentcoins + int(round(random.randint((2 + self.currentround),(9 + self.currentround)) / 2))
    def scrollingback(self):
        self.background1.run_action(Action.move_to(self.screen_center_x, self.background1.position.y - self.scrollspeed, 0))
        if self.backy1 <= (self.size_of_screen_y * -2.78):
            self.background1.run_action(Action.move_to(self.screen_center_x, -22, 0))
            
    def labels(self):
        
        if len(self.dmglabels) > 0:
            for dmglabel in self.dmglabels:
                dmglabel.run_action(Action.fade_to(0, 0.6))
                dmglabel.run_action(Action.move_to(dmglabel.position.x, 240, 0.2))
                if dmglabel.position.y <= 250:
                    dmglabel.remove_from_parent()
                    self.dmglabels.remove(dmglabel)
        if len(self.dodgelabels) > 0:
            for dodgemove in self.dodgelabels:
                dodgemove.run_action(Action.fade_to(0, 1.2))
                dodgemove.run_action(Action.move_to(dodgemove.position.x, 150, 0.5))
                if dodgemove.position.y <= 160:
                    dodgemove.remove_from_parent()
                    self.dodgelabels.remove(dodgemove)
        if len(self.lifesteal) > 0:
            for lifesteals in self.lifesteal:
                lifesteals.run_action(Action.fade_to(0, 0.5))
                lifesteals.run_action(Action.move_to(lifesteals.position.x, self.bar - 12, 0.5))
                if lifesteals.position.y <= self.bar - 10:
                    lifesteals.remove_from_parent()
                    self.lifesteal.remove(lifesteals)
        if len(self.regenover5) > 0:
            for regenovertime in self.regenover5:
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
        self.manalabel.text = str(self.currentmana)
        self.manalabel.position = (self.sbar - 10, self.manabar.position.y + self.manapixels - 5)
        if self.percent <= 5:
            self.hpbar.color = '#FF0000'
        elif self.percent <= 10 and self.percent > 5:
            self.hpbar.color = '#FF2000'
        elif self.percent <= 15 and self.percent > 10:
            self.hpbar.color = '#FF4000'
        elif self.percent <= 20 and self.percent > 15:
            self.hpbar.color = '#FF6000'
        elif self.percent <= 25 and self.percent > 20:
            self.hpbar.color = '#FF8000'
        elif self.percent <= 30 and self.percent > 25:
            self.hpbar.color = '#FFA000'
        elif self.percent <= 35 and self.percent > 30:
            self.hpbar.color = '#FFC000'
        elif self.percent <= 40 and self.percent > 35:
            self.hpbar.color = '#FFE000'
        elif self.percent <= 45 and self.percent > 40:
            self.hpbar.color = '#FFFF00'
        elif self.percent <= 50 and self.percent > 45:
            self.hpbar.color = '#E0FF00'
        elif self.percent <= 55 and self.percent > 50:
            self.hpbar.color = '#C0FF00'
        elif self.percent <= 60 and self.percent > 55:
            self.hpbar.color = '#A0FF00'
        elif self.percent <= 65 and self.percent > 60:
            self.hpbar.color = '#80FF00'
        elif self.percent <= 70 and self.percent > 65:
            self.hpbar.color = '#70FF00'
        elif self.percent <= 75 and self.percent > 70:
            self.hpbar.color = '#60FF00'
        elif self.percent <= 80 and self.percent > 75:
            self.hpbar.color = '#50FF00'
        elif self.percent <= 85 and self.percent > 80:
            self.hpbar.color = '#40FF00'
        elif self.percent <= 90 and self.percent > 85:
            self.hpbar.color = '#30FF00'
        elif self.percent <= 95 and self.percent > 90:
            self.hpbar.color = '#20FF00'
        elif self.percent <= 100 and self.percent > 95:
            self.hpbar.color = '#10FF00'
        #---------------------------------
        self.manapixels = self.manamaxpixels * self.currentmana / self.fullmana
        #---------------------------------
        self.attackpixels = (min((1 - (self.waitattack - time.time()) / self.fullatk), 1) * self.attackmaxpixels)
        #---------------------------------
        self.dodgepixels = self.dodgemaxpixels * self.currentdodge / 100
        self.coinslabel.text = str(self.currentcoins)
        self.rubylabel.text = str(self.currentrubies)
        self.killslabel.text = str(self.currentkills)
        if self.spellonecooldown > 0:
            self.spellonecooldown = int(self.startingso + self.sotimer - time.time())
            self.spellonetime.text = str(self.spellonecooldown)
        if self.spelltwocooldown > 0:
            self.spelltwocooldown = int(self.startingst + self.sttimer - time.time())
            self.spelltwotime.text = str(self.spelltwocooldown)
        if self.spellthreecooldown > 0:
            self.spellthreecooldown = int(self.startingsth + self.sthtimer - time.time())
            self.spellthreetime.text = str(self.spellthreecooldown)
        self.manabar.size = (20, self.manapixels)
        self.dodgebar.size = (self.dodgepixels, 21)
        self.hpbar.size = (self.pixels, 28)
        self.attackbar.size = (20, self.attackpixels)
        if self.health == self.fullhp:
            self.hplabel.text = '[' + str(int(round(self.fullhp* 10) / 10)) + ' / ' + str(int(round(self.fullhp* 10) / 10)) + '] ' + str(self.percent) + '%'
        elif self.health != self.fullhp:
            self.hplabel.text = '[' + str(float(round(self.health * 10) / 10)) + ' / ' + str(int(round(self.fullhp* 10) / 10)) + '] ' + str(self.percent) + '%'
        self.exptotal.text = str(self.currentexp)
        if self.charater.position.y >= 195:
            self.runspeed = 2.9
        #run(show_fps = True, PORTRAIT)
        self.timerroundup = self.timerroundup + 1
        self.timerdodge = self.timerdodge + 1
        self.timersteal = self.timersteal + 1
        self.rotationc = self.rotationc + 1
        self.monsterattack = self.monsterattack + 1
        self.timerregen = self.timerregen + 1
        self.roundlab.text = str(self.currentround)
        
    def waves(self):
        if self.currentroundkills == self.roundkills and self.dea == 0:
            self.currentexp = self.currentexp + (3 * self.currentround)
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
            if monster.sprite.position.y <= 310 and self.state == 'attack' and self.rotationc >= 10:
                self.critchanceroll = random.randint(1, 100)
                if self.critchanceroll <= self.crit:
                    sound.play_effect('assets/Hit_2.caf')	
                    self.rubychance = random.randint(1, 100000)
                    if self.rubychance <= 10 + self.rubychanceadd:
                        self.currentrubies = self.currentrubies + 1
                        sound.play_effect('arcade:Explosion_6')
                    self.dmg = random.randint(globals.playerdmglowest + globals.playerdmglowest*(globals.playercritdmg/100), globals.playerdmghighest + globals.playerdmghighest*(globals.playercritdmg/100))
                    self.totaldmg = self.totaldmg + self.dmg
                    if len(self.dmglabels) < 15:
                        self.dmglabels.append(LabelNode(text = str(self.dmg),
                                      position = (self.screen_center_x - random.randint(1, 100) + random.randint(1, 100), random.randint(350,360)),
                                      color = '#b00000',
                                      alpha = 1.0,
                                      font = ('AvenirNext-Heavy', 15),
                                      parent = self))
                        
                else:
                    self.soundrandom = random.randint(1,2)
                    if self.soundrandom <= 2:
                        sound.play_effect('assets/Hit_2.caf')	
                    self.rubychance = random.randint(1, 100000)
                    if self.rubychance <= 10 + self.rubychanceadd:
                        self.currentrubies = self.currentrubies + 1
                        sound.play_effect('arcade:Explosion_6')
                    self.dmg = random.randint(globals.playerdmglowest, globals.playerdmghighest)
                    self.totaldmg = self.totaldmg + self.dmg
                    if len(self.dmglabels) < 15:
                        self.dmglabels.append(LabelNode(text = str(self.dmg),
                                      position = (self.screen_center_x - random.randint(1, 100) + random.randint(1, 100), random.randint(350,360)),
                                      color = '#ff0000',
                                      alpha = 1.0,
                                      font = ('AvenirNext-Heavy', 12),
                                      parent = self))
                monster.hp = monster.hp - int(self.dmg)
                if monster.hp <= 0:
                    monster.sprite.remove_from_parent()
                    self.Monsters.remove(monster)
                    self.health = min(self.health + float(round(((monster.hpmax * 10) * globals.playerlifesteal / 100)) / 10), (float(round(self.fullhp* 10) / 10)))
                    if len(self.lifesteal) < 8:
                        self.lifesteal.append(LabelNode(text = '+' + str(float(round(((monster.hpmax * 10) * globals.playerlifesteal / 100)) / 10)),
                                                    position = (self.screen_center_x - self.screen_center_x/2.5 - random.randint(0, int(self.rangeheal)) + random.randint(0, int(self.rangeheal) * 4), self.bar + 12),
                                      color = '#00ff59',
                                      alpha = 1.0,
                                      font = ('AvenirNext-Heavy', 7),
                                      parent = self))
                    self.currentexp = self.currentexp + int(round(random.randint(1,7) * self.currentround) * self.expmulti)
                    self.currentkills = self.currentkills + 1
                    self.currentroundkills = self.currentroundkills + 1
                    self.currentcoins = self.currentcoins + int(round(random.randint((2 + self.currentround),(9 + self.currentround)) / 2))
                            
    def regenpassive(self):
        if time.time() - self.regentime >= 0.1 and self.health < (float(round(self.fullhp* 10) / 10)) and self.health != 0:
            sound.play_effect('digital:TwoTone1')
            self.regentime = time.time()
            self.addheal = round((self.regen/10.0)*10) / 10
            self.health = self.health + self.addheal
            if self.health > (float(round(self.fullhp* 10) / 10)) and self.dea == 0:
                self.health = (float(round(self.fullhp* 10) / 10))
            self.regenover5.append(LabelNode(text = '+' + str(self.addheal),
                                      position = (self.screen_center_x + self.screen_center_x/2.5 + random.randint(0, int(self.rangeheal)) - random.randint(0, int(self.rangeheal) * 4), self.bar + 12),
                                      color = '#00ff16',
                                      alpha = 1.0,
                                      font = ('AvenirNext-Heavy', 7),
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
            if self.currentmana <= 100 and self.dea != 1:
                self.currentmana = self.currentmana + globals.managain
                if self.currentmana > 100:
                    self.currentmana = 100
            if self.currentdodge <= 100 and self.dea != 1:
                self.currentdodge = self.currentdodge + globals.energygain
                if self.currentdodge > 100:
                    self.currentdodge = 100
            self.passivecoins = time.time()
    def deadornah(self):
        if self.state != 'dead' and self.health > float(round(self.fullhp* 10) / 10):
            self.health = float(round(self.fullhp* 10) / 10)
        if self.health <= 0 and self.dea == 0:
            self.health = 0
            self.state = 'dead'
            self.dea = 1
            globals.playerexp = globals.playerexp + self.currentexp
            self.monsterspawned = self.roundkills 
            globals.coins = globals.coins + self.currentcoins
            globals.rubies = globals.rubies + self.currentrubies
            self.removescene = time.time()
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
    
    def terraremove(self):
        #MonsterSpawn
        for terraz in self.terra:
            if terraz.sprite.position.y <= -50:
                terraz.sprite.remove_from_parent()
                self.terra.remove(terraz)
                    
    def terramove(self):
        for posi in self.terra:
            if posi.sprite.position.x < self.screen_center_x + 60 and posi.sprite.position.x > self.screen_center_x - 60:
                posi.sprite.remove_from_parent()
                self.terra.remove(posi)
            posi.sprite.run_action(Action.move_to(posi.sprite.position.x, posi.sprite.position.y - self.scrollspeed, 0))
    def terraspawn(self):
        #MonsterSpawn
        if time.time() - self.terratime >= random.randint(1,5) * 1.5 * 0.95:
            self.add_terrain()
            self.terratime = time.time()
                    
    def add_terrain(self):
        obstacles = Terrain()
        self.terratype = random.randint(0,10)
        if self.terratype == 0:
            
            obstacles.sprite = SpriteNode('./assets/sprites/shrub.PNG',
                                    position = (random.randint(0, self.size_of_screen_x), self.size_of_screen_y + 100),
                                    scale = 1,
                                    alpha = 0.95,
                                    parent = self)
        elif self.terratype == 1:
            
            obstacles.sprite = SpriteNode('./assets/sprites/flowers.PNG',
                                    position = (random.randint(0, self.size_of_screen_x), self.size_of_screen_y + 100),
                                    scale = 1,
                                    alpha = 0.95,
                                    parent = self)
                                    
        elif self.terratype == 2:
            
            obstacles.sprite = SpriteNode('./assets/sprites/tree.PNG',
                                    position = (random.randint(0, self.size_of_screen_x), self.size_of_screen_y + 100),
                                    scale = 1.25,
                                    alpha = 0.95,
                                    parent = self)
                                    
        elif self.terratype == 3:
            
            obstacles.sprite = SpriteNode('./assets/sprites/rock2.PNG',
                                    position = (random.randint(0, self.size_of_screen_x), self.size_of_screen_y + 100),
                                    scale = 1,
                                    alpha = 0.95,
                                    parent = self)
                                    
        elif self.terratype == 4:
            
            obstacles.sprite = SpriteNode('./assets/sprites/log.PNG',
                                    position = (random.randint(0, self.size_of_screen_x), self.size_of_screen_y + 100),
                                    scale = 1,
                                    alpha = 0.95,
                                    parent = self)
                                    
        elif self.terratype == 5:
            
            obstacles.sprite = SpriteNode('./assets/sprites/rock3.PNG',
                                    position = (random.randint(0, self.size_of_screen_x), self.size_of_screen_y + 100),
                                    scale = 0.8,
                                    alpha = 0.95,
                                    parent = self)
        elif self.terratype == 6:
            
            obstacles.sprite = SpriteNode('./assets/sprites/unlitlantern.PNG',
                                    position = (random.randint(0, self.size_of_screen_x), self.size_of_screen_y + 100),
                                    scale = 1,
                                    alpha = 0.95,
                                    parent = self)
        elif self.terratype == 7:
            
            obstacles.sprite = SpriteNode('./assets/sprites/barrel.PNG',
                                    position = (random.randint(0, self.size_of_screen_x), self.size_of_screen_y + 100),
                                    scale = 1,
                                    alpha = 0.95,
                                    parent = self)
        elif self.terratype == 8:
            
            obstacles.sprite = SpriteNode('./assets/sprites/sack.PNG',
                                    position = (random.randint(0, self.size_of_screen_x), self.size_of_screen_y + 100),
                                    scale = 1,
                                    alpha = 0.95,
                                    parent = self)
        elif self.terratype == 9:
            
            obstacles.sprite = SpriteNode('./assets/sprites/shrub2.PNG',
                                    position = (random.randint(0, self.size_of_screen_x), self.size_of_screen_y + 100),
                                    scale = 1.4,
                                    alpha = 0.95,
                                    color = '#ff9975',
                                    parent = self)
        elif self.terratype == 10:
            
            obstacles.sprite = SpriteNode('./assets/sprites/shrub3.PNG',
                                    position = (random.randint(0, self.size_of_screen_x), self.size_of_screen_y + 100),
                                    scale = 1,
                                    alpha = 0.95,
                                    parent = self)
        self.terra.append(obstacles)
    
    def enraged(self):
        self.enragingtime = time.time()
        self.charater.scale = self.charater.scale + 0.5
        self.enrag = 1
        self.crit = 100
        self.fullhp = globals.fullhealth * 1.5
        self.regen = globals.overtimeregen * 3
        
    def add_monster(self):
        monster = MonsterObj()
        if random.randint(0,1) == 1:
            monster.hp = random.randint(40, 60) * self.currentround / 2
            monster.hpmax = monster.hp
            monster.sprite = SpriteNode('./assets/sprites/game/straightreaper.PNG',
                                    position = (random.randint(300, self.size_of_screen_x - 300), self.size_of_screen_y + 100),
                                    scale = 0.85,
                                    alpha = 0.95,
                                    parent = self)
        else:
            monster.hp = random.randint(10, 20) * self.currentround / 2
            monster.hpmax = monster.hp
            monster.sprite = SpriteNode('./assets/sprites/eyeball.PNG',
                                    position = (random.randint(300, self.size_of_screen_x - 300), self.size_of_screen_y + 100),
                                    scale = 0.75,
                                    alpha = 0.95,
                                    parent = self)
        self.Monsters.append(monster)
        monster.sprite.run_action(Action.move_to(self.screen_center_x + random.randint(0, 75) - random.randint(0, 75), 280, self.monster_attack_speed))
    
    
    def checkspellone(self):
        spellcast = Spells()
        #LifeShield
        if globals.spellone == 'assets/sprites/LifeShield.png':
            self.spellonemana = 15
            if self.currentmana - self.spellonemana < 0:
                pass
            else:
                self.currentmana = self.currentmana - self.spellonemana
                self.spellonecooldown = 20
                self.spellone.color = 'grey'
                self.health = self.health + int(self.fullhp/5)
                if self.health > self.fullhp:
                    self.health = self.fullhp
                spellcast.sprite = SpriteNode('assets/sprites/lifesshield.PNG',
                                             position = (self.charater.position.x, self.charater.position.y),
                                             scale = 0.2,
                                             alpha = 1,
                                             parent = self)
                self.lifeshield.append(spellcast)
                spellcast.sprite.run_action(Action.fade_to(0, 5))
                globals.playerarmor = 100
        elif globals.spellone == 'assets/sprites/LifeShieldv2.png':
            self.spellonemana = 12
            if self.currentmana - self.spellonemana < 0:
                pass
            else:
                self.currentmana = self.currentmana - self.spellonemana
                self.spellonecooldown = 15
                self.spellone.color = 'grey'
                self.health = self.health + int(self.fullhp/10)
                if self.health > self.fullhp:
                    self.health = self.fullhp
                spellcast.sprite = SpriteNode('assets/sprites/lifesshield.PNG',
                                             position = (self.charater.position.x, self.charater.position.y),
                                             scale = 0.2,
                                             alpha = 1,
                                             parent = self)
                self.lifeshield.append(spellcast)
                spellcast.sprite.run_action(Action.fade_to(0, 5))
                globals.playerarmor = 95
        elif globals.spellone == 'assets/sprites/LifeShieldv1.png':
            self.spellonemana = 15
            if self.currentmana - self.spellonemana < 0:
                pass
            else:
                self.spellonecooldown = 10
                self.spellone.color = 'grey'
                self.health = self.health + int(self.fullhp/20)
                if self.health > self.fullhp:
                    self.health = self.fullhp
                spellcast.sprite = SpriteNode('assets/sprites/lifesshield.PNG',
                                             position = (self.charater.position.x, self.charater.position.y),
                                             scale = 0.2,
                                             alpha = 1,
                                             parent = self)
                self.lifeshield.append(spellcast)
                spellcast.sprite.run_action(Action.fade_to(0, 5))
                globals.playerarmor = 90
        #FireBalls
        elif globals.spellone == 'assets/sprites/fireball-red-3.png':
            self.spellonemana = 30
            if self.currentmana - self.spellonemana < 0:
                pass
            else:
                self.fireballmulti = 2.5
                self.spellonecooldown = 20
                self.spellone.color = 'grey'
                spellcast.sprite = SpriteNode('assets/sprites/5.png',
                                             position = (self.charater.position.x, self.charater.position.y + 75),
                                             scale = 0.75,
                                             alpha = 0.75,
                                             parent = self)
                self.fireballs.append(spellcast)
                spellcast.sprite.run_action(Action.move_to(self.screen_center_x, self.size_of_screen_y + 200, 2.5))
        elif globals.spellone == 'assets/sprites/fireball-red-2.png':
            self.spellonemana = 20
            if self.currentmana - self.spellonemana < 0:
                pass
            else:
                self.fireballmulti = 2
                self.spellonecooldown = 25
                self.spellone.color = 'grey'
                spellcast.sprite = SpriteNode('assets/sprites/5.png',
                                             position = (self.charater.position.x, self.charater.position.y + 75),
                                             scale = 0.5,
                                             alpha = 0.75,
                                             parent = self)
                self.fireballs.append(spellcast)
                spellcast.sprite.run_action(Action.move_to(self.screen_center_x, self.size_of_screen_y + 200, 2.5))
        elif globals.spellone == 'assets/sprites/fireball-red-1.png':
            self.spellonemana = 10
            if self.currentmana - self.spellonemana < 0:
                pass
            else:
                self.fireballmulti = 1.5
                self.spellonecooldown = 30
                self.spellone.color = 'grey'
                spellcast.sprite = SpriteNode('assets/sprites/5.png',
                                             position = (self.charater.position.x, self.charater.position.y + 75),
                                             scale = 0.3,
                                             alpha = 0.75,
                                             parent = self)
                self.fireballs.append(spellcast)
                spellcast.sprite.run_action(Action.move_to(self.screen_center_x, self.size_of_screen_y + 200, 2.5))
        #FanOfKnives
        elif globals.spellone == 'assets/sprites/enchant-red-3.png':
            self.spellonemana = 30
            if self.currentmana - self.spellonemana < 0:
                pass
            else:
                self.spellonecooldown = 15
                self.spellone.color = 'grey'
                self.fanofknivesmulti = 3
                spellcast.sprite = SpriteNode('assets/sprites/fanofknives3.PNG',
                                             position = (self.charater.position.x, self.charater.position.y),
                                             scale = 0.15,
                                             alpha = 1,
                                             parent = self)
                self.fanofknives.append(spellcast)
                spellcast.sprite.run_action(Action.rotate_to(30, 3))
        elif globals.spellone == 'assets/sprites/enchant-red-2.png':
            self.spellonemana = 20
            if self.currentmana - self.spellonemana < 0:
                pass
            else:
                self.spellonecooldown = 20
                self.spellone.color = 'grey'
                self.fanofknivesmulti = 2
                spellcast.sprite = SpriteNode('assets/sprites/fanofknives2.PNG',
                                             position = (self.charater.position.x, self.charater.position.y),
                                             scale = 0.15,
                                             alpha = 1,
                                             parent = self)
                self.fanofknives.append(spellcast)
                spellcast.sprite.run_action(Action.rotate_to(30, 3))
        elif globals.spellone == 'assets/sprites/enchant-red-1.png':
            self.spellonemana = 10
            if self.currentmana - self.spellonemana < 0:
                pass
            else:
                self.spellonecooldown = 30
                self.spellone.color = 'grey'
                self.fanofknivesmulti = 1.25
                spellcast.sprite = SpriteNode('assets/sprites/fanofknives1.PNG',
                                             position = (self.charater.position.x, self.charater.position.y),
                                             scale = 0.15,
                                             alpha = 1,
                                             parent = self)
                self.fanofknives.append(spellcast)
                spellcast.sprite.run_action(Action.rotate_to(30, 3))
        
        self.sotimer = time.time()
        self.startingso = self.spellonecooldown
        
    def checkspelltwo(self):
        spellcast = Spells()
        #LifeShield
        if globals.spelltwo == 'assets/sprites/LifeShield.png':
            self.spelltwomana = 10
            if self.currentmana - self.spelltwomana < 0:
                pass
            else:
                self.spelltwo.color = 'grey'
                self.spelltwocooldown = 20
                self.health = self.health + int(self.fullhp/5)
                if self.health > self.fullhp:
                    self.health = self.fullhp
                spellcast.sprite = SpriteNode('assets/sprites/lifesshield.PNG',
                                             position = (self.charater.position.x, self.charater.position.y),
                                             scale = 0.2,
                                             alpha = 1,
                                             parent = self)
                self.lifeshield.append(spellcast)
                spellcast.sprite.run_action(Action.fade_to(0, 5))
                globals.playerarmor = 100
        elif globals.spelltwo == 'assets/sprites/LifeShieldv2.png':
            self.spelltwomana = 12
            if self.currentmana - self.spelltwomana < 0:
                pass
            else:
                self.spelltwocooldown = 15
                self.spelltwo.color = 'grey'
                self.health = self.health + int(self.fullhp/10)
                if self.health > self.fullhp:
                    self.health = self.fullhp
                spellcast.sprite = SpriteNode('assets/sprites/lifesshield.PNG',
                                             position = (self.charater.position.x, self.charater.position.y),
                                             scale = 0.2,
                                             alpha = 1,
                                             parent = self)
                self.lifeshield.append(spellcast)
                spellcast.sprite.run_action(Action.fade_to(0, 5))
                globals.playerarmor = 95
        elif globals.spelltwo == 'assets/sprites/LifeShieldv1.png':
            self.spelltwomana = 15
            if self.currentmana - self.spelltwomana < 0:
                pass
            else:
                self.spelltwo.color = 'grey'
                self.spelltwocooldown = 10
                self.health = self.health + int(self.fullhp/20)
                if self.health > self.fullhp:
                    self.health = self.fullhp
                spellcast.sprite = SpriteNode('assets/sprites/lifesshield.PNG',
                                             position = (self.charater.position.x, self.charater.position.y),
                                             scale = 0.2,
                                             alpha = 1,
                                             parent = self)
                self.lifeshield.append(spellcast)
                spellcast.sprite.run_action(Action.fade_to(0, 5))
                globals.playerarmor = 90
        #FireBalls
        elif globals.spelltwo == 'assets/sprites/fireball-red-3.png':
            self.spelltwomana = 30
            if self.currentmana - self.spelltwomana < 0:
                pass
            else:
                self.fireballmulti = 2.5
                self.spelltwocooldown = 20
                self.spelltwo.color = 'grey'
                spellcast.sprite = SpriteNode('assets/sprites/5.png',
                                             position = (self.charater.position.x, self.charater.position.y + 75),
                                             scale = 0.75,
                                             alpha = 0.75,
                                             parent = self)
                self.fireballs.append(spellcast)
                spellcast.sprite.run_action(Action.move_to(self.screen_center_x, self.size_of_screen_y + 200, 2.5))
        elif globals.spelltwo == 'assets/sprites/fireball-red-2.png':
            self.spelltwomana = 20
            if self.currentmana - self.spelltwomana < 0:
                pass
            else:
                self.spelltwo.color = 'grey'
                self.fireballmulti = 2
                self.spelltwocooldown = 25
                spellcast.sprite = SpriteNode('assets/sprites/5.png',
                                             position = (self.charater.position.x, self.charater.position.y + 75),
                                             scale = 0.5,
                                             alpha = 0.75,
                                             parent = self)
                self.fireballs.append(spellcast)
                spellcast.sprite.run_action(Action.move_to(self.screen_center_x, self.size_of_screen_y + 200, 2.5))
        elif globals.spelltwo == 'assets/sprites/fireball-red-1.png':
            self.spelltwomana = 10
            if self.currentmana - self.spelltwomana < 0:
                pass
            else:
                self.spelltwocooldown = 30
                self.fireballmulti = 1.5
                self.spelltwo.color = 'grey'
                spellcast.sprite = SpriteNode('assets/sprites/5.png',
                                             position = (self.charater.position.x, self.charater.position.y + 75),
                                             scale = 0.3,
                                             alpha = 0.75,
                                             parent = self)
                self.fireballs.append(spellcast)
                spellcast.sprite.run_action(Action.move_to(self.screen_center_x, self.size_of_screen_y + 200, 2.5))
        #FanOfKnives
        elif globals.spelltwo == 'assets/sprites/enchant-red-3.png':
            self.spelltwomana = 30
            if self.currentmana - self.spelltwomana < 0:
                pass
            else:
                self.fanofknivesmulti = 3
                self.spelltwocooldown = 15
                self.spelltwo.color = 'grey'
                spellcast.sprite = SpriteNode('assets/sprites/fanofknives3.PNG',
                                             position = (self.charater.position.x, self.charater.position.y),
                                             scale = 0.15,
                                             alpha = 1,
                                             parent = self)
                self.fanofknives.append(spellcast)
                spellcast.sprite.run_action(Action.rotate_to(30, 3))
        elif globals.spelltwo == 'assets/sprites/enchant-red-2.png':
            self.spelltwomana = 20
            if self.currentmana - self.spelltwomana < 0:
                pass
            else:
                self.fanofknivesmulti = 2
                self.spelltwocooldown = 20
                self.spelltwo.color = 'grey'
                spellcast.sprite = SpriteNode('assets/sprites/fanofknives2.PNG',
                                             position = (self.charater.position.x, self.charater.position.y),
                                             scale = 0.15,
                                             alpha = 1,
                                             parent = self)
                self.fanofknives.append(spellcast)
                spellcast.sprite.run_action(Action.rotate_to(30, 3))
        elif globals.spelltwo == 'assets/sprites/enchant-red-1.png':
            self.spelltwomana = 10
            if self.currentmana - self.spelltwomana < 0:
                pass
            else:
                self.spelltwocooldown = 30
                self.spelltwo.color = 'grey'
                self.fanofknivesmulti = 1.25
                spellcast.sprite = SpriteNode('assets/sprites/fanofknives1.PNG',
                                             position = (self.charater.position.x, self.charater.position.y),
                                             scale = 0.15,
                                             alpha = 1,
                                             parent = self)
                self.fanofknives.append(spellcast)
                spellcast.sprite.run_action(Action.rotate_to(30, 3))
        
        self.sttimer = time.time()
        self.startingst = self.spelltwocooldown
        
        
    def checkspellthree(self):
        spellcast = Spells()
        #LifeShield
        if globals.spellthree == 'assets/sprites/LifeShield.png':
            self.spellthreemana = 10
            if self.currentmana - self.spellthreemana < 0:
                pass
            else:
                self.spellthreecooldown = 20
                self.spellthree.color = 'grey'
                self.health = self.health + int(self.fullhp/5)
                if self.health > self.fullhp:
                    self.health = self.fullhp
                spellcast.sprite = SpriteNode('assets/sprites/lifesshield.PNG',
                                             position = (self.charater.position.x, self.charater.position.y),
                                             scale = 0.2,
                                             alpha = 1,
                                             parent = self)
                self.lifeshield.append(spellcast)
                spellcast.sprite.run_action(Action.fade_to(0, 5))
                globals.playerarmor = 100
        elif globals.spellthree == 'assets/sprites/LifeShieldv2.png':
            self.spellthreemana = 12
            if self.currentmana - self.spellthreemana < 0:
                pass
            else:
                self.spellthreecooldown = 15
                self.spellthree.color = 'grey'
                self.health = self.health + int(self.fullhp/10)
                if self.health > self.fullhp:
                    self.health = self.fullhp
                spellcast.sprite = SpriteNode('assets/sprites/lifesshield.PNG',
                                             position = (self.charater.position.x, self.charater.position.y),
                                             scale = 0.2,
                                             alpha = 1,
                                             parent = self)
                self.lifeshield.append(spellcast)
                spellcast.sprite.run_action(Action.fade_to(0, 5))
                globals.playerarmor = 95
        elif globals.spellthree == 'assets/sprites/LifeShieldv1.png':
            self.spellthreemana = 10
            if self.currentmana - self.spellthreemana < 0:
                pass
            else:
                self.spellthreecooldown = 10
                self.spellthree.color = 'grey'
                self.health = self.health + int(self.fullhp/20)
                if self.health > self.fullhp:
                    self.health = self.fullhp
                spellcast.sprite = SpriteNode('assets/sprites/lifesshield.PNG',
                                             position = (self.charater.position.x, self.charater.position.y),
                                             scale = 0.2,
                                             alpha = 1,
                                             parent = self)
                self.lifeshield.append(spellcast)
                spellcast.sprite.run_action(Action.fade_to(0, 5))
                globals.playerarmor = 90
        #FireBalls
        elif globals.spellthree == 'assets/sprites/fireball-red-3.png':
            self.spellthreemana = 30
            if self.currentmana - self.spellthreemana < 0:
                pass
            else:
                self.fireballmulti = 2.5
                self.spellthreecooldown = 20
                self.spellthree.color = 'grey'
                spellcast.sprite = SpriteNode('assets/sprites/5.png',
                                             position = (self.charater.position.x, self.charater.position.y + 75),
                                             scale = 0.75,
                                             alpha = 0.75,
                                             parent = self)
                self.fireballs.append(spellcast)
                spellcast.sprite.run_action(Action.move_to(self.screen_center_x, self.size_of_screen_y + 200, 2.5))
        elif globals.spellthree == 'assets/sprites/fireball-red-2.png':
            self.spellthreemana = 20
            if self.currentmana - self.spellthreemana < 0:
                pass
            else:
                self.fireballmulti = 2
                self.spellthreecooldown = 25
                self.spellthree.color = 'grey'
                spellcast.sprite = SpriteNode('assets/sprites/5.png',
                                             position = (self.charater.position.x, self.charater.position.y + 75),
                                             scale = 0.5,
                                             alpha = 0.75,
                                             parent = self)
                self.fireballs.append(spellcast)
                spellcast.sprite.run_action(Action.move_to(self.screen_center_x, self.size_of_screen_y + 200, 2.5))
        elif globals.spellthree == 'assets/sprites/fireball-red-1.png':
            self.spellthreemana = 10
            if self.currentmana - self.spellthreemana < 0:
                pass
            else:
                self.fireballmulti = 1.5
                self.spellthreecooldown = 30
                self.spellthree.color = 'grey'
                spellcast.sprite = SpriteNode('assets/sprites/5.png',
                                             position = (self.charater.position.x, self.charater.position.y + 75),
                                             scale = 0.3,
                                             alpha = 0.75,
                                             parent = self)
                self.fireballs.append(spellcast)
                spellcast.sprite.run_action(Action.move_to(self.screen_center_x, self.size_of_screen_y + 200, 2.5))
        #FanOfKnives
        elif globals.spellthree == 'assets/sprites/enchant-red-3.png':
            self.spellthreemana = 30
            if self.currentmana - self.spellthreemana < 0:
                pass
            else:
                self.spellthreecooldown = 15
                self.spellthree.color = 'grey'
                self.fanofknivesmulti = 3
                spellcast.sprite = SpriteNode('assets/sprites/fanofknives3.PNG',
                                             position = (self.charater.position.x, self.charater.position.y),
                                             scale = 0.15,
                                             alpha = 1,
                                             parent = self)
                self.fanofknives.append(spellcast)
                spellcast.sprite.run_action(Action.rotate_to(30, 3))
        elif globals.spellthree == 'assets/sprites/enchant-red-2.png':
            self.spellthreemana = 20
            if self.currentmana - self.spellthreemana < 0:
                pass
            else:
                self.spellthreecooldown = 20
                self.spellthree.color = 'grey'
                self.fanofknivesmulti = 2
                spellcast.sprite = SpriteNode('assets/sprites/fanofknives2.PNG',
                                             position = (self.charater.position.x, self.charater.position.y),
                                             scale = 0.15,
                                             alpha = 1,
                                             parent = self)
                self.fanofknives.append(spellcast)
                spellcast.sprite.run_action(Action.rotate_to(30, 3))
        elif globals.spellthree == 'assets/sprites/enchant-red-1.png':
            self.spellthreemana = 10
            if self.currentmana - self.spellthreemana < 0:
                pass
            else:
                self.spellthreecooldown = 30
                self.spellthree.color = 'grey'
                self.fanofknivesmulti = 1.25
                spellcast.sprite = SpriteNode('assets/sprites/fanofknives1.PNG',
                                             position = (self.charater.position.x, self.charater.position.y),
                                             scale = 0.15,
                                             alpha = 1,
                                             parent = self)
                self.fanofknives.append(spellcast)
                spellcast.sprite.run_action(Action.rotate_to(30, 3))
        
        self.sthtimer = time.time()
        self.startingsth = self.spellthreecooldown
    
    
    
    
    def spellcast(self):
        if len(self.lifeshield) > 0:
            for shield in self.lifeshield:
                if shield.sprite.alpha <= 0.05:
                    shield.sprite.remove_from_parent()
                    self.lifeshield.remove(shield)
                    globals.playerarmor = self.originarmor
        if len(self.fanofknives) > 0:
            for monster in self.Monsters:
                for fanofknive in self.fanofknives:
                    if fanofknive.sprite.rotation >= 30:
                        fanofknive.sprite.remove_from_parent()
                        self.fanofknives.remove(fanofknive)
                    if fanofknive.sprite.frame.intersects(monster.sprite.frame):
                        self.dmg = int(random.randint(globals.playerdmglowest, globals.playerdmghighest)/3.5 * self.fanofknivesmulti)
                        self.totaldmg = self.totaldmg + self.dmg
                        if len(self.dmglabels) < 10:
                            self.dmglabels.append(LabelNode(text = str(self.dmg),
                                      position = (monster.sprite.position.x - random.randint(1, 100) + random.randint(1, 100), monster.sprite.position.y),
                                      color = '#000000',
                                      alpha = 1.0,
                                      font = ('AvenirNext-Heavy', 12),
                                      parent = self))
                        monster.hp = monster.hp - self.dmg
                        if monster.hp <= 0:
                            monster.sprite.remove_from_parent()
                            self.Monsters.remove(monster)
                            self.health = min(self.health + (float(round(monster.hpmax * 10) / 10)) * globals.playerlifesteal / 100, (float(round(self.fullhp* 10) / 10)))
                            if len(self.lifesteal) < 8:
                                self.lifesteal.append(LabelNode(text = '+' + str(float(round((monster.hpmax * globals.playerlifesteal / 100) * 10) / 10)),
                                                    position = (self.screen_center_x - self.screen_center_x/2.5 - random.randint(0, int(self.rangeheal)) + random.randint(0, int(self.rangeheal) * 4), self.bar + 12),
                                                    color = '#00ff59',
                                                    alpha = 1.0,
                                                    font = ('AvenirNext-Heavy', 7),
                                                    parent = self))
                            self.currentexp = self.currentexp + int(round(random.randint(1,7) * self.currentround) * self.expmulti)
                            self.currentkills = self.currentkills + 1
                            self.currentroundkills = self.currentroundkills + 1
                            self.currentcoins = self.currentcoins + int(round(random.randint((2 + self.currentround),(9 + self.currentround)) / 2))
        if len(self.fireballs) > 0:
            for monster in self.Monsters:
                for fireball in self.fireballs:
                    if fireball.sprite.position.y >= self.size_of_screen_y + 100:
                        fireball.sprite.remove_from_parent()
                        self.fireballs.remove(fireball)
                    if fireball.sprite.frame.intersects(monster.sprite.frame):
                        self.dmg = int(random.randint(globals.playerdmglowest, globals.playerdmghighest)/2.5 * self.fireballmulti)
                        self.totaldmg = self.totaldmg + self.dmg
                        if len(self.dmglabels) < 10:
                            self.dmglabels.append(LabelNode(text = str(self.dmg),
                                      position = (monster.sprite.position.x - random.randint(1, 100) + random.randint(1, 100), monster.sprite.position.y),
                                      color = '#000000',
                                      alpha = 1.0,
                                      font = ('AvenirNext-Heavy', 12),
                                      parent = self))
                        monster.hp = monster.hp - self.dmg
                        if monster.hp <= 0:
                            monster.sprite.remove_from_parent()
                            self.Monsters.remove(monster)
                            self.health = min(self.health + float(round(monster.hpmax * 10) / 10) * globals.playerlifesteal / 100, (float(round(self.fullhp* 10) / 10)))
                            if len(self.lifesteal) < 8:
                                self.lifesteal.append(LabelNode(text = '+' + str(float(round((monster.hpmax * globals.playerlifesteal / 100) * 10) / 10)),
                                                    position = (self.screen_center_x - self.screen_center_x/2.5 - random.randint(0, int(self.rangeheal)) + random.randint(0, int(self.rangeheal) * 4), self.bar + 12),
                                                    color = '#00ff59',
                                                    alpha = 1.0,
                                                    font = ('AvenirNext-Heavy', 7),
                                                    parent = self))
                            self.currentexp = self.currentexp + int(round(random.randint(1,7) * self.currentround) * self.expmulti)
                            self.currentkills = self.currentkills + 1
                            self.currentroundkills = self.currentroundkills + 1
                            self.currentcoins = self.currentcoins + int(round(random.randint((2 + self.currentround),(9 + self.currentround)) / 2))
                            
        if self.spellonecooldown <= 0:
            self.spellone.color = '#e7e7e7'
            self.spellonetime.text = ''
        if self.spelltwocooldown <= 0:
            self.spelltwo.color = '#e7e7e7'
            self.spelltwotime.text = ''
        if self.spellthreecooldown <= 0:
            self.spellthree.color = '#e7e7e7'
            self.spellthreetime.text = ''
