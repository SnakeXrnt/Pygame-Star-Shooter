import pygame.font


class Scoreboard:

	def __init__(self, info_game):
		self.screen = info_game.screen
		self.screen_rect = self.screen.get_rect()

		self.settings = info_game.game_setting
		self.stats = info_game.my_statistics


		self.text_color = (255, 0, 0)
		self.font = pygame.font.SysFont(None, 48)

		self.show_score()
		self.show_high_score()

	def show_score(self):
		score_string = str(self.stats.score)
		self.score_image = self.font.render(score_string, True, self.text_color, self.settings.bg_color)

		self.score_rect_image = self.score_image.get_rect()
		self.score_rect_image.right = self.screen_rect.right - 30
		self.score_rect_image.top = 10

	def draw_score(self):
		self.screen.blit(self.score_image, self.score_rect_image)
		self.screen.blit(self.high_score_image, self.high_score_rect_image)
		self.screen.blit(self.level_image,self.level_rect_image)

	def show_high_score(self):
		round_high_score = round(self.stats.high_score , -1)
		high_score_string = "{:,}".format(round_high_score)
		self.high_score_image = self.font.render(high_score_string, True, self.text_color, self.settings.bg_color)
		self.high_score_rect_image = self.high_score_image.get_rect()
		self.high_score_rect_image.midtop = self.screen_rect.midtop

	def check_high_score(self):
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.show_high_score()

	def show_level(self):
		level_string = str(self.stats.level)
		self.level_image = self.font.render(level_string , True , self.text_color, self.settings.bg_color)
		self.level_rect_image = self.level_image.get_rect()
		self.level_rect_image.right = self.screen_rect.right - 30 
		self.level_rect_image.top = 40 