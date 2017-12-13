import ethprice
import leds
import time
from machine import Timer

SEQUENCE = [
    (300.0, 'D3'),
    (330.0, 'D2'),
    (360.0, 'D1'),
    (99999.0, 'D0'),
]

# Valid IDs are between 1 and 14
TIMER_MAIN_LOOP = 1
TIMER_LED = 2


def get_price():
    current = ethprice.get_json()
    print('ETH: ${}'.format(current['price_usd']))
    return current


def display_price(pins, price):
    truth = [price['price_usd'] <= seq[0] for seq in SEQUENCE]
    pin = None
    try:
        pin = SEQUENCE[truth.index(True)][1]
    except ValueError:
        pin = SEQUENCE[-1][1]
    for s in SEQUENCE:
        pins[s[1]].off()
    pins[pin].on()
    pins['D4'].on()
    Timer(TIMER_LED).init(period=500, mode=Timer.ONE_SHOT, callback=lambda x: pins['D4'].off())


def main_loop():
    price = get_price()
    display_price(pins, price)

pins = leds.get_pins()
Timer(TIMER_MAIN_LOOP).init(period=5000, mode=Timer.PERIODIC, callback=lambda x: main_loop())
