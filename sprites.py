from settings import *

class Person:
    def __init__(self):
        self.image = person_image
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2)
        self.speed_x = randint(1, 2)
        self.speed_y = randint(1, 2)
        
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.touch()
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def touch(self):
        if self.rect.top <= 0:
            self.speed_y = randint(1, 2)
        if self.rect.bottom >= SCREEN_SIZE[1]:
            self.speed_y = -1 * randint(1, 2)
        if self.rect.right >= SCREEN_SIZE[0]:
            self.speed_x = -1 * randint(1, 2)
        if self.rect.left <= 0:
            self.speed_x = randint(1, 2)
