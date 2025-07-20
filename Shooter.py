import pygame
import random 

from file_helper import *


destroyed = 0
skipped = 0
class Enemy:
        def __init__(self, speed, x, y, width, height, skin):
            self.speed = speed 
            self.skin = pygame.image.load(skin)
            self.skin = pygame.transform.scale(self.skin, [width, height])
            self.hitbox = self.skin.get_rect()
            self.hitbox.x = x
            self.hitbox.y = y
            

        def draw(self, window):
            window.blit(self.skin, self.hitbox)
            

        def update(self):
            global skipped
            self.hitbox.y += self.speed
            if self.hitbox.y >= 500:
                self.hitbox.y -= self.hitbox.y
                self.hitbox.x = random.randint(150, 550)
                skipped += 1
                
class Bullet:
        def __init__(self, speed, x, y, width, height, skin):
            self.speed = speed 
            self.skin = pygame.image.load(skin)
            self.skin = pygame.transform.scale(self.skin, [width, height])
            self.hitbox = self.skin.get_rect()
            self.hitbox.x = x
            self.hitbox.y = y

        def draw(self, window):
            window.blit(self.skin, self.hitbox)

        def update(self):
            self.hitbox.y -= self.speed

class Rocket:
        def __init__(self, speed, x, y, width, height, skin):
            self.speed = speed 
            self.skin = pygame.image.load(skin)
            self.skin = pygame.transform.scale(self.skin, [width, height])
            self.hitbox = self.skin.get_rect()
            self.hitbox.x = x
            self.hitbox.y = y
            self.bullets = []

        def draw(self, window):
            window.blit(self.skin, self.hitbox)
            for bullet in self.bullets:
                bullet.draw(window)

        def update(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]:
                self.hitbox.x += self.speed
            if keys[pygame.K_a]:
                self.hitbox.x -= self.speed
            if keys[pygame.K_SPACE]:
                self.bullets.append(Bullet(5, self.hitbox.x+20, self.hitbox.y, 10, 5, "bullet.png"))

            for bullet in self.bullets:
                bullet.update()
            


def start_game():
        global destroyed,skipped



    

    


    
    
        

        pygame.init()
        window = pygame.display.set_mode([700, 500])
        clock = pygame.time.Clock()
        data = read_file()
        #save_file(data)
        hero = Rocket(10, 102, 436, 50, 50, data["skin"])
        ufos = [
            Enemy(1, 206, 175, 50, 50, "ufo.png"),
            Enemy(3, 284, 194, 50, 50, "ufo.png"),
            Enemy(1, 366, 202, 50, 50, "ufo.png"),
            Enemy(2, 450, 209, 50, 50, "ufo.png"),
            Enemy(1, 275, 290, 50, 50, "ufo.png"),
            Enemy(1, 338, 168, 50, 50, "ufo.png"),
            Enemy(3, 400, 281, 50, 50, "ufo.png")

        ]

        galaxy_jpg = pygame.image.load("galaxy.jpg")
        galaxy_jpg = pygame.transform.scale(galaxy_jpg, [700,500])


        skipped_text = pygame.font.Font(None, 32).render("Пропущено:" + str(skipped), True, [255, 255, 255])
        destroyed_text = pygame.font.Font(None, 32).render("Знищено:" + str(destroyed), True, [255, 255, 255])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())


            for bullet in hero.bullets[:]:
                for ufo in ufos[:]:
                    if bullet.hitbox.colliderect(ufo.hitbox):
                        hero.bullets.remove(bullet)
                        ufo.hitbox.x = random.randint(0, 600) 
                        ufo.hitbox.y = -100
                        destroyed += 1
                        data = read_file()
                        data["money"] += 1
                        save_file(data)
                        break



            hero.update()
            for ufo in ufos:
                ufo.update()

            destroyed_text = pygame.font.Font(None, 32).render("Знищено:" + str(destroyed), True, [255, 255, 255])
            skipped_text = pygame.font.Font(None, 32).render("Пропущено:" + str(skipped), True, [255, 255, 255])
            window.fill([123, 123, 123])
            window.blit(galaxy_jpg, [0,0])
            window.blit(skipped_text, [0, 0])
            window.blit(destroyed_text, [7, 30])
            hero.draw(window)
            for ufo in ufos:
                ufo.draw(window)
            pygame.display.flip()

            clock.tick(60)


            