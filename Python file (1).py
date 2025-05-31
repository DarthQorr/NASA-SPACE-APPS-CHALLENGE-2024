# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 22:19:21 2024

@author: USER
"""

import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import csv

def ReturnValue(result):
    return result

csv_file = input("Enter Location of the csv file: ")
data_cat = pd.read_csv(csv_file)


csv_times = np.array(data_cat['time_rel(sec)'].tolist())
csv_data = np.array(data_cat['velocity(m/s)'].tolist())

fig,ax = plt.subplots(1,1,figsize=(10,3))
ax.plot(csv_times,csv_data)

ax.set_xlim([min(csv_times),max(csv_times)])
plt.ylabel('Velocity (m/s)')
plt.xlabel('Time (s)')
ax.set_title('xa.s12.00.mhz.1975-06-17HR00_evid0006-checkpoint', fontweight='bold')



# Reading data and calculating exponent values
with open(csv_file, "r") as f4:
    a = csv.reader(f4)
    next(a)  # Skip header
    data = list(a)
    
    exponentlist = []
    size = len(data)

    # Process the data to extract exponent values
    for i in range(size):
        if "E" in data[i][2]:
            exponent = (data[i][2].split("E"))[1]
        elif "e" in data[i][2]:
            exponent = (data[i][2].split("e"))[1]
        exponentlist.append([i, float(exponent), float(data[i][1])])

    initial = 0
    primeexponent = -20
    exponentlist2 = []

    # Calculate average exponent values in chunks
    for j in range(0, size, 500):
        expsum = 0
        for i in range(initial, j):
            expsum += exponentlist[i][1]
            
        q = round(expsum / 500)
        exponentlist2.append([j, exponentlist[j][2], q])
        
        if q > primeexponent and q != 0:
            primeexponent = q
        initial = j

    # Determine the result based on prime exponent values
    res = []
    for i in range(len(exponentlist2)):
        if exponentlist2[i][2] == primeexponent:
            res.append(exponentlist2[i][0])
    
    result = []
    exception = 0
    for i in range(len(res)):
        if res[i] > 100000 + exception:
            exception = res[i]
            result.append(res[i])

    print("Start row indices:", ReturnValue(result))

    # Save the result to a CSV file for Unity to read
    output_file_path = r'C:\Users\syed6\OneDrive\Desktop\start_row_indices.csv'
    
    # Open the file in write mode
    with open(output_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write header
        writer.writerow(['StartRowIndices'])
        
        # Write data
        for row in result:
            writer.writerow([row])

    print(f"Results saved to {output_file_path}")
