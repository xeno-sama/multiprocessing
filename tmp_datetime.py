import pandas as pd
from datetime import timedelta, date
from time import perf_counter

start_time = perf_counter()

start_date = date(1700, 1, 1)
end_date = date(2500, 1, 1)
delta = timedelta(days=1)

# while start_date <= end_date:
#     # print(start_date.strftime("%Y-%m-%d"))
#     start_date += delta


daterange = pd.date_range(start_date, end_date)
# pandas limit 1677-09-21 - 2262-04-11
for single_date in daterange:
    print(single_date.strftime("%Y-%m-%d"))

print(f'{(perf_counter() - start_time)}')
