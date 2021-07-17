from ui.components import Footer, LastPrice
from ui.ui import UI
from fetch.fetch import PriceFetcher
import os


if __name__ == '__main__':
    ui = UI()

    products = os.environ.get('PRODUCTS').split(',')

    for i, product in enumerate(products):
        ui.add_component(LastPrice(ui.screen, 8, 10 + 90*i,
                         len(products), PriceFetcher(product)))

    ui.add_component(Footer(ui.screen))

    ui.process()
