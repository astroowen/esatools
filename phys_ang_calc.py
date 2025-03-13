"""
(δ * D)/206265 = d

where
δ : angular diameter of the object / angular distance between the two objects,
    in arcseconds (estimate from size of image or get from SIMBAD or NED)
D : distance (get from caption or try to research)
d : physical diameter

The units of d are the same as the units of D - probably light-years. Image
dimensions on the ESA/Hubble site are W x H.

(d/D) * 206,265 = δ

To use this script:
1. Fill in the coordinates of the two objects (RA and DEC in the ICRS frame,
   or specify if another frame) to c1 and c2
2. Either:
    a. If you have individual distances for c1 and c2, fill those in as
       distance=<number>*u.lightyear to c1 and c2, and set D = None, or:
    b. If you only have a general distance, set D = <that_distance>*u.lightyear,
       and fill distance=D into c1 and c2
3. Run it!
"""
from astropy import units as u
from astropy.coordinates import SkyCoord

D = 3.2e9 * u.lightyear

c1 = SkyCoord(["08 00 58.418 +36 03 41.69"],distance=48.5e6 * u.parsec, 
              unit=(u.hourangle, u.deg), frame='icrs')
c2 = SkyCoord(["08 00 55.260 +36 03 2.84"], distance=47.2e6 * u.parsec, 
              unit=(u.hourangle, u.deg), frame='icrs')

if D is not None:
    diff = (c1.separation(c2).arcsecond * D)/206265
else:
    diff = c1.separation_3d(c2)
print(diff.to(u.lightyear))