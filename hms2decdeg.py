# Hours (or degrees) minutes seconds to decimal degrees

import astropy.units as u
from astropy.coordinates import SkyCoord
coord = SkyCoord(
	["18 29 56.8848005064 +01 14 46.304766672"],
	unit=(u.hourangle, u.deg),
	frame='icrs'
	)
print(coord) # prints in decimal degrees by default
