import pygame.font
from pygame.sprite import Group


class Scoreboard:

	def __init__(self, info_game):
		self.info_game   = info_game
		self.screen      = info_game.screen
		self.screen_rect = self.screen.get_rect()

		self.settings    = info_game.game_settings
		self.stats       = info_game.stats


		self.text_color  = (255, 204, 102)
		self.font        = pygame.font.SysFont(None, 25)

		#self.show_score()
		#self.show_high_score()
		#self.show_level()

	def show_score(self):
		round_score                 = round(self.stats.score)
		score_string                = "Score         : "+"{:,}".format(round_score)
		self.score_image            = self.font.render(score_string, True, self.text_color, None)

		self.score_rect_image       = self.score_image.get_rect()
		self.score_rect_image.left  = self.screen_rect.left + 10
		self.score_rect_image.top   = 10

	def draw_score(self):
		self.show_score()
		self.show_high_score()
		self.show_level()
		self.screen.blit(self.score_image, self.score_rect_image)
		self.screen.blit(self.high_score_image, self.high_score_rect_image)
		self.screen.blit(self.level_image, self.level_rect_image)

	def show_high_score(self):
		round_high_score                = round(self.stats.high_score)
		high_score_string               = "High Score : "+"{:,}".format(round_high_score)
		self.high_score_image           = self.font.render(high_score_string, True, self.text_color, None)

		self.high_score_rect_image      = self.high_score_image.get_rect()
		self.high_score_rect_image.left = self.screen_rect.left + 10
		self.high_score_rect_image.top  = 40

	def show_level(self):
		rounded_level              = round(self.stats.level)
		level_string               = ("Level          : "+str(rounded_level))
		self.level_image           = self.font.render(level_string, True, self.text_color, None)

		self.level_rect_image      = self.level_image.get_rect()
		self.level_rect_image.left = self.screen_rect.left + 10
		self.level_rect_image.top  = 70

	def check_high_score(self):
		if self.stats.score > self.stats.high_score:
			self.stats.high_score  = self.stats.score
			self.show_high_score()
			
	def create_cover(self, info_game):
		self.screen             = info_game.screen
		self.screen_rect        = self.screen.get_rect()

		self.width, self.height = 400, 90
		self.rect_color         = (135, 124, 103)

		self.rect               = pygame.Rect(0,0, self.width, self.height)
		self.rect.midtop        = self.screen_rect.midtop

		self.screen.fill(self.rect_color, self.rect)
