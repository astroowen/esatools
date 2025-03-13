import astropy.units as u

# Input distance from Earth to object:
D = 162000 * u.lightyear
# Input angular diameter of target on image (or just of frame)
delta = 160 * u.arcsecond
# This calculates the physical diameter of the target (or image):
d = (D*delta)/(206265 * u.arcsecond)
print(
    f"distance      : {D}\napparent size : {delta}\nphysical size : {d:.3f}", 
    sep="", end="\n\n"
)