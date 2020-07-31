#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 02:03:24 2020

@author: pedro
"""
import pandas as pd
import numpy as np
import datetime
import random

# create companies names, fuel sources, location, etc.
companies_names = ['Solar Generation SA','Green Energy Co',
                   'Coal is Life','Thermal Gen', 'Go Green']

fuel_sources = ['Solar', 'Solar', 'Coal', 'Gas','Wind']

location = ['NE','CO','SE','S','N']

capacity = ['50', '40', '100', '50', '30']

gen_id = ['Solar Generation SA','Green Energy Co',
          'Coal is Life','Coal is Life','Thermal Gen',
          'Thermal Gen','Go Green']

# create dictionaries
df_gen_id = pd.DataFrame(zip(list(range(8)),gen_id), columns=['sensor','company'])
df_fuel = pd.DataFrame(zip(companies_names,fuel_sources), columns=['company','fuel'])
df_location = pd.DataFrame(zip(companies_names,location), columns=['company','location'])

dicts_sensors = dict(zip(list(range(8)),gen_id))
dicts_source = dict(zip(companies_names,fuel_sources))
dicts_location = dict(zip(companies_names,location))
dicts_cap = dict(zip(companies_names,capacity))

# create timestamps
start_datetime = datetime.datetime(2019,1,1,1,0)
end_datetime = datetime.datetime(2019,7,1,1,0)
interval = datetime.timedelta(hours = 4)

# populate simulation
time = start_datetime
trend = 0
df = pd.DataFrame(columns=['time', 'sensor_reading', 'sensor_id'])

while time < end_datetime:

    s_cap = float(dicts_cap['Solar Generation SA'])*(1 + trend)
    g_cap = float(dicts_cap['Green Energy Co'])*(1 + trend)
    c_cap = float(dicts_cap['Coal is Life'])*(1 - trend)
    t_cap = float(dicts_cap['Thermal Gen'])*(1 - trend)
    gg_cap = float(dicts_cap['Go Green'])*(1 + trend)
        
    # simulate sensors readings
    s_gen = random.gauss(s_cap,2)
    g_gen = random.gauss(g_cap,2)
    c_gen1 = random.gauss(c_cap/2,2)
    c_gen2 = random.gauss(c_cap/2,2)
    t_gen1 = random.gauss(t_cap/2,2)
    t_gen2 = random.gauss(t_cap/2,2)
    gg_gen = random.gauss(s_cap,2)
    
    df2 = pd.DataFrame(np.array([[time, time, time, time, time, time, time],
                        [s_gen, g_gen, c_gen1, c_gen2, t_gen1, t_gen2, gg_gen],
                        list(range(7))]).T,
                        columns=['time', 'sensor_reading', 'sensor_id'])
    df = df.append(df2)
    
    time += interval
    trend += 0.0002
    
final_df = df.merge(df_gen_id, left_on = 'sensor_id', right_on = 'sensor')
final_df = final_df.merge(df_fuel, on = 'company')
final_df = final_df.merge(df_location, on = 'company')

# save to csv
final_df.to_csv('data.csv')


# create simplified to df to load the blockchain
import datetime
def to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day

final_df['int_time'] = final_df.time.apply(to_integer)
final_df['int_sensor'] = final_df.sensor_reading.apply(round)

simple_df = final_df[['int_time','sensor_id','int_sensor']]
simple_df.to_csv('data_simple.csv')



