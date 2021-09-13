demand = [500, 800, 700, 800, 300, 250, 360, 350]
stock = [100]
lot = 400
es = 100
mps = []


def fixed():
    """mps feito atraves da estrategia de lote fixo"""
    for i in demand:
        m = 0
        if stock[-1] < es + i:
            while m + stock[-1] < es + i:
                m += lot
        mps.append(m)
        stock.append(m + stock[-1] - i)


fixed()
print(mps)
print(stock)
