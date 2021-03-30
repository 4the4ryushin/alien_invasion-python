class settings():
	def __init__(self):
		self.screen_width=800
		self.screen_height=500
		self.bg_color=(230,230,230)
		self.ship_speed=0.6
		self.bullet_speed=0.666
		self.bullet_width=3
		self.bullet_height=12
		self.bullet_color=60,60,60
		self.bullets_allowed=4
		self.alien_speed=0.8
		self.fleet_drop_speed=8
		self.fleet_direction=1 #  fleet_direction of 1 represents right; -1 represents left
		self.ship_limit=3
		#how quickly game speed up
		self.speedup_scale=1.1
		self.score_scale=1.5
		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		self.ship_speed=0.6
		self.bullet_speed=0.666
		self.alien_speed=0.8
		self.fleet_direction=1
		self.alien_points=50

	def increase_speed(self):
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points*self.score_scale)





		

