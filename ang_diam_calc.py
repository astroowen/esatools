import astropy.units as u

# Input distance (must be in pc) from Earth to object:
#D = (2_800_000_000*u.lightyear).to(u.parsec)
D = 1366*u.parsec
# Input angular diameter of target on image (or just of frame)
# (note: arcmin*60 = arcsec, degree*60*60 = arcsec)
delta = (16*u.arcsecond)
# This calculates the physical diameter of the target (or image):
d = (D*delta)/(206265 * u.arcsecond)
d = d.to(u.lightyear)
print("distance      D: ", D, "\n", "apparent size δ: ", delta, "\n", "physical size d: ", d, sep="")
