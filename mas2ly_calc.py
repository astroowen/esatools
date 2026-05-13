from astropy import units as u

parallax = 1.5461 * u.milliarcsecond # u.mas

distance = parallax.to(u.lightyear, equivalencies=u.parallax())

print(f"{parallax:0.04f} = {distance:0.03f}")

# https://docs.astropy.org/en/stable/units/equivalencies.html#how-to-convert-parallax-to-distance
