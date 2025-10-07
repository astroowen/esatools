import astropy.units as u

# Distance modulus (magnitudes, ergo unitless) and target unit
mod = 29.75
target = u.megaparsec

# Calculate distance in parsec
distance = 10**((mod/5)+1) * u.parsec
# print it:
print(f"μ: {mod} mag\nd: {distance.to(target):0.05f}")
