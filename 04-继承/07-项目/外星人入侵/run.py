import sys
import pygame
from setting import Settings
from ship import Ship
import functions as fun
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
    pygame.init()
    set = Settings()
    screen = pygame.display.set_mode((set.screen_width,set.screen_height))
    pygame.display.set_caption('外星人入侵')

    stats = GameStats(set)
    ship = Ship(set,screen)
    bullets = Group()
    aliens = Group()
    fun.create_fleet(set,screen,ship,aliens)

    while True:
        fun.check_events(set,screen,ship,bullets)
        if stats.game_active:
            ship.update()
            fun.update_bullets(set,screen,ship,aliens,bullets)
            fun.update_aliens(set,stats,screen,ship,aliens,bullets)
        fun.update_screen(set,screen,ship,bullets,aliens)
run_game()