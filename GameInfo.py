import pygame

class GameInfo:
    width = 600
    height = 790
    score = 0
    game_over_img = pygame.image.load("./assets/bg/gameover.png")
    game_bg_img = pygame.image.load("./assets/bg/bg.png")
    game_bg_img_01 = pygame.image.load("./assets/bg/bg01.png")
    game_bg_img_level = pygame.image.load("./assets/bg/level.png")

    def draw_text(self,text, screen,topleft = [10, 10]):
        font = pygame.font.Font("./assets/fonts/汉标粗黑体.ttf", 36)
        survived_text = font.render(str(text), True, (255, 255, 255))
        text_rect = survived_text.get_rect()
        text_rect.topleft = topleft
        screen.blit(survived_text, text_rect)

