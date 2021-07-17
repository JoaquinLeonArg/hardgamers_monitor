from typing import List
import pygame
from ui.components import Component
from ui.style import Colors


class UI:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()  # For sound
        pygame.display.set_caption("Xx_HardGamers_NoScoper_xX")
        self.screen: pygame.Surface = pygame.display.set_mode((300, 160))
        self.clock: pygame.time.Clock = pygame.time.Clock()  # For syncing the FPS
        self.running: bool = True
        self.components: List[Component] = []

    def add_component(self, component: Component):
        self.components.append(component)

    def process(self):
        while self.running:
            self.clock.tick(60)
            # Quit handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill(Colors.background)
            for component in self.components:
                component.draw()
            pygame.display.flip()
        pygame.quit()
        for component in self.components:
            component.destroy()
