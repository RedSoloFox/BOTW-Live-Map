import struct, socket
from botwgecko.tcpgecko import TCPGecko

# Wii U is Big endian (>)


class BOTWGecko(TCPGecko):
    #Make this into a config TODO
    coord_pointer = 0x439C0794

    def __init__(self):
        # overwrite __init__ so I don't have to auto-connect
        print("BOTWGecko initialized")
        self.is_connected = False

    def connect(self, ip):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        print("Connecting to " + str(ip) + ":7331")
        self.s.connect((str(ip), 7331))  # IP, 1337 reversed, Cafiine uses 7332+
        print("Connected!")
        self.is_connected = True

    def disconnect(self):
        print("Disconnecting")
        self.s.close()
        print("Disconnected")
        self.is_connected = False

    def connect_and_get_coord_address(self, ip):
        self.connect(ip)
        self.coord_address = self.get_coord_address_from_pointer(self.coord_pointer)

    def get_coord_address_from_pointer(self, address):
        pointer = self.readmem(address, 0x4)
        print(address, struct.unpack(">L", pointer)[0] + 0x140)
        return struct.unpack(">L", pointer)[0] + 0x140

    def auto_coord_address(self):
        self.coord_address = self.get_coord_address_from_pointer(self.coord_pointer)

    def get_coordinates(self):
        coord = self.readmem(self.coord_address, 0xC)
        return struct.unpack(">3f", coord)