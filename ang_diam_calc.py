import astropy.units as u

# Input distance (must be in pc) from Earth to object:
#D = (2_800_000_000*u.lightyear).to(u.parsec)
D = 392*u.parsec
# Input angular diameter of target on image (or just of frame)
# (note: arcmin*60 = arcsec, degree*60*60 = arcsec)
delta = (6.681*u.arcminute)*60
# This calculates the physical diameter of the target (or image):
d = (D*delta)/(206265 * u.arcsecond)

print(
    "distance      D: ", D, "\n",
    "apparent size δ: ", delta, "\n",
    "physical size d: ", d.to(u.lightyear), "\n",
    "                (", d.to(u.parsec), ")", sep="")
