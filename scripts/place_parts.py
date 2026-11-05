# Run inside KiCad PCB Editor: Tools -> Scripting Console
#   exec(open(r"<project folder>\scripts\place_parts.py").read())
# Places every footprint at a fixed spot inside the 55 mm round board (centre 148.5, 105).
# Antenna of U1 points up (12 o'clock), USB-C at the bottom (6 o'clock),
# encoder at 3 o'clock, display header at 9 o'clock. Coordinates in mm, rotation in degrees.
import pcbnew
from pcbnew import FromMM, VECTOR2I

PLACE = {
    # big parts
    "U1":  (148.5, 93.2, 0),
    "J1":  (148.5, 128.5, 0),
    "SW2": (157.0, 105.5, 0),
    "J3":  (127.0, 96.5, 0),
    "J2":  (133.0, 121.0, 0),
    # MCU 3V3 / EN network, top-left of U1
    "C1":  (137.5, 88.1, 90),
    "R1":  (135.5, 88.1, 90),
    "C3":  (133.5, 88.1, 90),
    "C2":  (131.1, 88.4, 90),
    # I2C sensor, top-right
    "U4":  (166.5, 89.5, 0),
    "C7":  (163.0, 88.0, 90),
    "R6":  (163.2, 92.5, 90),
    "R7":  (164.9, 92.7, 90),
    # encoder pull-ups, right of U1
    "R10": (160.5, 90.2, 0),
    "R9":  (160.5, 95.9, 0),
    "R8":  (160.5, 97.7, 0),
    # BOOT button under the module
    "SW1": (146.5, 104.0, 0),
    # charger
    "U3":  (141.5, 116.0, 0),
    "C10": (145.2, 119.5, 0),
    "C8":  (138.2, 116.9, 90),
    "R4":  (146.2, 113.6, 0),
    "D3":  (141.5, 111.0, 0),
    "R5":  (145.3, 110.4, 0),
    # LDO
    "U2":  (151.0, 115.0, 0),
    "C4":  (151.0, 111.0, 0),
    "C5":  (150.6, 119.0, 0),
    "C6":  (150.7, 121.0, 0),
    # power-path diodes
    "D1":  (156.0, 119.5, 0),
    "D2":  (157.0, 122.5, 0),
    # USB-C CC resistors
    "R2":  (141.0, 126.0, 0),
    "R3":  (141.0, 128.0, 0),
    # battery voltage divider
    "R11": (139.9, 122.2, 90),
    "R12": (141.6, 122.2, 90),
    "C9":  (140.8, 119.4, 0),
}

board = pcbnew.GetBoard()
missing = []
for ref, (x, y, rot) in PLACE.items():
    fp = board.FindFootprintByReference(ref)
    if fp is None:
        missing.append(ref)
        continue
    fp.SetPosition(VECTOR2I(FromMM(x), FromMM(y)))
    fp.SetOrientationDegrees(rot)
pcbnew.Refresh()
print("placed:", len(PLACE) - len(missing), "of", len(PLACE))
if missing:
    print("missing footprints (run Update PCB from Schematic first):", missing)
