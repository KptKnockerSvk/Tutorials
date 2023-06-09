from .game_element import GameElement
import pygame

class Ship(GameElement):
    def handle_keys(self, keys, ship_speed, game_res_x):
        if keys[pygame.K_LEFT] and self.pos[0] > ship_speed:
            self.movement((-ship_speed, 0))
        if keys[pygame.K_RIGHT] and self.pos[0] < game_res_x - self.image.get_width:
            self.movement((ship_speed, 0))

        if keys[pygame.K_RIGHT]:
            if ship_coox < 440:
                ship_coox += 5