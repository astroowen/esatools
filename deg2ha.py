from astropy import units as u

degs = [
85.1607,
74.3669,
73.9739,
85.9116,
84.7783,
]

degs = [d*u.deg for d in degs]
has = [d.to(u.hourangle) for d in degs]

print(has)
# not really that useful - if you want full hms display you need to make a SkyCoord and then you need the declination also