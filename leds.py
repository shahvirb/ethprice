from machine import Pin

# D4 is the built in LED

wemos_map = {
    'D0': (16, Pin.OUT),
    'D1': (5, Pin.OUT),
    'D2': (4, Pin.OUT),
    'D3': (0, Pin.OUT),
    'D4': (2, Pin.OUT)
}


def init_pins():
    pins = {}
    for dpin in wemos_map:
        pins[dpin] = Pin(wemos_map[dpin][0], wemos_map[dpin][1], value=0)
    return pins

def get_pins():
    pins = {}
    for dpin in wemos_map:
        pins[dpin] = Pin(wemos_map[dpin][0], wemos_map[dpin][1])
    return pins