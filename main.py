import sys
import random as rd
import pygame
from GameInfo import GameInfo
from Button import Button

class Game:
    caption = "猜数字小游戏"
    screen = None
    fps = 60
    fclock = None
    runing = True
    game_start = False
    level_up = False
    game_over = False

    def __init__(self, game_info, submit_button):
        pygame.init()
        pygame.mixer.init()
        self.game_info = game_info
        self.submit_button = submit_button
        self.current_string = []
        self.rand_number = rd.randint(1, 100)
        self.show_info = 0
        self.level = 1
        self.current_submit = 0
        self.count = 10
        self.screen = pygame.display.set_mode([self.game_info.width, self.game_info.height], pygame.RESIZABLE)
        pygame.display.set_caption(self.caption)
        self.fclock = pygame.time.Clock()
        self.bg_img = pygame.image.load('./assets/bg/bg.png').convert()

    def event_process(self, event):
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # 全屏幕需要按esc退出
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_BACKSPACE:
                self.current_string = self.current_string[0:-1]
            elif event.unicode in "0123456789":
                self.current_string.append(event.unicode)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            print(mouse)
            if 190 < mouse[0] < 414 and 663 < mouse[1] < 733 and self.level_up == True:
                print('level game')
                self.show_info = 0
                self.level_up = False
                self.runing = True
                return
            if 122 < mouse[0] < 535 and 292 < mouse[1] < 587 and self.game_start == False:
                print('start game')
                self.game_start = True
            elif 122 < mouse[0] < 535 and 673 < mouse[1] < 756 and self.game_start == False:
                sys.exit()
            elif 122 < mouse[0] < 535 and 469 < mouse[1] < 559 and self.game_start == True:
                print(self.current_string)
                if self.current_string:
                    self.current_submit = int(''.join(self.current_string))
                    self.check(self.current_submit)
                    self.current_string = []
        # 屏幕大小改变
        elif event.type == pygame.VIDEORESIZE:
            self.game_info.width, self.game_info.height = event.size[0], event.size[1]
            self.screen = pygame.display.set_mode([self.game_info.width, self.game_info.height], pygame.RESIZABLE)

    def check(self, number):
        print(number)
        print(self.rand_number)
        if number > self.rand_number:
            self.show_info = 1
            self.count -= 1
        elif number < self.rand_number:
            self.show_info = 2
            self.count -= 1
        else:
            self.show_info = 3
            self.count -= 1

    def up_level(self, level):
        self.level = level
        self.rand_number = rd.randint(1, 100 + level * 5)

    def draw(self):
        # 画背景
        game_bg_surface = pygame.transform.scale(self.game_info.game_bg_img,
                                                 (self.game_info.width, self.game_info.height))
        self.screen.blit(game_bg_surface, (0, 0))

    def draw_game(self):
        if self.game_over:
            game_over_surface = pygame.transform.scale(self.game_info.game_over_img,
                                                       (self.game_info.width, self.game_info.height))
            game_over_rect = game_over_surface.get_rect()
            self.screen.blit(game_over_surface, game_over_rect)
            return
        # 画背景
        game_bg_surface = pygame.transform.scale(self.game_info.game_bg_img_01,
                                                 (self.game_info.width, self.game_info.height))
        self.screen.blit(game_bg_surface, (0, 0))
        self.screen.blit(self.submit_button.surface, self.submit_button.rect)
        pygame.draw.rect(self.screen, (252, 211, 55),
                         ((self.screen.get_width() / 2) - 200,
                          (self.screen.get_height() / 2) - 80,
                          400, 60), 0)
        fontobject = pygame.font.Font("./assets/fonts/汉标粗黑体.ttf", 28)
        self.screen.blit(fontobject.render("请输入：" + ''.join(self.current_string), 1, (255, 255, 255)),
                         ((self.screen.get_width() / 2) - 200, (self.screen.get_height() / 2) - 68))
        self.game_info.draw_text(f'第{self.level}关' + f',猜测范围【1到{100 + (self.level - 1) * 10}】', self.screen)
        self.game_info.draw_text('当前分数：' + str(self.game_info.score), self.screen, [10, 50])

        if self.show_info == 1:
            self.game_info.draw_text(f'提示：【{self.current_submit}】太大了,还剩{self.count}次机会', self.screen, [10, 100])
        elif self.show_info == 2:
            self.game_info.draw_text(f'提示：【{self.current_submit}】太小了,还剩{self.count}次机会', self.screen, [10, 100])

        elif self.show_info == 3:
            self.game_info.score += 10
            self.up_level(self.level + 1)
            level_bg_surface = pygame.transform.scale(self.game_info.game_bg_img_level,
                                                      (self.game_info.width, self.game_info.height))
            self.screen.blit(level_bg_surface, (0, 0))
            self.level_up = True
            self.runing = False
            self.count = 10
        if self.count <= 0:
            self.game_over = True

    def run(self):
        while True:
            for event in pygame.event.get():
                self.event_process(event)
            if self.runing:
                if self.game_start:
                    self.draw_game()
                else:
                    self.draw()
                pygame.display.flip()
            self.fclock.tick(self.fps)

def main():
    game_info = GameInfo()
    submit_button = Button()
    game = Game(game_info, submit_button)
    pygame.mixer.music.load("./assets/sound/bg.mp3")  # 加载音乐文件
    pygame.mixer.music.play(-1, 0)  # 开始播放音乐流
    game.run()

if __name__ == '__main__':
    main()
