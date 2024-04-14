#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 17:29:02 2024

@author: calebhofmann
"""

import pandas as pd
import numpy as np
from scipy.stats import skew
import matplotlib.pyplot as plt

df = pd.read_excel('CPI Skewness.xlsx', sheet_name='CNB CPI Data')

def calculate_monthly_price_changes_and_log(row):
    price_changes = [np.log(value) - np.log(100) for value in row[2:]]
    return price_changes

df['Monthly Price Changes (Log)'] = df.apply(calculate_monthly_price_changes_and_log, axis=1)

def calculate_monthly_skewness(row):
    return skew(row['Monthly Price Changes (Log)'])

df['Monthly Skewness (Log)'] = df.apply(calculate_monthly_skewness, axis=1)

print(df[['Classification ECOICOP', 'Monthly Skewness (Log)']])


df.sort_values(by='Classification ECOICOP', inplace=True)

plt.figure(figsize=(10, 6))  

plt.plot(df['Classification ECOICOP'], df['Monthly Skewness (Log)'], marker='o', linestyle='-')

plt.title('Monthly CPI Skewness, Czech Republic, 2018-Pres')
plt.xlabel('Date')
plt.ylabel('Monthly Skewness (Log)')

plt.xticks(rotation=45)

plt.grid(True) 
plt.tight_layout()  
plt.show()


df.sort_values(by='Classification ECOICOP', inplace=True)

df['Average Price Change (Log)'] = df['Monthly Price Changes (Log)'].apply(np.mean)

monthly_average_price_change = df.groupby(df['Classification ECOICOP'].dt.to_period('M'))['Average Price Change (Log)'].mean()

monthly_average_price_change_df = monthly_average_price_change.reset_index()

plt.figure(figsize=(10, 6))  

plt.plot(monthly_average_price_change_df['Classification ECOICOP'].dt.to_timestamp(), monthly_average_price_change_df['Average Price Change (Log)'], marker='o', linestyle='-')

plt.title('Mean Log Price Change, Czech Republic, 2018-Pres')
plt.xlabel('Date')
plt.ylabel('Average Price Change (Log)')

plt.xticks(rotation=45)


plt.grid(True) 
plt.tight_layout()  
plt.show()
