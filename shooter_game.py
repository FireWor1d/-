from pygame import *
from random import randint

init()

clock = time.Clock()

window = display.set_mode((700,500))

display.set_caption('TheALONEFENIXProduct')

background = transform.scale(image.load('galaxy.jpg'),(700,500))
sprite1 = transform.scale(image.load('ufo.png'),(50,50))
sprite2 = transform.scale(image.load('rocket.png'),(50,50))

lifes = 0


font = font.SysFont('Arial', 30)
win = font.render('YOU LOSE!', True, (255,215,0))

mixer.music.load('space.ogg')
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, img,x, y, w, h, speed):
        super().__init__()
        self.w = w
        self.h = h
        self.image = transform.scale(image.load(img), (self.w,self.h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def render(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Rocket(GameSprite):
    def moove(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 650:
            self.rect.x += self.speed

class Ufo(GameSprite):    
    def update(self):
        global lifes
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.rect.x = randint(0,700)
            self.rect.y = -100
            lifes += 1

    def updatesss(self):
        global finish
        global lifes
        if lifes >= 5:
            window.blit(win, (420, 150))
            finish = True
            
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()

class Asteroid(GameSprite):
    def spawn(self):
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.rect.x = randint(0,700)
            self.rect.y = -100


    
            



finish = False

score = 0


rocket = Rocket('rocket.png', 300, 400, 50, 50, 10)
ufo = Ufo('ufo.png', 250, 76, 50, 50, 1)
ufo2 = Ufo('ufo.png', 200, 76, 50, 50, 1)
ufo3 = Ufo('ufo.png', 250, 16, 50, 50, 1)
ufo4 = Ufo('ufo.png', 250, 176, 50, 50, 1)
ufo5 = Ufo('ufo.png', 150, 76, 50, 50, 1)

asteroid1 = Asteroid('asteroid.png', 225,86,30,30,3)  
asteroid2 = Asteroid('asteroid.png', 195,56,30,30,3)
asteroids = sprite.Group()
asteroids.add(asteroid1)
asteroids.add(asteroid2)
asteroids.draw(window)

life = GameSprite('lifffe.png', 30, 30, 30, 30, 0)
life2 = GameSprite('lifffe.png', 65, 30, 30, 30, 0)
life3 = GameSprite('lifffe.png', 100, 30, 30, 30, 0)
life4 = GameSprite('lifffe.png', 135, 30, 30, 30, 0)
life5 = GameSprite('lifffe.png', 170, 30, 30, 30, 0)

life6 = GameSprite('jj.png', 170, 30, 30, 30, 0)
life7 = GameSprite('jj.png', 135, 30, 30, 30, 0)
life8 = GameSprite('jj.png', 100, 30, 30, 30, 0)
life9 = GameSprite('jj.png', 65, 30, 30, 30, 0)


ufos = sprite.Group()
ufos.add(ufo)
ufos.add(ufo2)
ufos.add(ufo3)
ufos.add(ufo4)
ufos.add(ufo5)
ufos.update()
ufos.draw(window)


game = True


bullets = sprite.Group()



while game:
    keys_pressed = key.get_pressed()

    window.blit(background,(0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False

        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                bullets.add(Bullet('bullet.png', rocket.rect.centerx        -7, rocket.rect.top, 30, 15, 30))



    if not finish: 
        sprite.groupcollide(bullets,ufos,True,True)
        if sprite.spritecollide(rocket,ufos,True):
            lifes += 1  
        if sprite.spritecollide(rocket,asteroids,True):
            lifes += 1

        if lifes == 0:
            life.render()
            life2.render()
            life3.render()
            life4.render()
            life5.render()

        if lifes == 1:
            life.render()
            life2.render()
            life3.render()
            life4.render()
            life6.render()

        if lifes == 2:
            life.render()
            life2.render()
            life3.render()
            life6.render()
            life7.render()

        if lifes == 3:
            life.render()
            life2.render()
            life6.render()
            life7.render()
            life8.render()

        if lifes == 4:
            life.render()
            life6.render()
            life7.render()
            life8.render()
            life9.render()


        
            




        for bullet in bullets:
            bullet.render()

        rocket.render()
        rocket.moove()
        bullets.draw(window)
        bullets.update()

        for asteroid in asteroids:
            asteroid.render()
            asteroid.spawn()

        for ufo in ufos:
            ufo.render()
            ufo.update()
            ufo.updatesss()
        if len(ufos) < 3:
            ufos.add(Ufo('ufo.png', randint(10,630), 76, 50, 50, 1 ))
        ufos.update()

        '''ufo.rect.x = randint(0,700 - ufo.w)
                    ufo.rect.y = -100
                    score += 1'''

        
        '''if sprite.collide_rect(rocket, ufo2):
            ufo.rect.x = randint(0,700 - ufo.w)
            ufo.rect.y = -100

        
        if sprite.collide_rect(rocket, ufo3):
            ufo.rect.x = randint(0,700 - ufo.w)
            ufo.rect.y = -100


        if sprite.collide_rect(rocket, ufo4):
            ufo.rect.x = randint(0,700 - ufo.w)


        if sprite.collide_rect(rocket, ufo5):
            ufo.rect.x = randint(0,700 - ufo.w)
            ufo.rect.y = -100'''

    if finish:
        window.blit(win, (420, 150))
        if keys_pressed[K_r]:
            finish = False
            lifes = 0


    clock.tick(75)
    display.update()
