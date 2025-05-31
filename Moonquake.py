# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:40:53 2024

@author: USER
"""

import numpy as np
import pandas as pd
from obspy import read
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import os

#%%

cat_directory = 'C:/Users/USER/Downloads/space_apps_2024_seismic_detection/data/lunar/training/catalogs/'
cat_file = cat_directory + 'apollo12_catalog_GradeA_final.csv'
cat = pd.read_csv(cat_file)
cat

row = cat.iloc[6]
arrival_time = datetime.strptime(row['time_abs(%Y-%m-%dT%H:%M:%S.%f)'],'%Y-%m-%dT%H:%M:%S.%f')
arrival_time

arrival_time_rel = row['time_rel(sec)']
arrival_time_rel


test_filename = row.filename
test_filename


data_directory = 'C:/Users/USER/Downloads/Testfile/'
csv_file = 'xa.s12.00.mhz.1970-06-26HR00_evid00002.csv'
data_cat = pd.read_csv('C:/Users/USER/Downloads/Testfile/xa.s12.00.mhz.1970-04-25HR00_evid00006.csv')
data_cat


# Read in time steps and velocities
csv_times = np.array(data_cat['time_rel(sec)'].tolist())
csv_data = np.array(data_cat['velocity(m/s)'].tolist())
# Plot the trace!

fig,ax = plt.subplots(1,1,figsize=(10,3))
ax.plot(csv_times,csv_data)

# Make the plot pretty
ax.set_xlim([min(csv_times),max(csv_times)])
ax.set_ylabel('Velocity (m/s)')
ax.set_xlabel('Time (s)')
ax.set_title('xa.s12.00.mhz.1970-01-19HR00_evid00006', fontweight='bold')

