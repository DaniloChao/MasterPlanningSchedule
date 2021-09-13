request = [350, 800, 600, 800, 50, 30, 10, 10]
forecast = [500, 700, 700, 600, 300, 250, 360, 350]


y = zip(request, forecast)
demand = []
for i in y:
    demand.append(max(i))

print(demand)
