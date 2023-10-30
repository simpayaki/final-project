from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (55,55))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys [K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.side = "right"
        if self.rect.x >= win_width - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption('Labirint')
background = transform.scale(image.load('background.jpg'), (win_width, win_height))

player = Player('gg.png', 5, win_height - 80, 4)
monster = Enemy('enemy.png', win_width - 80, 280, 2)
final = GameSprite('son.png', win_width - 120, win_height - 80, 0)

w1 = Wall(154, 205, 50, 100, 20 , 580, 10)
w2 = Wall(154, 205, 50, 100, 480, 580, 10)
w3 = Wall(154, 205, 50, 100, 20 , 10, 380)
w4=Wall(154,205,50,100,390,370,10)
w5=Wall(154,205,50,550,105,10,160)
w6=Wall(154,205,50,550,350,10,130)
w7=Wall(154,205,50,670,30,10,450)
w8=Wall(154,205,50,460,350,10,50)
w9=Wall(154,205,50,370,255,190,10)
w10=Wall(154,205,50,370,255,10,60)
w11=Wall(154,205,50,210,305,160,10)
w12=Wall(154,205,50,210,105,10,200)
w13=Wall(154,205,50,290,30,10,200)
w14=Wall(154,205,50,290,180,170,10)
w15=Wall(154,205,50,380,105,170,10)
game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 70)
win = font.render('YOU ESCAPED!', True, (255, 195, 0))
lose = font.render('YOU DIED!', True, (180, 0, 0))

mixer.init()
mixer.music.load('epicmusic.ogg')
mixer.music.play()

plach = mixer.Sound('plach.ogg')
bam = mixer.Sound('vistrel.ogg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background,(0,0))
        player.update()
        monster.update()

        player.reset()
        monster.reset()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()
        w13.draw_wall()
        w14.draw_wall()
        w15.draw_wall()
        if sprite.collide_rect(player,monster) or sprite.collide_rect(player,w1) or sprite.collide_rect(player,w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player,w4) or sprite.collide_rect(player,w5) or sprite.collide_rect(player,w6) or sprite.collide_rect(player,w7) or sprite.collide_rect(player,w8) or sprite.collide_rect(player,w9) or sprite.collide_rect(player,w10) or sprite.collide_rect(player,w11) or sprite.collide_rect(player,w12) or sprite.collide_rect(player,w13) or sprite.collide_rect(player,w14) or sprite.collide_rect(player,w15):
            finish = True
            window.blit(lose, (200,200))
            bam.play()

        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200,200))
            plach.play()

    display.update()
    clock.tick(FPS)