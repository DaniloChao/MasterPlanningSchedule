atp = [550, 0, -200, 0, 350, 370, 390, 390]

p = list(map(lambda t: t if t != '' else 0, atp))
o = 0
q = 0
ac_atp = []
for i in p:
    if i < 0:
        o += i
for i in p:
    if not ac_atp:
        q = i + o
        ac_atp.append(q)
    else:
        if i < 0:
            ac_atp.append(q)
        else:
            q += i
            ac_atp.append(q)

print(ac_atp)
