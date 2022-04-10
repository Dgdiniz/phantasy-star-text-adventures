import os
import json
from megadrive import MegadriveRom


class PhantasyStarTAExtraction:
    def __init__(self):
        self.rom = MegadriveRom()
        self.table = {}

    def load_table(self):
        with open("../table/table.json", encoding='utf-8') as f:
            self.table = json.load(f)
    
    def extract( self, textPointersStartAddress, textPointersEndAddress, dialogsStartAddress, gamename ):
        print(f"Extracting Script for {gamename}...")

        script = {}
        script["Dialogs"] = []

        self.rom.load_rom(f"../games/{gamename}.bin")
        print(f"Rom length: {len(self.rom)} bytes")

        pointers = self.rom[textPointersStartAddress:textPointersEndAddress+1]
        print(f"Pointers length: {len(pointers)} bytes")

        print(len(pointers))

        self.load_table()

        numberOfDialogs = len(pointers)//4

        for i in range(numberOfDialogs):
            dialog = {}
            dialog["index"] = i
            
            pointer = self.rom.read2be(textPointersStartAddress + 4*i + 2) + dialogsStartAddress

            dialog["Original_Pointer"] = hex(pointer)
            dialog["Original_Dialog"] = self.extractDialog(pointer)
            dialog["Translated_Dialog"] = dialog["Original_Dialog"]
            dialog["Comments"] = ""
            dialog["Already_Translated"] = "no"

            script["Dialogs"].append(dialog)

        with open(f"../scripts/{gamename}_script.json", 'w') as fp:
            fp.write(json.dumps(script, ensure_ascii=False, indent=4, separators=(',', ': ')))
        
        print(f"Script {gamename} extracted successfully!")

    def extractDialog(self,address):
        dialog = ""

        i=0

        while 1:
            current = self.rom[address + i]

            if current == 0x0: break
            if current == 0xfe: current = 0x20 # remove break line
            
            if hex(int(current)) in self.table:
                dialog += self.table[hex(int(current))]
            else:
                code = f"{current:0{2}X}"
                dialog += "{" + code + "}"
            
            i += 1
            
        dialog += "{00}"

        return dialog
    

if __name__ == "__main__":
    psta = PhantasyStarTAExtraction() 

    psta.extract(0x2f000, 0x2f643, 0x30000, "amia")
