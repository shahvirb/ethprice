import ethprice
import leds
import time

SEQUENCE = [
    (300.0, 'D3'),
    (330.0, 'D2'),
    (360.0, 'D1'),
    (99999.0, 'D0'),
]

def display_price(pins, price):
    truth = [price <= seq[0] for seq in SEQUENCE]
    pin = None
    try:
        pin = SEQUENCE[truth.index(True)][1]
    except ValueError:
        pin = SEQUENCE[-1][1]
    for s in SEQUENCE:
        pins[s[1]].off()
    pins[pin].on()


def main():
    pins = leds.get_pins()
    while True:
        current = ethprice.get_json()
        print('ETH: ${}'.format(current['price_usd']))
        display_price(pins, current['price_usd'])
        time.sleep(10)