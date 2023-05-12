import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

	def __init__(self, info_game):
		super().__init__()
		self.screen = info_game.screen
		self.settings = info_game.game_setting
		self.image = pygame.image.load('img/alien.PNG')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)

	def update(self):
		self.x += self.settings.alien_speed * self.settings.alien_army_direction
		self.rect.x = self.x

	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if (self.rect.right >= screen_rect.right) or (self.rect.left <= screen_rect.left):
			return True