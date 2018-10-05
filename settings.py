#coding=utf-8、

class Setting():
	"""存储外星人入侵中若有设置的类"""
	def __init__(self):
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (230,230,230)
		self.ship_speed_factor = 3
		#子弹设置
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullets_allowed = 3
		#外星人设置
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 1
		# fleet_direction为1表示向由移动 为-1表示向坐移动
		self.fleet_direction = 1
