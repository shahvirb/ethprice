# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
import webrepl
webrepl.start()
gc.collect()

import leds
pins = leds.init_pins()

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
pins['D4'].on() # HACK - fix inverting LED

import main
main.main()