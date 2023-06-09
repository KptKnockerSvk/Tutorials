import pygame
from config.config import consts
import sys
from src.game_element import GameElement\

from src.ship import Ship\

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode(consts.GAME_RES)

    bg = GameElement(consts.BG_BASE_POS, consts.BG_IMAGE)
    ship = Ship(consts.SHIP_SPAWNN, consts.SHIP_IMAGE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        ship.handle_keys(keys, consts.SHIP_SPEED, consts.GAME_RES[0])

        bg.draw(window)
        ship.draw(window)
        
        pygame.display.update
        clock.tick(consts.GAME_FPS)