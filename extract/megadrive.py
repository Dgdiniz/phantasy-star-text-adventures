# Douglas Diniz - 2018 - dgdiniz@gmail.com

class MegadriveRom:
    def __init__(self):
        self.rom = bytearray()

    def __len__(self):
        return len(self.rom)
    
    def __getitem__(self, position):
        return self.rom[position]
       
    def load_rom(self, rom_path):
        self.romfile = open(rom_path, "rb")
        self.rom = bytearray(self.romfile.read())

    def read2be(self, address):
        return int.from_bytes(self.rom[address:address+2], "big")
    
    def read4be(self, address):
        return int(self.rom[address:address+4])

    def size(self):
        return len(self.rom)
