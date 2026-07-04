import pygame
from os.path import join

def load_image(*path: str) -> pygame.Surface:
    fp = join(*path)

    return pygame.image.load(fp)
