import pygame

from .settings import *
from .helpers import *

__all__ = ["Game"]

class Game:
    def __init__(self) -> None:
        # Init Pygame
        pygame.init()

        # Create Screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("The Hollow Frontier")
        pygame.display.set_icon(load_image("src", "assets", "logo.png"))
    
    # Events handler
    def handle_events(self, events: list[pygame.Event]) -> None:
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

    # Main Loop
    def run(self) -> None:
        while True:
            self.screen.fill("black")

            # Get Events
            events = pygame.event.get()

            self.handle_events(events)            

            pygame.display.update()
