import pygame as pg
from random import randint

def load_image(file, size):
    image = pg.image.load(file)
    image = pg.transform.scale(image, size)
    return image
    
SCREEN_SIZE = (1400, 800)
PERSON_SIZE = (SCREEN_SIZE[0] // 8, SCREEN_SIZE[0] // 8)

bg_image = load_image("images/fon1.jfif", SCREEN_SIZE)
person_image = load_image("images/cara_fea1.png", PERSON_SIZE)
