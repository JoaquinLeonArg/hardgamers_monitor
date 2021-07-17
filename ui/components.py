from abc import ABC, abstractmethod
import datetime
from ui.style import Colors
from fetch.fetch import PriceFetcher
import pygame


class Component(ABC):
    def __init__(self, surface):
        self.surface = surface

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def destroy(self):
        pass


class LastPrice(Component):
    def __init__(self, surface, x: int, y: int, count: int, fetcher: PriceFetcher):
        super().__init__(surface)
        self.x = x
        self.y = y
        self.count = count
        self.price_font = pygame.font.Font('fonts/NotoSans-Bold.ttf', 40)
        self.store_font = pygame.font.Font('fonts/NotoSans-Regular.ttf', 14)
        self.updated_font = pygame.font.Font('fonts/NotoSans-Italic.ttf', 14)
        self.price_fetcher = fetcher

    def destroy(self):
        self.price_fetcher.die()

    def draw(self):
        self.y -= 1
        if self.y < -80:
            self.y += 60 + 80*self.count
        if self.price_fetcher.last_update:
            text = self.price_font.render(
                f'$ {self.price_fetcher.value}', True, Colors.text)
            self.surface.blit(text, (self.x, self.y))

            text = self.store_font.render(
                f'{self.price_fetcher.text}: {self.price_fetcher.product_name}', True, Colors.text)
            self.surface.blit(text, (self.x, self.y + 46))

            text = self.store_font.render(
                f'@ {self.price_fetcher.store_name}', True, Colors.text)
            self.surface.blit(text, (self.x, self.y + 60))

            text = self.updated_font.render(
                f'Updated {(datetime.datetime.now() - self.price_fetcher.last_update).seconds}s ago', True, Colors.text)
            self.surface.blit(
                text, (self.x + text.get_width() + 8, self.y + 60))


class Footer(Component):
    def __init__(self, surface):
        super().__init__(surface)
        self.font = pygame.font.Font('fonts/NotoSans-Regular.ttf', 16)

    def draw(self):
        pygame.draw.rect(self.surface, Colors.accent, (0, 140, 300, 20))
        text = self.font.render('Creado por Joaquin León', True, Colors.text)
        self.surface.blit(text, (8, 138))

    def destroy(self):
        pass
