from astropy import units as u

dis = [
19.4,
14.3,
14.20,
19.8,
11.57,
    ]

inunit = u.megaparsec
outunit = u.megalightyear

for d in dis:
    l = (d * inunit).to(outunit)
    print(f"{d*inunit:0.03f} = {l:0.03f}")

lys = [(d * inunit).to(outunit) for d in dis]
print(f"average of {sum(lys)/len(lys):0.03f}")
