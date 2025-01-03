import pandas as pd
import csv


df = pd.read_csv('2024.csv')
wdf = pd.read_csv('wrecked_2024.csv')

## Open the dataset and take notes of imperfection that you can see
# print(wdf)

## Corroborate the notes with .info()
# print(wdf.info())

## Create a new dataset with no missing values, compare the length of the 'clean' and 'unclean' datasets
# nwdf = wdf.dropna()
# print(len(wdf))
# print(len(nwdf))

## Get the average of the temperature column, and fill the missing values with it
# print(wdf)
# at = wdf["Temperature (°C)"].mean()
# wdf.fillna({"Temperature (°C)": at}, inplace=True)

## Do the same with the rest of the df
# h = wdf["Humidity (%)"].mean()
# ws = wdf["Wind Speed (km/h)"].mean()
# wdf.fillna({"Humidity (%)": at}, inplace=True)
# wdf.fillna({"Wind Speed (km/h)": at}, inplace=True)
# print(wdf)

## Find the correlation between the temperrature and the rest of the columns 
# print(df["Temperature (°C)"].corr(df["Humidity (%)"]))
# print(df["Temperature (°C)"].corr(df["Wind Speed (km/h)"]))