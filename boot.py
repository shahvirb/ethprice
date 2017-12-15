# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
import webrepl
webrepl.start()
gc.collect()

import leds
pins = leds.init_pins()
pins['D4'].on()

def connect_wifi():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Win32TrojanKeyLogger.exe', '1234567890')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

connect_wifi()
pins['D4'].off()

# Create i2c bus and init display
import machine
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4), freq=400000)
from ssd1306 import SSD1306_I2C
display = SSD1306_I2C(64, 48, i2c)

# Set the RTC
import ntptime
ntptime.settime()

import main
main.main_loop(display)
