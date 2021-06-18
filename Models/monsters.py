import pygame

from pygame.sprite import Sprite

class TinyMonster(Sprite):

	def __init__(self, Game):
		super().__init__()

		self.screen = Game.screen
		self.screen_rect = self.screen.get_rect()
		self.game_settings = Game.game_settings

		self.image = pygame.image.load('img/tiny.png')
		self.image_rect = self.image.get_rect()

		self.re_transform_scale()

		self.image_rect.bottom = self.screen_rect.top

		self.y = self.image_rect.y

		self.update()

		self.hit = False
		self.show = False

	def re_transform_scale(self):
		self.image = pygame.transform.scale(self.image, (self.image_rect.width//4, self.image_rect.height//4))
		self.image_rect = self.image.get_rect()

	def update(self):
		self.y += self.game_settings.monsters_speed
		self.image_rect.y = self.y
		'''
		if self.image_rect.top >= self.screen_rect.bottom:
			self.reposition()

	def reposition(self):
		self.image_rect.top = 0
		self.y = self.image_rect.top
		'''

	def show_tinyMonster(self):
		self.screen.blit(self.image, self.image_rect)

class MediumMonster(Sprite):

	def __init__(self, Game):
		super().__init__()

		self.screen = Game.screen
		self.screen_rect = self.screen.get_rect()
		self.game_settings = Game.game_settings

		self.image = pygame.image.load('img/medium.png')
		self.image_rect = self.image.get_rect()

		self.re_transform_scale()

		self.image_rect.bottom = self.screen_rect.top
		self.image_rect.y -= 5

		self.y = self.image_rect.y

		self.update()

		self.hit = False

	def re_transform_scale(self):
		self.image = pygame.transform.scale(self.image, (self.image_rect.width//2, self.image_rect.height//2))
		self.image_rect = self.image.get_rect()

	def update(self):
		self.y += self.game_settings.monsters_speed
		self.image_rect.y = self.y
		'''
		if self.image_rect.top >= self.screen_rect.bottom:
			self.reposition()

	def reposition(self):
		self.image_rect.top = 0
		self.y = self.image_rect.top
		'''

	def show_mediumMonster(self):
		self.screen.blit(self.image, self.image_rect)

class LargeMonster(Sprite):

	def __init__(self, Game):
		super().__init__()
		
		self.screen = Game.screen
		self.screen_rect = self.screen.get_rect()
		self.game_settings = Game.game_settings

		self.image = pygame.image.load('img/large.png')
		self.image_rect = self.image.get_rect()

		self.re_transform_scale()

		self.image_rect.bottom = self.screen_rect.top
		self.image_rect.y -= 5
		
		self.y = self.image_rect.y

		self.update()

		self.hit = False

	def re_transform_scale(self):
		self.image = pygame.transform.scale(self.image, (3*self.image_rect.width//4, 3*self.image_rect.height//4))
		self.image_rect = self.image.get_rect()

	def update(self):
		self.y += self.game_settings.monsters_speed
		self.image_rect.y = self.y
		'''
		if self.image_rect.top >= self.screen_rect.bottom:
			self.reposition()

	def reposition(self):
		self.image_rect.top = 0
		self.y = self.image_rect.top
		'''

	def show_largeMonster(self):
		self.screen.blit(self.image, self.image_rect)