import datetime as dt

then = input("What time was it last edited? Enter as '13:55' or '1:55pm' only, no spaces.\n")
h = int(then.split(':')[0])
if then.endswith("pm"):
	if h < 12: h += 12
	then = then[:-2]
if then.endswith("am"):
	if h == 12: h -= 12
	then = then[:-2]
m = int(then.split(':')[1])
then = dt.time(h, m)

dt_then = dt.datetime.combine(dt.date.today(), then)
dt_now = dt.datetime.now()

since = dt_now - dt_then

mm, ss = divmod(since.seconds, 60)
hh, m2 = divmod(mm, 60)

print(f"It's been {hh} hours {m2} minutes ({mm} minutes) since {dt_then:%H:%M} today.")
