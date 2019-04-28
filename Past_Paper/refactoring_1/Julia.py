#!/usr/bin/env python
from argparse import ArgumentParser
from numpy import zeros
import matplotlib.pyplot as plt

if __name__ == "__main__":
    parser = ArgumentParser(description="Generate Julia set from parameters")
    parser.add_argument('rows', type=int)
    parser.add_argument('columns', type=int)
    parser.add_argument('steps', type=int)
    parser.add_argument('shape_1', type=float)
    parser.add_argument('shape_2', type=float)
    arguments = parser.parse_args()
    
    rows = arguments.rows
    columns = arguments.columns

    
def create_empty_array(rows, columns):
    myarray = zeros([rows, columns])
    return myarray


def fill_array(myarray):  
    """
    This function populates the array with values which when plotted create the Julia set.
    """
    (rows, columns) = myarray.shape
    scale = 0.5
    xcontract = 1.5
    ycontract = 1.0
    steps = arguments.steps
    shape_1 = arguments.shape_1
    shape_2 = arguments.shape_2

    for col in range(columns):
        for row in range(rows):
            zx = xcontract*(col-columns/2)/(scale*columns)
            zy = ycontract*(row-rows/2)/(scale*rows)
            i = steps
            t = True
            while t is True:
                if zx*zx + zy*zy >= 4:
                    t = False
                if i <= 1:
                    t = False
                a = zx * zx - zy * zy - shape_1
                zy = 2.0 * zx * zy + shape_2
                zx = a
                i = i - 1
            myarray[row][col] = i
            
    return myarray


def plot_array(array):
    plt.imshow(array)
    plt.savefig('Julia.png')

    
def julia():
    myarray = create_empty_array(rows, columns)
    fill_array(myarray)
    plot_array(myarray)
    
    
julia()
