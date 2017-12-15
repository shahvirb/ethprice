from machine import Pin

# D4 is the built in LED

    # GPIO Pin #, Pin Mode, Inverted
wemos_map = {
    # 'D0': (16, Pin.OUT, False),
    # 'D1': (5, Pin.OUT, False),
    # 'D2': (4, Pin.OUT, False),
    # 'D3': (0, Pin.OUT, False),
    'D4': (2, Pin.OUT, True)
}


class InvertingPin(Pin):
    def on(self):
        return super(InvertingPin, self).off()
        
    def off(self):
        return super(InvertingPin, self).on()


def init_pins():
    pins = {}
    for dpin in wemos_map:
        constructor = InvertingPin if wemos_map[dpin][2] else Pin
        pins[dpin] = constructor(wemos_map[dpin][0], wemos_map[dpin][1], value=0)
    return pins


def get_pins():
    pins = {}
    for dpin in wemos_map:
        constructor = InvertingPin if wemos_map[dpin][2] else Pin
        pins[dpin] = constructor(wemos_map[dpin][0], wemos_map[dpin][1])
    return pins