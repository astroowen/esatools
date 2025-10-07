from astropy import units as u

dis = [
" |   22.80    Mpc |                       |redshift|2010ApJ...725.2270P|",
" |   21       Mpc |                       |        |2007ApJS..173..185G|",
" |   22.39    Mpc |                       |redshift|2007ApJ...655..790C|",
    ]
if type(dis[0]) == str: dis = [float(d.strip()[1:9]) for d in dis]

inunit = u.megaparsec
outunit = u.megalightyear

for d in dis:
    l = (d * inunit).to(outunit)
    print(f"{d*inunit:0.03f} = {l:0.03f}")

lys = [(d * inunit).to(outunit) for d in dis]
print(f"average of {sum(lys)/len(lys):0.03f}")
