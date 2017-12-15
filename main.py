from ssd1306 import SSD1306_I2C
import ethprice
import leds
import machine
import main
import network
import ntptime
import time
import utime


DISP_HEIGHT = 48
DISP_WIDTH = 64

def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Win32TrojanKeyLogger.exe', '1234567890')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


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
    h = int((h + 18) % 24)
    d -= 1
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)


def scroll_dy(display, dy)
    for i in range(DISP_HEIGHT):
        display.scroll(0, 1)
        display.framebuf.line(0, i, DISP_WIDTH-1, i, 0)
        display.show()
        time.sleep(0.05)


def main():
    # Create i2c bus and init display
    i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4), freq=400000)
    display = SSD1306_I2C(64, 48, i2c)
    
    # Connect to WiFi
    pins = leds.init_pins()
    pins['D4'].on()
    connect_wifi()
    pins['D4'].off()
    
    # Set the RTC
    ntptime.settime()
    
    while True:
        price = get_price()
        display_price(display, price)
        time.sleep(30)


if __name__ == '__main__':
    main()