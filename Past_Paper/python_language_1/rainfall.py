# a)

import numpy as np
import json
from matplotlib import pyplot as plt
from statistics import mean 
import math

def data_to_dict(filepath, destination):
    with open(filepath, 'r') as f:
        data = np.genfromtxt(f, delimiter=",", names=['year','day','rainfall'])
    years = range(1937, 2012)
    diction = {}
    for year in years:
        rainfall = []
        for row in data:
            if row[0] == year:
                rainfall.append(row[2])
        diction[year] = rainfall
        
    with open(destination, 'w') as json_file:
        json.dump(diction, json_file, indent=4)

# b)

def make_plot(filename, year, color="blue"):
    with open(filename, 'r') as f:
        mydata = f.read()
        mydict = json.loads(mydata)
    rainfall = mydict[year]
    days = range(len(rainfall))
    plt.plot(days, rainfall, color)
    plt.xlabel("Day of year")
    plt.ylabel("Rainfall (mm)")
    plt.title("Daily rainfall")

# see '1998.png' for the saved plot

# c)

def mean_for_period(filename, start, end):
    with open(filename, 'r') as f:
        mydata = f.read()
        mydict = json.loads(mydata)
    period = range(int(start), int(end)+1)
    rain_data = []
    for year in list(period):
        rainfall = mydict[str(year)]
        mean_rainfall = mean(rainfall)
        rain_data.append(mean_rainfall)
    plt.plot(list(period), rain_data)
    plt.xlabel("Year")
    plt.ylabel("Mean rainfall for year (mm)")
    plt.title("Yearly mean rainfall over given period")

# see '1999-2000.png' for the saved plot

# d) 

def apply_correction(value):
    corr = 1.2**(math.sqrt(2))
    return value*corr

def apply_to_year_1(filename, year):
    with open(filename, 'r') as f:
        mydata = f.read()
        mydict = json.loads(mydata)
    rainfall = mydict[year]
    new_list = []
    for element in rainfall:
        new_list.append(apply_correction(element))
    return new_list

def apply_to_year_2(filename, year):
    """
    Apply correction factor to all of the data for a given year, using list comprehension.
    The list comprehension method is quicker because it does not need to call the append function and load the new_list for every element.
    However, the list comprehension is less readable than the for-loop in apply_to_year_1.
    """
    with open(filename, 'r') as f:
        mydata = f.read()
        mydict = json.loads(mydata)
    rainfall = mydict[year]
    new_list = [apply_correction(element) for element in rainfall]
    return new_list