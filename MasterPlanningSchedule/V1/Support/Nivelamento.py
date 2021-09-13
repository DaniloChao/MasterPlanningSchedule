from itertools import accumulate
from math import ceil
demand = [500, 800, 700, 800, 300, 250, 360, 350]
stock = [100]
lot = 300
es = 100
mps = []


def flattening():
    j = 1
    for i in list(accumulate(demand)):
        yield ceil((i - stock[0] + es) / j)
        j += 1


def flat():
    ac_demand = flattening()
    m = max(ac_demand)
    for i in demand:
        mps.append(m)
        stock.append(m + stock[-1] - i)


flat()
print(mps)
print(stock)
