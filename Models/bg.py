import pygame

class Bg:

	def __init__(self, Game):
		self.screen = Game.screen
		self.game_settings = Game.game_settings

		self.screen_rect = Game.screen.get_rect()

		self.image = pygame.image.load("img/bg.JPG")

		self.rect = self.image.get_rect()

		self.rect.right = self.screen_rect.right
		self.rect.bottom = self.screen_rect.bottom

	def update(self):
		self.rect.y += self.game_settings.bg_speed
		self.blitme()
		if self.rect.top == self.screen_rect.top:
			self.rect.bottom = self.screen_rect.bottom
			self.rect.y -= 2

	def blitme(self):
		self.screen.blit(self.image, self.rect)