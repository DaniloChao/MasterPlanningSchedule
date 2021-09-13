demand = [500, 800, 700, 800, 300, 250, 360, 350]
stock = [100]
lot = 300
es = 100
mps = []


def escort():
    for i in demand:
        m = 0
        if stock[-1] < i + es:
            m = i + es - stock[-1]
        mps.append(m)
        stock.append(m - i + stock[-1])


escort()
print(mps)
print(stock)
