
class GameStatistics:

	def __init__(self, info_game):
		self.setting = info_game.game_setting
		self.reset_statistics()

		self.game_active = False
		self.high_score = 0

	def reset_statistics(self):
		self.my_shipP1_life = self.setting.ship_life
		self.current_level_score = 0
		self.score = 0
		self.level = 0