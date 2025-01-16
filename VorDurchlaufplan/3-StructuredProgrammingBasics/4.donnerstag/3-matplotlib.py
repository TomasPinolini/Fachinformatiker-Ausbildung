import pandas as pd
import csv
import matplotlib.pyplot as pl
import numpy as np


## Get the annual dataset from before and make some linear charts to see the weather variance throughout the year

df = pd.read_csv('2024.csv')

# d = np.array(df["Date"])
# t = np.array(df["Temperature (°C)"])
# h = np.array(df["Humidity (%)"])
# ws = np.array(df["Wind Speed (km/h)"])

# pl.plot(d, ws)
# pl.show()

## Do the same but only for January
df["Date"] = pd.to_datetime(df["Date"])
jan = df[(df["Date"] >= "2024-01-01") & (df["Date"] <= "2024-01-31")]
dJ = np.array(jan["Date"])
tJ = np.array(jan["Temperature (°C)"])
hJ = np.array(jan["Humidity (%)"])
wsJ = np.array(jan["Wind Speed (km/h)"])

pl.plot(dJ, hJ)
pl.show()
