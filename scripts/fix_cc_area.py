# Opens a lane north of the USB-C pad row so the CC resistors can sit straight above their pads,
# and moves C5/C6/C10 next to the parts they decouple.
#   exec(open(r"<project folder>\scripts\fix_cc_area.py").read())
# First flip C10 to the front side by hand (select it, press F) - it was created on the back.
import pcbnew
from pcbnew import FromMM, VECTOR2I

MOVES = {
    "R3":  (147.25, 121.7, 90),   # CC1, pad 1 (CC1) points down at J1 pad A5
    "R2":  (150.25, 121.7, 90),   # CC2, pad 1 (CC2) points down at J1 pad B5
    "C5":  (154.0, 118.2, 0),     # LDO output caps, right of U2
    "C6":  (154.0, 120.2, 0),
    "C10": (140.5, 111.0, 0),     # VBUS cap next to the charger U3 (VDD pin)
}
board = pcbnew.GetBoard()
for ref, (x, y, rot) in MOVES.items():
    fp = board.FindFootprintByReference(ref)
    if fp is None:
        print("missing", ref)
        continue
    if fp.GetLayer() != pcbnew.F_Cu:
        print(ref, "is on the BACK side: select it, press F, then run this again")
    fp.SetPosition(VECTOR2I(FromMM(x), FromMM(y)))
    fp.SetOrientationDegrees(rot)
pcbnew.Refresh()
print("moved:", list(MOVES))
