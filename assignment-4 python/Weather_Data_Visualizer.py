# Name: Aayan Srivastwa
# Project: Weather Data Analyzer
# Assignment No: 4

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Task 1: Load the Data
data = pd.read_csv("weather.csv")
print(data.head())
print(data.info())
print(data.describe())

#Task 2: Data Cleaning

data['Date'] = pd.to_datetime(data['Date'])
data = data.fillna(method='ffill')
data = data[['Date', 'Temperature', 'Rainfall', 'Humidity']]
print(data.head())

#Task 3: NumPy Statistics

print("Mean Temperature:", np.mean(data['Temperature']))
print("Max Temperature:", np.max(data['Temperature']))
print("Min Temperature:", np.min(data['Temperature']))
print("Std Temperature:", np.std(data['Temperature']))


data['Month'] = data['Date'].dt.month

#Task 4: Visualization

#Line Chart
plt.figure(figsize=(10,5))
plt.plot(data['Date'], data['Temperature'])
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Daily Temperature Trend")
plt.savefig("daily_temperature.png")
plt.show()

#Bar Chart
monthly_rain = data.groupby('Month')['Rainfall'].sum()

plt.figure(figsize=(10,5))
plt.bar(monthly_rain.index, monthly_rain.values)
plt.xlabel("Month")
plt.ylabel("Total Rainfall")
plt.title("Monthly Rainfall")
plt.savefig("monthly_rainfall.png")
plt.show()

#Scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(data['Temperature'], data['Humidity'])
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.title("Humidity vs Temperature")
plt.savefig("humidity_vs_temp.png")
plt.show()

#Combined Figure
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(data['Date'], data['Temperature'])
plt.title("Temperature Trend")

plt.subplot(1,2,2)
plt.scatter(data['Temperature'], data['Humidity'])
plt.title("Temp vs Humidity")

plt.savefig("combined_plots.png")
plt.show()


#Task 5: Grouping & Aggregation
monthly_stats = data.groupby('Month').agg({
    'Temperature': ['mean', 'max', 'min'],
    'Rainfall': 'sum',
    'Humidity': 'mean'
})

print(monthly_stats)

#Task 6: Save Processed Data
data.to_csv("processed_weather_data.csv", index=False) 
print("Processed data saved to 'processed_weather_data.csv'")