import pygame

class Settings:

	def __init__(self):
		#setting game
		self.screen_width = 800
		self.screen_height = 600
		self.title = "*Alien Game*"
		self.bg_color = [230, 230, 230]
		self.bg_image = pygame.image.load("img/bg_image.jpg")

		#setting ship
		#self.ship_speed = 2
		self.ship_life = 5

		#setting bullet
		#self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_limit = 300

		#setting alien
		#self.alien_speed = 1.0
		self.alien_army_drop_speed = 10.0
		#self.alien_army_direction = 1 # 1 right , -1 left


		#scaling level
		self.speedup_level = 1.5
		self.score_scale = 2.0

		self.init_dynamic_settings()

	def init_dynamic_settings(self):
		self.ship_speed = 2
		self.bullet_speed = 1.0
		self.alien_speed = 1.0
		self.alien_points = 50

		self.alien_army_direction = 1 # 1 right , -1 left

	def increase_speed(self):
		self.ship_speed *= self.speedup_level
		self.bullet_speed *= self.speedup_level
		self.alien_speed *= self.speedup_level