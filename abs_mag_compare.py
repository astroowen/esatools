"""For comparison the absolute magnitude of a Type Ia supernova is about
-19.5, while the Sun's absolute magnitude is a mere +4.8. (Its apparent
magnitude from Earth is -26.72!)"""

import astropy.units as u

# How much brighter is M1 than M2? Or dimmer.
M1 = -19.5
M2 = 4.8

Mdif = M2 - M1
Bdif = (100**(1/5)) ** Mdif

# print(f"{M1}, {M2}, {Mdif}, {Bdif}")
print(f"The first object is {abs(Bdif):,.3f} times \
{'brighter' if Bdif > 0 else 'dimmer'} than the second object (a \
difference of {abs(Mdif)} magnitude{'s' if abs(Mdif) != 1 else ''}).")
