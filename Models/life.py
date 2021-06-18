import pygame
import pygame.font

class Life:

	def __init__(self, Game):

		self.screen              = Game.screen
		self.game_settings       = Game.game_settings
		self.screen_rect         = self.screen.get_rect()
		self.font                = pygame.font.SysFont('Comic Sans MS', 22, bold=True)
		self.string_color        = (255,204,102)

		self.green_life_image    = pygame.Rect(0,0, 150, 25)
		self.yellow_life_image   = pygame.Rect(0,0, 100, 25)
		self.red_life_image      = pygame.Rect(0,0, 50, 25)
		self.life_background     = pygame.Rect(0,0, 160, 35)

		self.green_life_image.topright = self.screen_rect.topright
		self.green_life_image.x -= 20
		self.green_life_image.y += 50

		self.yellow_life_image.topright = self.screen_rect.topright
		self.yellow_life_image.x -= 70
		self.yellow_life_image.y += 50

		self.red_life_image.topright = self.screen_rect.topright
		self.red_life_image.x -= 120
		self.red_life_image.y += 50

		self.life_background.topright = self.screen_rect.topright
		self.life_background.x -= 15
		self.life_background.y += 45

	def show_string(self):
		string                          = "HEALTH BAR"
		self.string_image               = self.font.render(string, True, self.string_color, None)

		self.string_rect_image          = self.string_image.get_rect()
		self.string_rect_image.topright = self.screen_rect.topright
		self.string_rect_image.x -= 22
		self.string_rect_image.y += 10

		self.screen.blit(self.string_image, self.string_rect_image)


	def show_life_background(self):
		pygame.draw.rect(self.screen, (0,0,0), self.life_background)

	def show_green(self):
		pygame.draw.rect(self.screen, (0,255,0), self.green_life_image)

	def show_yellow(self):
		pygame.draw.rect(self.screen, (255, 196, 0), self.yellow_life_image)

	def show_red(self):
		pygame.draw.rect(self.screen, (255,0,0), self.red_life_image)
