# Removes tracks that were drawn before their parts were moved (tracks do not follow a footprint
# moved with M), and pulls R12 off R11 (they sat on the same spot).
#   exec(open(r"<project folder>\scripts\clear_stale_tracks.py").read())
# Afterwards: press B (refill zones) and Ctrl+S. Then route everything once from the net list.
import pcbnew
from pcbnew import FromMM, VECTOR2I

STALE_NETS = {
    "VBUS", "+3V3", "Net-(U1-EN)", "Net-(D3-A)", "Net-(D3-K)", "/DISP_SCK", "Net-(U3-PROG)",
}

board = pcbnew.GetBoard()
removed = 0
for item in list(board.GetTracks()):          # segments and vias
    if item.GetNetname() in STALE_NETS:
        board.Remove(item)
        removed += 1

r12 = board.FindFootprintByReference("R12")
if r12 is not None:
    r12.SetPosition(VECTOR2I(FromMM(142.0), FromMM(120.7)))
    r12.SetOrientationDegrees(90)

pcbnew.Refresh()
print("removed track items:", removed, "| R12 moved off R11")
