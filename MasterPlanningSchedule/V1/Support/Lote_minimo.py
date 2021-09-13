demand = [500, 800, 700, 800, 300, 250, 360, 350]
stock = [100]
lot = 300
es = 100
mps = []


def minimum():
    """mps feito atraves da estrategia de lote minimo"""
    for i in demand:
        m = 0
        if stock[-1] < i + es:
            m = max(lot, i + es - stock[-1])
        mps.append(m)
        stock.append(stock[-1] + m - i)


minimum()
print(mps)
print(stock)
