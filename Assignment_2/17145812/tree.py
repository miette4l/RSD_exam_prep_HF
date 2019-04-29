#!/usr/bin/env python

"""
This is an improved version where I've got rid of some repetition in code by creating small functions.
"""

from argparse import ArgumentParser
from math import sin, cos
from matplotlib import pyplot as plt

def append_newvalue(x1, y1, a1, angle, nodes, s, sign):
    return nodes.append([x1+s*sin(sign), y1+s*cos(sign), sign])

def plot_branch(handedness, x1, y1, nodes):
    if handedness == 'left':
        v = -2
    if handedness == 'right':
        v = -1
    return plt.plot([x1, nodes[v][0]], [y1, nodes[v][1]])

def plotTree(x1, y1, lengths, levels, angle, scale, plot=True):

    s = scale
    rotation = 0
    d = [[x1, y1+scale, rotation]]

    if plot:
        plt.plot([x1, x1], [y1, y1+scale])  # plot trunk

    for level in range(levels):
        nodes = []
        for coord in d:
            x1, y1, a1 = coord[0], coord[1], coord[2]
            difference = a1-angle
            sum_ = a1+angle
            append_newvalue(x1, y1, a1, angle, nodes, s, difference)
            append_newvalue(x1, y1, a1, angle, nodes, s, sum_)
            if plot:
                plot_branch('left', x1, y1, nodes)
                plot_branch('right', x1, y1, nodes)
        d = nodes
        s *= lengths

    if plot:
        plt.savefig("tree.png")


if __name__ == "__main__":
    parser = ArgumentParser(description="Generate tree of life")
    parser.add_argument("x1", type=float, help="initial x-position where graph begins", default='0', nargs='?')
    parser.add_argument("y1", type=float, help="initialyx-position where graph begins", default='0', nargs='?')
    parser.add_argument("lengths", type=float, help="choose branch lengths", default='0.6', nargs='?')
    parser.add_argument("levels", type=int, help="choose the number of branch levels, or in other words the depth of the tree", default='5', nargs='?')
    parser.add_argument("angle", type=float, help="choose the angle of branches", default='0.1', nargs='?')
    parser.add_argument("scale", type=float, help="choose the scale of the tree", default='1', nargs='?')
    parser.add_argument("-p", help="turn off plotting",
                        action="store_false")
    args = parser.parse_args()

    plotTree(args.x1, args.y1, args.lengths, args.levels, args.angle, args.scale, plot=args.p)
