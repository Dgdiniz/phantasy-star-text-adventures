arch md.cpu

macro seekRom(offset) {
    origin {offset}
    base 0x0
}

seekRom(0x30000)
insert script, "obj/amia_dialogs.bin"    

seekRom(0x2f000)
insert poiters, "obj/amia_pointers.bin"