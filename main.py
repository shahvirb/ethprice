import ethprice
import leds
import time


def get_price():
    current = ethprice.get_json()
    print('ETH: ${}'.format(current['price_usd']))
    return current


def display_price(display, price):
    display.fill(0)
    display.text('{:4.2f}'.format(price['price_usd']), 0, 0)
    display.show()


def main_loop(display):
    while True:
        price = get_price()
        display_price(display, price)
        time.sleep(10)
