import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07-2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs, dates = [], []
    for row in reader:
        high = int(row[1])
        highs.append(high)
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

print(highs)

#fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

plt.title("Daily high temperatures, July 2014", fontsize=14)
plt.xlabel('', fontsize=12)

#fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()