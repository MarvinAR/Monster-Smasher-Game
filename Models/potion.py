import pygame

from pygame.sprite import Sprite

class Potion(Sprite):

	def __init__(self, Game):
		super().__init__()

		self.screen            = Game.screen
		self.screen_rect       = self.screen.get_rect()
		self.game_settings     = Game.game_settings

		self.image             = pygame.image.load('img/potion.png')
		self.image_rect        = self.image.get_rect()

		self.image_rect.bottom = self.image_rect.top

		self.y                 = self.image_rect.y

		self.update()

		self.hit = False
		self.show = False

	def update(self):
		self.y           += 2
		self.image_rect.y = self.y

	def show_potion(self):
		self.screen.blit(self.image, self.image_rect)