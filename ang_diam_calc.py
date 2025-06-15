import astropy.units as u

# Input distance (must be in pc) from Earth to object:
D = (160_000*u.lightyear).to(u.parsec)
# Input angular diameter of target on image (or just of frame)
# (note: arcmin*60 = arcsec, degree*60*60 = arcsec)
delta = (2.65*60*u.arcsecond)
# This calculates the physical diameter of the target (or image):
d = (D*delta)/(206265 * u.arcsecond)
d = d.to(u.lightyear)
print("distance      D: ", D, "\n", "apparent size δ: ", delta, "\n", "physical size d: ", d, sep="")
