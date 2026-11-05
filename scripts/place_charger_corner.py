# Straightens the charger corner: every part sits one step from the U3 pin it connects to.
#   exec(open(r"<project folder>\scripts\place_charger_corner.py").read())
import pcbnew
from pcbnew import FromMM, VECTOR2I

MOVES = {
    "C10": (140.1, 111.95, 0),    # VBUS cap, right of U3 pin 4 (VDD)
    "R4":  (140.1, 110.05, 180),  # PROG resistor, right of U3 pin 5
    "D3":  (136.5, 107.6, 90),    # charge LED, above U3 pin 1 (STAT)
    "R5":  (139.4, 107.0, 0),     # LED resistor, right of D3
}
board = pcbnew.GetBoard()
done = []
for fp in board.GetFootprints():
    ref = fp.GetReference()
    if ref in MOVES:
        x, y, rot = MOVES[ref]
        fp.SetPosition(VECTOR2I(FromMM(x), FromMM(y)))
        fp.SetOrientationDegrees(rot)
        done.append(ref)
pcbnew.Refresh()
print("moved:", done)
