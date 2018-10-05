#coding=utf-8
import sys
import pygame
from alien import  Alien
from bullet import Bullet
def check_keydown_events(event,ai_settings,screen,ship,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,bullets,screen,ship)
	elif event.key == pygame.K_q:
		sys.exit
def fire_bullet(ai_settings,bullets,screen,ship):
	# 创建一颗子弹，并让其加入到编组Bullets中,并且限制子弹数量
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)
def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
def check_events(ai_settings,screen,ship,bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
def update_screen(ai_Settings,screen,ship,aliens,bg_color,bullets):
	screen.fill(bg_color)
	# 在飞船和外星人后面绘制所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)

def update_bullets(aliens,bullets,ai_settings,screen,ship):
	bullets.update()
	for bullet in bullets:
		if bullet.rect.y < 0:
			bullets.remove(bullet)
	collisions = pygame.sprite.groupcollide(bullets,aliens,False,True)
	if len(aliens) == 0:
		bullets.empty()
		creat_fleet(ai_settings,screen,aliens,ship)
	#让最近绘制的屏幕可见
	pygame.display.flip()


def get_number_aliens_x(ai_settings,alien_width):
	#计算每行可放下多少个外星人
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x) / (2 * alien_width)
	return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
	available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
	number_rows = int(available_space_y/(2 * alien_height))
	return number_rows
def creat_fleet(ai_settings,screen,aliens,ship):
	"""创建外星人群"""
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width) - 2
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			"""创建一个外星人并放在当前行"""
			alien = Alien(ai_settings, screen)
			alien_width = alien.rect.width
			alien.x = alien_width + 2 * alien_width * alien_number
			alien.rect.x = alien.x
			alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
			aliens.add(alien)

def check_fleet_edgs(ai_settings,aliens):
	for alien in aliens.sprites():
		ai_settings.fleet_direction *= -1
		if alien.check_edgs(aliens,ai_settings):
			for alien in aliens.sprites():
				alien.rect.y += ai_settings.fleet_drop_speed
			break

def update_aliens(ai_settings,aliens):
	check_fleet_edgs(ai_settings,aliens)
	aliens.update()
