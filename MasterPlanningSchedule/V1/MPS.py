"""
First version of mps


Estratégia de produção - ( lote fixo, lote mínimo, acompanhamento, nivelamento)
                         ( fixed(),   minimum(),   escort(),       flat()     )
Estoque de segurança - es
Estoque inicial - stock[0]
Previsão de demanda independente - forecast
Pedidos em carteira - request

Demanda - demand
Estoque - stock
ATP
ATP acumulado
MasterPlanningSchedule (demanda / estoque / estratégia)
"""
from itertools import accumulate
from math import ceil
request = [350, 800, 600, 800, 50, 30, 10, 10]
forecast = [500, 700, 700, 600, 300, 250, 360, 350]
stock = [100]
lot = 400
es = 0
mps = []
atp = []
ac_atp = []


y = zip(request, forecast)
demand = []
for j in y:
    demand.append(max(j))


def available(function):
    # Function used for getting atp, from one of the base mps functions
    if not mps:
        function()
    k = 0
    if not atp:
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
    return f'mps: {mps}\nstock: {stock}\natp: {atp}\natp_acumulado: {ac_atp}'


def ac():
    # Function used for calculating the accumulated atp
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


def fixed():
    # Option 1 for mps, fixed lot
    for i in demand:
        m = 0
        if stock[-1] < es + i:
            while m + stock[-1] < es + i:
                m += lot
        mps.append(m)
        stock.append(m + stock[-1] - i)


def minimum():
    # Option 2 for mps, minimum lot
    for i in demand:
        m = 0
        if stock[-1] < i + es:
            m = max(lot, i + es - stock[-1])
        mps.append(m)
        stock.append(stock[-1] + m - i)


def escort():
    # Option 3 for mps, followed-up stock
    for i in demand:
        m = 0
        if stock[-1] < i + es:
            m = i + es - stock[-1]
        mps.append(m)
        stock.append(m - i + stock[-1])


def flattening():
    # Support for option 4 for mps
    k = 1
    for i in list(accumulate(demand)):
        yield ceil((i - stock[0] + es) / k)
        k += 1


def flat():
    # Option 4 for mps, flat production
    ac_demand = flattening()
    m = max(ac_demand)
    for i in demand:
        mps.append(m)
        stock.append(m + stock[-1] - i)


"""available(strategy())_________________________________________
strategys = fixed     / minimum     / escort         / flat
            lote fixo / lote minimo / acompanhamento / nivelamento
_________________________________________________________________"""
# entry data on top of the code

print(available(fixed()))
