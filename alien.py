#coding=utf-8
import  pygame
from pygame.sprite import Sprite
class Alien(Sprite):
	def __init__(self,ai_settings,screen):
		"""初始化机器人并设置其起始位置"""
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# 加载外星人图像，并设置其rect属性
		self.image = pygame.image.load('images/alien.bmp')
		self.image = pygame.transform.scale(self.image,(25,28))
		self.rect = self.image.get_rect()

		# 每个外星人一开始都在屏幕左上角附近
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# 存储外星人精确位置
		self.x = float(self.rect.x)
	def blitme(self):
		"""在指定位置绘制外星人"""
		self.screen.blit(self.image,self.rect)
	def draw_alien(self):
		pygame.draw.rect(self.screen,self.rect)

	def check_edgs(self,aliens,ai_settings):
		#screen_rect = self.screen.get_rect
		for alien in aliens:
			if alien.rect.x + alien.rect.width >= ai_settings.screen_width:
				return True
			elif alien.rect.x < 0:
				return True

	def update(self):
		"""向右移动外星人"""
		self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
		self.rect.x = self.x
