from time import sleep
import threading
from bs4 import BeautifulSoup
from requests import get
import datetime
import pygame


class PriceFetcher:
    def __init__(self, text):
        self.text = text

        self.value = None
        self.product_name = None
        self.store_name = None
        self.last_update = None

        self.alive = True
        self.thread = threading.Thread(target=self.fetch_data)
        self.thread.start()

        self.sound = pygame.mixer.Sound('sound/duck.mp3')

    def die(self):
        self.alive = False
        self.thread.join()

    def fetch_data(self):
        while self.alive:
            old_value = self.value
            response = get(
                f'https://www.hardgamers.com.ar/search?text={self.text}')
            soup = BeautifulSoup(response.text, 'html.parser')

            price = soup.find(
                attrs={"class": "product-price", "itemprop": "price"}).string
            self.value = price.replace(' ', '').replace('\n', '').split(',')[0]

            name = soup.find(
                attrs={"class": "product-title line-clamp"}).string
            self.product_name = name.replace(' ', '').replace('\n', '')
            if len(self.product_name) > 30:
                self.product_name = self.product_name[:27] + '...'

            store = soup.find(
                attrs={"class": "subtitle"}).string
            self.store_name = store.replace(' ', '').replace('\n', '')
            if len(self.store_name) > 12:
                self.store_name = self.store_name[:9] + '...'

            self.last_update = datetime.datetime.now()

            if old_value != None and self.value < old_value:
                self.sound.play()

            sleep(30)
