request = [350, 800, 600, 800, 50, 30, 10, 10]
stock = [100, 400, 400, 100, 100, 200, 350, 390, 440]
mps = [800, 800, 400, 800, 400, 400, 400, 400]
atp = []
ac_atp = []

"""
x = [350, 800, 600, 800, 50, 30, 0, 0]
x = map(lambda y: y if y != 0 else "", x)
print(list(x))

if not atp:
    print('lista vazia')
"""


def available():
    k = 0
    for i in request:
        z = 0
        ll = 1
        if mps[k] == 0:
            atp.append('')
            k += 1
            continue
        try:
            while mps[k+ll] == 0:
                z = request[k+ll]
                ll += 1
        except IndexError:
            pass
        if not atp:
            n = stock[0] + mps[k] - i - z
        else:
            n = mps[k] - i - z
        atp.append(n)
        k += 1
    ac()
    return atp


def ac():
    o = 0
    q = 0
    p = list(map(lambda t: t if t != '' else 0, atp))
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


available()
print(atp)
print(ac_atp)
