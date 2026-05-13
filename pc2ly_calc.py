from astropy import units as u

dis = [25]
if type(dis[0]) == str:
	dis = [float(d.strip()[1:9]) for d in dis]
	print("reformatted:", dis)

inunit = u.parsec
outunit = u.lightyear

for d in dis:
    l = (d * inunit).to(outunit)
    print(f"{d*inunit:0.03f} = {l:0.03f}")

lys = [(d * inunit).to(outunit) for d in dis]
print(f"average of {sum(lys)/len(lys):0.03f}")
