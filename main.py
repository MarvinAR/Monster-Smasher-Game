import pygame
import sys
import os
from datetime import datetime
from random import randint
from json import dump
from time import sleep

from Controller import settings, button
from Controller.stats import GameStatistics
from Controller.score import Scoreboard

from Models.monsters import TinyMonster, MediumMonster, LargeMonster
from Models.bg import Bg
from Models.life import Life
from Models.human import Human
from Models.potion import Potion

from tkinter import Tk, Label
from tkinter import messagebox as Msg
from PIL import Image, ImageTk

class Game:

	def __init__(self):
		pygame.init()

		#########################################
		# OBJECT YANG INVISIBLE BEHIND THE SCREEN
		#########################################

		self.game_settings = settings.Settings()
		self.screen = pygame.display.set_mode([self.game_settings.screen_width, self.game_settings.screen_height])

		#***************************************************#
		# Group OBJEK / MODELS IN OUR GAME (OBJECT IN OBJECT)
		#***************************************************#
		self.create_tiny_monster = False
		self.create_medium_monster = False
		self.create_large_monster = False
		self.create_human = False
		self.create_potion = False

		self.game_tiny_monster = pygame.sprite.Group()
		self.game_medium_monster = pygame.sprite.Group()
		self.game_large_monster = pygame.sprite.Group()
		self.game_human = pygame.sprite.Group()
		self.game_potion = pygame.sprite.Group()

		self.stats = GameStatistics(self)
		self.score = Scoreboard(self)

		####################################################

		self.title = pygame.display.set_caption(self.game_settings.title)
		self.bg_screen = Bg(self)

		self.play_button = button.Button(self, "PLAY")
		self.reset_button = button.Button_2(self, "RESET")
		self.exit_button = button.Button_3(self, "EXIT")
		self.pause_button = button.Button_4(self, "||")
		self.help_button = button.Button_5(self, "?")

		self.life = Life(self)

		self.running = True
		self.counter = 0

		self.potion_pressed = 0
		self.time_now = 0

	#####################
	# PROPERTY GAME UTAMA
	#####################

	def run_game(self):
		while self.running:
			self.rg_check_events()

			if self.stats.game_active:
				self.bg_screen.update()

				self.rg_game_over_check()

				tiny_monsters = self.game_tiny_monster.sprites()
				for tinyMonster in tiny_monsters:
					tinyMonster.update()

				medium_monsters = self.game_medium_monster.sprites()
				for mediumMonster in medium_monsters:
					mediumMonster.update()

				large_monsters = self.game_large_monster.sprites()
				for largeMonster in large_monsters:
					largeMonster.update()

				people = self.game_human.sprites()
				for person in people:
					person.update()

				potions = self.game_potion.sprites()
				for potion in potions:
					potion.update()

				self.beyond_the_screen_check()

			self.rg_update_screen()

	def rg_check_events(self):
		events = pygame.event.get()
		#print(events)

		for event in events:
			if event.type == pygame.QUIT:
				self.running = False
			elif event.type == pygame.KEYDOWN:
				self.rg_e_check_keydown_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				self.rg_check_mouse_buttondown(event.button)

	def rg_e_check_keydown_events(self, event):
		if event.key == pygame.K_q:
			sys.exit()

	def rg_check_mouse_buttondown(self, event_button):
		if event_button == 1:
			mouse_pos = pygame.mouse.get_pos()
			monster_hit = pygame.mouse.get_pos()
			self._check_play_button(mouse_pos)
			self._check_monsters_hit(monster_hit)
			self._check_pause_button(mouse_pos)

			if not self.stats.game_active:
				self._check_reset_button(mouse_pos)
				self._check_exit_button(mouse_pos)
				self._check_help_button(mouse_pos)

	def rg_update_screen(self):
		self.bg_screen.blitme()
		
		if not self.stats.game_active:
			self.play_button._draw_button()
			self.reset_button._draw_button()
			self.exit_button._draw_button()
			img_menu = pygame.image.load('img/main_menu.png')
			img_rect_menu = img_menu.get_rect()
			self.screen.blit(img_menu, img_rect_menu)
			self.help_button._draw_button()

		if self.stats.game_active:
			self.update_tiny_monsters()
			self.update_medium_monsters()
			self.update_large_monsters()
			self.update_human()
			self.update_potion()
			self.score.create_cover(self)
			self.pause_button._draw_button()
			self.score.draw_score()
			self.show_healthbar()
				
		pygame.display.flip()

	def rg_game_over_check(self):
		if self.game_settings.life == 0:
			self.stats.game_active = False
			python = sys.executable
			os.execl(python, python, *sys.argv)

	########
	# LIFE #
	########

	def show_healthbar(self):
		if self.game_settings.life !=0:
			self.life.show_life_background()
			self.life.show_string()
			if self.game_settings.life == 1:
				self.life.show_red()
			if self.game_settings.life == 2:
				self.life.show_yellow()
			if self.game_settings.life == 3:
				self.life.show_green()

	#################
	 #Tiny Monsters#
	#################
	def update_tiny_monsters(self):
		self.show_tinyMons_oneByOne()
		tiny_monsters = self.game_tiny_monster.sprites()
		
		for tinyMonster in tiny_monsters:
				tinyMonster.show_tinyMonster()

	def show_tinyMons_oneByOne(self):
		now = datetime.now()
		self.current_time = now - self.stats.start_time
		#print(self.current_time.seconds)
		if self.current_time.seconds > 1:

			if self.current_time.seconds % 2 == 0 and self.create_tiny_monster == False:
				self.create_tinyMons_oneByOne()
				self.create_tiny_monster = True
				#print('create')

			elif self.current_time.seconds % 2 != 0 and self.create_tiny_monster == True:
				self.create_tiny_monster = False

	def create_tinyMons_oneByOne(self):
		tiny = TinyMonster(self)
		tiny.image_rect.x = randint(0, self.game_settings.screen_width-50)
		tiny.image_rect.y = 75
		self.game_tiny_monster.add(tiny)

	#################
	#Medium Monsters#
	#################
	def update_medium_monsters(self):
		self.show_mediumMons_oneByOne()
		medium_monsters = self.game_medium_monster.sprites()
		
		for mediumMonster in medium_monsters:
			mediumMonster.show_mediumMonster()

	def show_mediumMons_oneByOne(self):
		if self.current_time.seconds > 2 :
			if self.current_time.seconds % 3 == 0 and self.create_medium_monster == False:
				self.create_mediumMons_oneByOne()
				self.create_medium_monster = True

			elif self.current_time.seconds % 3 != 0 and self.create_medium_monster == True:
				self.create_medium_monster = False

	def create_mediumMons_oneByOne(self):
		medium = MediumMonster(self)
		medium.image_rect.x = randint(0, self.game_settings.screen_width-75)
		self.game_medium_monster.add(medium)

	#################
	#Large Monsters#
	#################
	def update_large_monsters(self):
		self.show_largeMons_oneByOne()
		large_monsters = self.game_large_monster.sprites()
		
		for largeMonster in large_monsters:
			largeMonster.show_largeMonster()

	def show_largeMons_oneByOne(self):
		if self.current_time.seconds > 4:

			if self.current_time.seconds % 5 == 0 and self.create_large_monster == False:
				self.create_largeMons_oneByOne()
				self.create_large_monster = True

			elif self.current_time.seconds % 5 != 0 and self.create_large_monster == True:
				self.create_large_monster = False

	def create_largeMons_oneByOne(self):
		large = LargeMonster(self)
		large.image_rect.x = randint(0, self.game_settings.screen_width-200)
		self.game_large_monster.add(large)

	#################
		#Human#
	#################
	def update_human(self):
		self.show_human_oneByOne()
		people = self.game_human.sprites()
		
		for person in people:
			person.show_human()

	def show_human_oneByOne(self):
		now = datetime.now()
		self.current_time = now - self.stats.start_time
		#print(self.current_time.seconds)
		if self.current_time.seconds > 9:

			if self.current_time.seconds % 10 == 0 and self.create_human == False:
				self.create_human_oneByOne()
				self.create_human = True

			elif self.current_time.seconds % 10 != 0 and self.create_human == True:
				self.create_human = False

	def create_human_oneByOne(self):
		human = Human(self)
		human.image_rect.x = randint(0, self.game_settings.screen_width-50)
		self.game_human.add(human)

	#################
		#Potion#
	#################
	def update_potion(self):
		self.show_potion_oneByOne()
		potions = self.game_potion.sprites()
		
		for potion in potions:
			potion.show_potion()

	def show_potion_oneByOne(self):

		if self.stats.level % 2 == 0 and self.create_potion == False:
			self.create_potion_oneByOne()
			self.create_potion = True

		elif self.stats.level % 2 != 0 and self.create_potion == True:
			self.create_potion = False

	def create_potion_oneByOne(self):
		potion = Potion(self)
		potion.image_rect.x = randint(0, self.game_settings.screen_width-50)
		self.game_potion.add(potion)


	#############
	#Play Button#
	#############

	def _check_play_button(self, mouse_pos):
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		status = self.stats.game_active

		if button_clicked and not status:
			self.stats.game_active = True

			if self._check_pause_button(mouse_pos):
				self.stats.reset_statistics()

			self.score.show_score()
			self.score.check_high_score()

	#############
	#RESET Button#
	#############

	def _check_reset_button(self, mouse_pos):
		button_clicked = self.reset_button.rect.collidepoint(mouse_pos)

		if button_clicked:
			Tk().withdraw()
			result_user = Msg.askyesno('Confirmation !', "Are you sure to reset your highscore that you've made so far?")
			
			if result_user == True:
				with open('highscore.json', "w") as f:
					self.stats.high_score = 0
					dump(self.stats.high_score,f)

			self.stats.reset_statistics()

			self.score.show_score()
			self.score.check_high_score()


	#############
	#EXIT Button#
	#############

	def _check_exit_button(self, mouse_pos):
		button_clicked = self.exit_button.rect.collidepoint(mouse_pos)

		if button_clicked:
			Tk().withdraw()
			result_user = Msg.askyesno('Confirmation !', 'Are you sure to exit?')
			
			if result_user == True:
				quit()
			
	#######
	#Pause#
	#######

	def _check_pause_button(self, mouse_pos):
		button_clicked = self.pause_button.rect.collidepoint(mouse_pos)

		if button_clicked:
			self.stats.game_active = False

	######
	#Help#
	######

	def _check_help_button(self, mouse_pos):
		button_clicked = self.help_button.rect.collidepoint(mouse_pos)

		if button_clicked:
			window = Tk()
			window.title("Directions")

			title1 = Label(window, text='About Game', font=('arial', 18, 'bold'))
			title1.grid(column = 2, row = 0)

			title2 = Label(window, text='Monsters', font=('arial', 18, 'bold'))
			title2.grid(column = 1, row = 0)

			title3 = Label(window, text='RARE Entity', font=('arial', 18, 'bold'))
			title3.grid(column = 4, row = 0)

			title4 = Label(window, text='Info', font=('arial', 18, 'bold'))
			title4.grid(column = 2, row = 2)

			open_tiny_image = Image.open('tinyImg/tiny.png')
			tiny_image_done = ImageTk.PhotoImage(open_tiny_image)
			tiny_image_label = Label(window, image=tiny_image_done)
			tiny_image_label.grid(column = 0, row = 1)

			tiny_description = """
Stone Golem a.k.a Tiny Monster
Killed : Score +15
Passed : Score -5, Life -1
			"""

			tiny_description_label = Label(window, text=tiny_description, font=('arial', 12))
			tiny_description_label.grid(column = 1, row = 1)

			open_med_image = Image.open('tinyImg/medium.png')
			med_image_done = ImageTk.PhotoImage(open_med_image)
			med_image_label = Label(window, image=med_image_done)
			med_image_label.grid(column = 0, row = 2)

			med_description = """
Mythical Wolf a.k.a Medium Monster
Killed : Score +10
Passed : Score -10, Life -1
			"""

			med_description_label = Label(window, text=med_description, font=('arial', 12))
			med_description_label.grid(column = 1, row = 2)

			open_large_image = Image.open('tinyImg/large.png')
			large_image_done = ImageTk.PhotoImage(open_large_image)
			large_image_label = Label(window, image=large_image_done)
			large_image_label.grid(column = 0, row = 3)

			large_description = """
Demon Dragon a.k.a Large Monster
Killed : Score +5
Passed : Score -15, Life -1
			"""

			large_description_label = Label(window, text=large_description, font=('arial', 12))
			large_description_label.grid(column = 1, row = 3)

			open_boss_image = Image.open('tinyImg/bos.png')
			boss_image_done = ImageTk.PhotoImage(open_boss_image)
			boss_image_label = Label(window, image=boss_image_done)
			boss_image_label.grid(column = 3, row = 1)

			boss_description = """
Prehistoric Giant Turtle a.k.a Boss
Not Available in Game
Bcz Technical Problem
			"""

			boss_description_label = Label(window, text=boss_description, font=('arial', 12))
			boss_description_label.grid(column = 4, row = 1)

			open_human_image = Image.open('tinyImg/innocent.png')
			human_image_done = ImageTk.PhotoImage(open_human_image)
			human_image_label = Label(window, image=human_image_done)
			human_image_label.grid(column = 3, row = 2)

			human_description = """
Human a.k.a Innocent
Killed : Score -10, Life -1
Passed : Score +15, Life +1
			"""

			human_description_label = Label(window, text=human_description, font=('arial', 12))
			human_description_label.grid(column = 4, row = 2)

			open_potion_image = Image.open('tinyImg/potion.png')
			potion_image_done = ImageTk.PhotoImage(open_potion_image)
			potion_image_label = Label(window, image=potion_image_done)
			potion_image_label.grid(column = 3, row = 3)

			potion_description = """
Freeze Time Potion
Tapped : Time Freeze
Duration : at least 2 seconds
Tips : Tap after 2 seconds, tap anywhere to continue.
			"""

			potion_description_label = Label(window, text=potion_description, font=('arial', 12))
			potion_description_label.grid(column = 4, row = 3)

			tips_description = """
This is basically a tapping game.
In this game, you only have 3 lives.
Monsters, potions, innocents will fall from the top of the screen.
Tap them to get points, but don't tap the innocent
because you will gain some points and restore 1 life.
			"""

			tips_description_label = Label(window, text=tips_description, font=('Comic Sans Ms', 10))
			tips_description_label.grid(column = 2, row = 1)

			about_description = """
Developed by Marvin AR and Luigi E
Antah Berantah
Contact : -1 - 2345 - 6789
Since December 2020
© Claim 2021 Project. All rights reserved. 
			"""

			about_description_label = Label(window, text=about_description, font=('Comic Sans Ms', 15))
			about_description_label.grid(column = 2, row = 3)

			window.mainloop()

	def _check_monsters_hit(self, monster_hit):
		for tinyMonster in self.game_tiny_monster.copy():
			if tinyMonster.image_rect.collidepoint(monster_hit):
				tinyMonster.hit = True

			if tinyMonster.hit == True:
				self.game_tiny_monster.remove(tinyMonster)

				self.update_level()
				self.update_score_tiny()


		for mediumMonster in self.game_medium_monster.copy():
			if mediumMonster.image_rect.collidepoint(monster_hit):
				mediumMonster.hit = True

			if mediumMonster.hit == True:
				self.game_medium_monster.remove(mediumMonster)

				self.update_level()
				self.update_score_medium()


		for largeMonster in self.game_large_monster.copy():
			if largeMonster.image_rect.collidepoint(monster_hit):
				largeMonster.hit = True

			if largeMonster.hit == True:
				self.game_large_monster.remove(largeMonster)

				self.update_level()
				self.update_score_large()

		for human in self.game_human.copy():
			if human.image_rect.collidepoint(monster_hit):
				human.hit = True

			if human.hit == True:
				self.game_human.remove(human)

				self.update_score_human()

		for potion in self.game_potion.copy():
			if potion.image_rect.collidepoint(monster_hit):
				potion.hit = True

			if potion.hit == True:
				self.game_potion.remove(potion)

				self.potion_pressed = pygame.time.get_ticks()

				self.game_settings.bg_speed = 0
				self.game_settings.monsters_speed = 0

		self.time_now = pygame.time.get_ticks()

		if self.time_now - self.potion_pressed >= 2000:
			self.game_settings.bg_speed = 2
			self.game_settings.monsters_speed = 2

	def update_score_tiny(self):
		self.stats.score += 15
		self.score.show_score()
		self.score.check_high_score()

		self.stats.saveData()

	def update_score_medium(self):
		self.stats.score += 10
		self.score.show_score()
		self.score.check_high_score()

		self.stats.saveData()

	def update_score_large(self):
		self.stats.score += 5
		self.score.show_score()
		self.score.check_high_score()

		self.stats.saveData()

	def update_score_human(self):
		self.stats.score -= 10
		self.score.show_score()
		self.score.check_high_score()

		self.game_settings.life -= 1

		self.stats.saveData()

	def update_level(self):
		self.counter += 1

		if self.counter % 10 == 0:
			self.stats.level += 1
			self.score.show_level()

	def beyond_the_screen_check(self):
		for tinyMonster in self.game_tiny_monster.copy():
			if tinyMonster.image_rect.top >= 613:
				#print(self.game_settings.life)
				self.stats.score -= 5

				self.score.show_score()
				self.score.check_high_score()

				self.game_tiny_monster.remove(tinyMonster)
				self.game_settings.life -= 1

		for mediumMonster in self.game_medium_monster.copy():
			if mediumMonster.image_rect.top >= 613:
				#print(self.game_settings.life)
				self.stats.score -= 10

				self.score.show_score()
				self.score.check_high_score()

				self.game_medium_monster.remove(mediumMonster)
				self.game_settings.life -= 1

		for largeMonster in self.game_large_monster.copy():
			if largeMonster.image_rect.top >= 613:
				#print(self.game_settings.life)
				self.stats.score -= 15

				self.score.show_score()
				self.score.check_high_score()

				self.game_large_monster.remove(largeMonster)
				self.game_settings.life -= 1

		for human in self.game_human.copy():
			if human.image_rect.top >= 613:
				#print(self.game_settings.life)
				self.stats.score += 15

				self.score.show_score()
				self.score.check_high_score()

				self.game_human.remove(human)
				self.game_settings.life += 1

				if self.game_settings.life > 3:
					self.game_settings.life = 3



theGame = Game()
theGame.run_game()