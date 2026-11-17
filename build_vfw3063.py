"""
Bonfiglioli VF/W 30/63_1200 - P56 - BN56A4
Combined two-stage worm gearmotor - representative 3D reconstruction (mm)

Interface dimensions from Bonfiglioli VF/W catalog (R11) :
  Output (version U) : bore 25 H7 through, keyway 8 H8, across 28.3,
                       hub 75 h8 protruding both sides
  Input flange P56 B5: N=120, N1=100 (4x7), N2=80 spigot, M=9 thick,
                       bore 9 E7, keyway 3 H9, across 10.4
  Motor BN 56A4 (IM B5): flange P=120/M=100/N=80/S=7/T=3, body AC=110,
                       LB=165, AD=91, AF=74, shaft 9x20, key 3 (GA=10.2)

Layout : two worm stages in series -> motor axis parallel to output axis.
  Output axis       : X, at (y=0, z=0)
  Intermediate axis : Y, at (x=132, z=63)   (W63 center distance = 63)
  Motor axis        : X, at (z=93)          (VF30 center distance = 30)
Reducer chain along X : flange 9 + VF30 76 + W63 94 + hub 3.5 = 182.5
"""
import math
import cadquery as cq

# ---------------- reducer body ----------------
# input flange (motor side), x = 0..9, motor axis at z=93
flange = cq.Workplane("YZ", origin=(0, 0, 93)).circle(60).extrude(9)

# VF30 section, x = 9..85
vf30 = cq.Workplane("YZ", origin=(9, 0, 74)).rect(80, 88).extrude(76)
try:
    vf30 = vf30.edges("|X").fillet(12)
except Exception:
    pass

# W63 section, x = 85..179
w63 = cq.Workplane("YZ", origin=(85, 0, 36.25)).rect(94, 147.5).extrude(94)
try:
    w63 = w63.edges("|X").fillet(10)
except Exception:
    pass

# output hub 75 h8, x = 179..182.5, output axis z=0
hub = cq.Workplane("YZ", origin=(179, 0, 0)).circle(37.5).extrude(3.5)

body = flange.union(vf30).union(w63).union(hub)

# spigot recess N2=80 x 3 deep on motor face
body = body.cut(cq.Workplane("YZ", origin=(0, 0, 93)).circle(40).extrude(3))

# input bore 9 E7 through flange
body = body.cut(cq.Workplane("YZ", origin=(-1, 0, 93)).circle(4.5).extrude(11))

# input keyway 3 H9, across 10.4 (top of slot at +5.2 from axis)
body = body.cut(
    cq.Workplane("XY", origin=(-1, 0, 93))
    .box(11, 3, 5.2, centered=(True, True, False))
)

# flange bolt holes 4x7 on N1=100
for a in (45, 135, 225, 315):
    y = 50 * math.cos(math.radians(a))
    z = 93 + 50 * math.sin(math.radians(a))
    body = body.cut(
        cq.Workplane("YZ", origin=(-1, y, z)).circle(3.5).extrude(11)
    )

# output bore 25 H7 through all (version U)
body = body.cut(cq.Workplane("YZ", origin=(80, 0, 0)).circle(12.5).extrude(103))

# output keyway 8 H8, across 28.3 (top of slot at +14.15 from axis)
body = body.cut(
    cq.Workplane("XY", origin=(80, 0, 0)).box(103, 8, 14.15, centered=(True, True, False))
)

reducer = body

# ---------------- motor BN 56A4 (IM B5) ----------------
# B5 flange plate, x = -10..0, spigot N=80 x T=3 entering the recess
mflange = cq.Workplane("YZ", origin=(-10, 0, 93)).circle(60).extrude(10)
mflange = mflange.union(cq.Workplane("YZ", origin=(0, 0, 93)).circle(40).extrude(3))
for a in (45, 135, 225, 315):
    y = 50 * math.cos(math.radians(a))
    z = 93 + 50 * math.sin(math.radians(a))
    mflange = mflange.cut(
        cq.Workplane("YZ", origin=(-11, y, z)).circle(3.5).extrude(12)
    )

# stator body AC=110, LB=165 (flange face -> rear), x = -173..-8
mbody = cq.Workplane("YZ", origin=(-173, 0, 93)).circle(55).extrude(165)

# fan cowl at rear, x = -218..-173, rounded rear cap
cowl = cq.Workplane("YZ", origin=(-218, 0, 93)).circle(55).extrude(45)
try:
    cowl = cowl.edges("<X").fillet(25)
except Exception:
    pass

# shaft 9 x 20 into the input bore
shaft = cq.Workplane("YZ", origin=(-20, 0, 93)).circle(4.5).extrude(30)

# terminal box on top : AF=74 wide, top at AD=91 above mounting face
tbox = cq.Workplane("XY", origin=(-70, 0, 147)).box(60, 74, 37, centered=(True, True, False))
tbox = tbox.union(
    cq.Workplane("XY", origin=(-70, 0, 184)).box(66, 80, 6, centered=(True, True, False))
)

motor = mflange.union(mbody).union(cowl).union(shaft).union(tbox)

# ---------------- assembly + export ----------------
assy = cq.Assembly(name="VF_W_30_63_1200_P56_BN56A4")
assy.add(reducer, name="gearbox_body", color=cq.Color(0.62, 0.62, 0.62))
assy.add(motor, name="motor_BN56A4", color=cq.Color(0.16, 0.31, 0.55))

out = "/workspace/VF_W_30_63_1200_P56_BN56A4.step"
assy.save(out)

print("saved", out)
