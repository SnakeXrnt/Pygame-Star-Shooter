import pygame 

class Ship:

	def __init__(self, info_game):

		self.screen = info_game.screen
		self.setting = info_game.game_setting

		self.screen_rect = info_game.screen.get_rect()

		self.image = pygame.image.load("img/ship.PNG")

		self.rect = self.image.get_rect()
		#self.rect.midbottom = (self.screen_rect.midbottom)
		#self.rect.x = 0.5*(self.rect.x)
		#self.x = float(self.rect.x)
		#self.y = float(self.rect.y)
		self.reset_position_ship()

		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		if self.moving_right and (self.rect.right < self.screen_rect.right):
			self.x += self.setting.ship_speed
		if self.moving_left and (self.rect.left > 0):
			self.x -= self.setting.ship_speed
		if self.moving_up and (self.rect.top > 0):
			self.y -= self.setting.ship_speed
		if self.moving_down and (self.rect.bottom < self.screen_rect.bottom):
			self.y += self.setting.ship_speed

		self.rect.x = self.x
		self.rect.y = self.y

	def reset_position_ship(self):
		self.rect.midbottom = (self.screen_rect.midbottom)
		self.rect.x = 0.5*(self.rect.x)
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def blitme(self):
		self.screen.blit(self.image, self.rect)