#!/usr/bin/env python
from argparse import ArgumentParser
from numpy import zeros
import matplotlib.pyplot as plt

    
def create_empty_array(rows, columns):
    myarray = zeros([rows, columns])
    return myarray

def new_val(contraction, axis, shape, scale):
    new = contraction*(axis-shape/2)/(scale*shape)
    return new

def fill_array(myarray, steps, shape_1, shape_2):  
    """
    This function populates the array with values which when plotted create the Julia set.
    """
    (rows, columns) = myarray.shape
    scale = 0.5
    xcontract = 1.5
    ycontract = 1.0

    for col in range(columns):
        for row in range(rows):
            zx = new_val(xcontract, col, columns, scale)
            zy = new_val(ycontract, row, rows, scale)
            i = steps
            t = True
            while (zx*zx + zy*zy < 4 and i > 1): # combined these
                a = zx * zx - zy * zy - shape_1
                zy = 2.0 * zx * zy + shape_2
                zx = a
                i -= 1 # shortened this
            myarray[row][col] = i
            
    return myarray


def plot_array(array):
    plt.imshow(array)
    plt.savefig('Julia.png')

    
def julia(rows, columns, steps, shape_1, shape_2):
    myarray = create_empty_array(rows, columns)
    fill_array(myarray, steps, shape_1, shape_2)
    plot_array(myarray)
    
    
if __name__ == "__main__":
    parser = ArgumentParser(description="Generate Julia set from parameters")
    parser.add_argument('rows', type=int, default='600', nargs='?', help='number of rows in the array')
    parser.add_argument('columns', type=int, default='800', nargs='?', help='number of columns in the array')
    parser.add_argument('steps', type=int, default='255', nargs='?', help='number of steps to iterate through when creating the fractal: this gives detail')
    parser.add_argument('shape_1', type=float, default='0.7', nargs='?', help='one of the parameters that changes the shape of the fractal')
    parser.add_argument('shape_2', type=float, default='0.27015', nargs='?',  help='another parameter that changes the shape of the fractal')
    arguments = parser.parse_args()
    
    rows = arguments.rows
    columns = arguments.columns
    steps = arguments.steps
    shape_1 = arguments.shape_1
    shape_2 = arguments.shape_2

    julia(rows, columns, steps, shape_1, shape_2)
