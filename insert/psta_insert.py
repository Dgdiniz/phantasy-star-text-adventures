import os
import json
from megadrive import MegadriveRom


class PhantasyStarTAInsertion:
    def __init__(self):
        self.rom = MegadriveRom()
        self.table = {}
        self.invertedtable = {}

    def load_table(self):
        with open("../table/table.json", encoding='utf-8') as f:
            self.table = json.load(f)
    
    def invertTable(self):
        for key in self.table:
            self.invertedtable[self.table[key]] = key
    
    def insert(self, textPointersStartAddress, textPointersEndAddress, gamename):
        dialogs = bytearray()
        script = {}        
        offset = 0
        i=0

        self.rom.load_rom(f"../games/{gamename}.bin")

        pointers = self.rom[textPointersStartAddress:textPointersEndAddress+1]
        print(pointers)

        with open(f"../scripts/{gamename}_script.json", encoding='latin1') as f:
            script = json.load(f)
        
        self.load_table()
        self.invertTable()

        for dialog in script["Dialogs"]:
            #print(f"Dialogo: {i}") # for debug
            off = offset.to_bytes(2,byteorder='big')
            pointers[4*i+2] = off[0]
            pointers[4*i+2+1] = off[1]
            encodedDialog = self.encodeDialog(dialog["Translated_Dialog"])
            dialogs += encodedDialog
            offset += len(encodedDialog)
            i+=1
        
        with open(f"../obj/{gamename}_pointers.bin", "wb") as f:
            f.write(pointers)
        
        with open(f"../obj/{gamename}_dialogs.bin", "wb") as f:
            f.write(dialogs)

        print(f"Insertion {gamename} completed successfully!")
    
    def encodeDialog(self, dialog):
        encodedDialog = bytearray()
        i=0

        while i < len(dialog):
            current = dialog[i]
            if current == "{":
                strcode = dialog[i+1:i+3]
                code = int(strcode, 16)
                encodedDialog += code.to_bytes(1, byteorder='big')
                i+=4
            else:
                if current in self.invertedtable:
                    decodedbyte = int(self.invertedtable[current],16)
                    encodedDialog += decodedbyte.to_bytes(1, byteorder='big')
                else:
                    print(f"ERROR: current: {current}")
                    for i in self.invertedtable:
                        print(i)
                    raise Exception
                
                i+=1

        return encodedDialog


if __name__ == "__main__":
    psta = PhantasyStarTAInsertion() 

    psta.insert(0x2f000, 0x2f643, "amia") 
