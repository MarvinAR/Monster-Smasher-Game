import pygame

from pygame.sprite import Sprite

class Human(Sprite):

	def __init__(self, Game):
		super().__init__()

		self.screen = Game.screen
		self.screen_rect = self.screen.get_rect()
		self.game_settings = Game.game_settings

		self.image = pygame.image.load('img/human.png')
		self.image_rect = self.image.get_rect()

		self.re_transform_scale()

		self.image_rect.bottom = self.screen_rect.top

		self.y = self.image_rect.y

		self.update()

		self.hit = False
		self.show = False

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

	def show_human(self):
		self.screen.blit(self.image, self.image_rect)