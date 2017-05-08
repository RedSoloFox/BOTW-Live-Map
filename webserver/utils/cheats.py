from webserver import bgecko
from botwgecko.mem_addresses import *
import struct

# TODO, move address getting to botwgecko, do once, less work

def get_health():
    address = struct.unpack(">L", bgecko.readmem(current_health_pointer, 0x4))[0] + 0x388
    current_health = bgecko.readmem(address, 0x4)

    address = struct.unpack(">L", bgecko.readmem(max_health_pointer, 0x4))[0] - 0x10
    max_health = bgecko.readmem(address, 0x4)

    return [struct.unpack('>i', current_health), struct.unpack('>i', max_health)]


def set_health(health):
    address = struct.unpack(">L", bgecko.readmem(current_health_pointer, 0x4))[0] + 0x388
    byte_health = struct.pack(">L", int(health))
    bgecko.writestr(address, byte_health)


def get_stamina():
    return 1


def set_stamina(stamina):
    return 0


def get_rupees():
    return 1


def set_rupees(rupees):
    return 0


def get_mon():
    return 1


def set_mon(mon):
    return 0


def set_speed(speed):
    return 0


def set_damage(damage):
    return 0


def set_time(time):
    return 0


def get_abilities():
    # Get current abilities, and return dictionary
    return {"1": "err", "2": "err", "3": "err", "4": "err"}


def set_abilities():
    return 0