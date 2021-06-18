import pygame.font 

class Button:

	def __init__(self, Game, msg):
		self.screen             = Game.screen
		self.screen_rect        = self.screen.get_rect()

		self.width, self.height = 280, 75
		self.button_color       = (135, 163, 255)
		self.text_color         = (255, 255, 255)
		self.font               = pygame.font.SysFont(None, 48)

		self.rect               = pygame.Rect(0,0, self.width, self.height)
		self.rect.center        = self.screen_rect.center
		self.rect.y -= 90

		self._show_msg(msg)

	def _show_msg(self, msg):
		self.msg_image             = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect        = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def _draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)


class Button_2:

	def __init__(self, Game, msg):
		self.screen             = Game.screen
		self.screen_rect        = self.screen.get_rect()

		self.width, self.height = 280, 75
		self.button_color       = (135, 163, 255)
		self.text_color         = (255, 255, 255)
		self.font               = pygame.font.SysFont(None, 48)

		self.rect               = pygame.Rect(0,0, self.width, self.height)
		self.rect.center        = self.screen_rect.center
		self.rect.y += 70

		self._show_msg(msg)

	def _show_msg(self, msg):
		self.msg_image             = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect        = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def _draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)


class Button_3:

	def __init__(self, Game, msg):
		self.screen             = Game.screen
		self.screen_rect        = self.screen.get_rect()

		self.width, self.height = 280, 75
		self.button_color       = (135, 163, 255)
		self.text_color         = (255, 255, 255)
		self.font               = pygame.font.SysFont(None, 48)

		self.rect               = pygame.Rect(0,0, self.width, self.height)
		self.rect.center        = self.screen_rect.center
		self.rect.y += 230

		self._show_msg(msg)

	def _show_msg(self, msg):
		self.msg_image             = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect        = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def _draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)

class Button_4:

	def __init__(self, Game, msg):
		self.screen             = Game.screen
		self.screen_rect        = self.screen.get_rect()

		self.width, self.height = 50, 50
		self.button_color       = (255,204,102)
		self.text_color         = (0, 0, 0)
		self.font               = pygame.font.SysFont(None, 48, bold=True)

		self.rect               = pygame.Rect(0,0, self.width, self.height)
		self.rect.midtop        = self.screen_rect.midtop
		self.rect.y += 30
		self.rect.x -= 10

		self._show_msg(msg)

	def _show_msg(self, msg):
		self.msg_image             = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect        = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def _draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)

class Button_5:

	def __init__(self, Game, msg):
		self.screen             = Game.screen
		self.screen_rect        = self.screen.get_rect()

		self.width, self.height = 35, 35
		self.button_color       = (19,92,8)
		self.text_color         = (255, 255, 255)
		self.font               = pygame.font.SysFont(None, 48)

		self.rect               = pygame.Rect(0,0, self.width, self.height)
		self.rect.topright      = self.screen_rect.topright

		self._show_msg(msg)

	def _show_msg(self, msg):
		self.msg_image             = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect        = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
		self.msg_image_rect.y += 1

	def _draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)