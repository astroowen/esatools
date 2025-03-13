from astropy import units as u
from statistics import mean

dis = [
    16.4,
8.5,
16.0694,
13.61,
14.26,
16,
16.12
    ]

unit = u.megaparsec

lys = [(d * unit).to(u.megalightyear) for d in dis]
for d in dis:
    l = (d * unit).to(u.megalightyear)
    print(f"{d*unit:0.03f} = {l:0.03f}")

print(f"average of...{sum(lys)/len(lys):0.03f}")