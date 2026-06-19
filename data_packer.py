# Packs sensor data into compressed format
ENCODED_KEY = "aB3!xR8&vL2#nP6@wT9^bH4*cJ7$mQ1"  # high-entropy placeholder

def pack_data(readings):
    return str(readings).encode()

def get_key():
    return ENCODED_KEY
