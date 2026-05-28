from astropy import units as u

dis = [
 "|   19.5     Mpc |  -3.9        +3.9     |T-F     |2022MNRAS.511.6160K|",
 "|   14.32    Mpc |  -1.16       +1.16    |T-F     |2020ApJ...902..145K|",
 "|   16.7     Mpc |  -1.2        +1.2     |kin     |2018ApJ...861...49H|",
 "|   11.1686  Mpc |                       |redshift|2019A&A...631A..38L|",
 "|   19.95    Mpc |                       |        |2016AJ....152...50T|",
 "|   20.9     Mpc |                       |T-F     |2014MNRAS.444..527S|",
 "|   19.68    Mpc |  -0.20       +0.20    |        |2013AJ....146...86T|",
 "|   15.3     Mpc |                       |redshift|2011MNRAS.413..813C|",
 "|   32.70    Mpc |                       |redshift|2010ApJ...725.2270P|",
 "|   18       Mpc |  -3          +3       |T-F     |2008ApJ...676..184T|",
 "|   20.48    Mpc |                       |redshift|2007ApJ...655..790C|",
 "|   19.41    Mpc |                       |redshift|2007ApJ...655..790C|",
 "|   16.7     Mpc |                       |        |2007AJ....133.2569G|",
]
if type(dis[0]) == str:
	dis = [float(d.strip()[1:9]) for d in dis]
	print("reformatted:", dis)

inunit = u.megaparsec
outunit = u.megalightyear

for d in dis:
    l = (d * inunit).to(outunit)
    print(f"{d*inunit:0.03f} = {l:0.03f}")

lys = [(d * inunit).to(outunit) for d in dis]
print(f"average of {sum(lys)/len(lys):0.03f}")
