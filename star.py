import pygame
from pygame.sprite import Sprite

class Star(Sprite):
	def __init__(self, info_game):
		super().__init__()
		self.screen = info_game.screen

		self.image = pygame.image.load('img/star.png')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)