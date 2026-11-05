# Re-places only the 3V3 / EN decoupling cluster left of the ESP32 module (U1 pins 1 and 2).
# Why: after the first placement, C1's +3V3 pad faced the EN pad and the EN row would have had to
# cross a GND pad. Now the +3V3 pads all sit on one row (y ~ 87.2) and the EN parts sit on a row below.
#   exec(open(r"<project folder>\scripts\tweak_left_cluster.py").read())
import pcbnew
from pcbnew import FromMM, VECTOR2I

MOVES = {
    "R1": (138.0, 87.95, 90),    # pad2 (+3V3) up, pad1 (EN) down
    "C3": (135.6, 89.0, 180),    # EN cap, EN pad on the right
    "C1": (133.2, 88.6, 270),    # 100 nF, +3V3 pad up
    "C2": (131.0, 88.8, 270),    # 10 uF, +3V3 pad up
}
board = pcbnew.GetBoard()
for ref, (x, y, rot) in MOVES.items():
    fp = board.FindFootprintByReference(ref)
    fp.SetPosition(VECTOR2I(FromMM(x), FromMM(y)))
    fp.SetOrientationDegrees(rot)
pcbnew.Refresh()
print("moved:", list(MOVES))
