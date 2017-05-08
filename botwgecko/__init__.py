import struct
from pygecko import TCPGecko
# from botwgecko.mem_addresses import *

# Wii U is Big endian (>)


class BOTWGecko(TCPGecko):
    #Make this into a config TODO
    coord_pointer = 0x439D89A4

    def __init__(self):
        super().__init__()
        print("BOTWGecko initialized!")

    def connect_and_get_coord_address(self, ip):
        self.connect(ip)
        self.coord_address = self.get_coord_address_from_pointer(self.coord_pointer)

    def get_coord_address_from_pointer(self, address):
        pointer = self.readmem(address, 0x4)
        return struct.unpack(">L", pointer)[0] + 0x140

    def auto_coord_address(self):
        self.coord_address = self.get_coord_address_from_pointer(self.coord_pointer)

    def get_coordinates(self):
        coord = self.readmem(self.coord_address, 0xC)
        return struct.unpack(">3f", coord)