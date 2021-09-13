# MasterPlanningSchedule
This algorithm was written while testing a few things on python, so it wasn't written with the thought it being in the best format.

Repository with algorithms for calculating MPS (master planning schedule)

Strategies available would be: fixed lot (fixed), minimum lot (minimum), demand tracking (escort) or flat.

At MPS.py at the top of the page there are some input data that needs to be written as intended: request, forecast, stock... es(safety stock).
The last line should be modified as wished, depending on the strategy you're looking for. Format: "print(available(......()))"

Saídas: 
  MPS[...];
  Stock[...];
  Atp(available to promises)[...];
  Ac_atp(accumulated atp)[...]
