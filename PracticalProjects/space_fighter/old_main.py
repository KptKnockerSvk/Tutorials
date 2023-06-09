import pygame
import sys
import random
from config.config import consts



def generate_meteor(meteor_image):
    return {
        "mask": pygame.mask.from_surface(meteor_image),
        "x": random.choice(range(10, 440, 80)),
        "y": random.choice(range(-10,-500,-50))
    }

def check_collision(mask1, mask2, mask1_coord, mask2_coord):
    x_off = mask2_coord[0] - mask1_coord[0]
    y_off = mask2_coord[1] - mask1_coord[1]
    if mask1.overlap(mask2,(x_off, y_off)):
        return True
    else:
        return False


if __name__ == "__main__":
    pygame.init()

    clock = pygame.time.Clock()
    bg = pygame.image.load(consts.BG_IMAGE)
    ship = pygame.image.load(consts.SHIP_IMAGE)
    meteor_img = pygame.image.load(consts.METEOR_IMAGE)
    game_font = pygame.font.SysFont(consts.FONT_TYPE, consts.FONT_SIZE)

    ship_mask = pygame.mask.from_surface(ship)

    ship_coox = 250
    ship_cooy = 720

    win = pygame.display.set_mode((500, 800))

    score = 0
    meteors = []
    meteor_speed = 0
    meteor_incr = 3
    meteor_count = 4
    end = False

    while True:
        score_text = game_font.render(f"Score: {score}", True, (255,255,255))

        if len(meteors) == 0:
            meteor_speed += 1
            meteor_count += meteor_incr
            for i in range(meteor_count):
                meteors.append(generate_meteor(meteor_img))
            
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if ship_coox > 10:
                ship_coox -= 5
        if keys[pygame.K_RIGHT]:
            if ship_coox < 440:
                ship_coox += 5
                    

        win.blit(bg, (0,0))
        win.blit(ship, (ship_coox, ship_cooy))

        if not end:
            for meteor in meteors[:]:
                win.blit(meteor_img,(meteor["x"], meteor["y"]))
                meteor["y"] += meteor_speed
                if meteor["y"] > 800:
                    score += 1
                    meteors.remove(meteor)
                if check_collision(ship_mask, meteor["mask"], (ship_coox, ship_cooy), (meteor["x"], meteor["y"])):
                    print("End")
                    end = True
        if end:
            end_text = game_font.render(f"Game over: {score}", True, (255,255,255))
            win.blit(end_text, (200,400))
        win.blit(score_text, (300,10))
        pygame.display.update()
        clock.tick(60)