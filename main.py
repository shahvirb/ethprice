import ethprice
import leds
import time
import utime


def get_price():
    current = ethprice.get_json()
    print('ETH: ${}'.format(current['price_usd']))
    print(timestr(utime.localtime()))
    return current


def display_price(display, price):
    display.fill(0)
    display.text('{:4.2f}'.format(price['price_usd']), 0, 0)
    display.text(timestr(utime.localtime()), 0, 40)
    display.show()


def timestr(time):
    y, mon, d, h, m, s, wkday, yrday = time
    #HACK -- timezone adjustment
    h += 18
    d -= 1
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)


def main_loop(display):
    while True:
        price = get_price()
        display_price(display, price)
        time.sleep(30)
