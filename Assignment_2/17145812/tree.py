#!/usr/bin/env python

from argparse import ArgumentParser
from math import sin, cos
from matplotlib import pyplot as plt


def plotTree(x1, y1, lengths, levels, angle, plot=True):

    scale = 1
    s = scale
    rotation = 0
    d = [[x1, y1+scale, rotation]]

    if plot:
        plt.plot([x1, x1], [y1, y1+scale])  # plot trunk

    for level in range(levels):
        nodes = []
        for i, fork in enumerate(d):
            x1, y1, a1 = d[i][0], d[i][1], d[i][2]
            nodes.append([x1+s*sin(a1-angle), y1+s*cos(a1-angle), a1-angle])
            nodes.append([x1+s*sin(a1+angle), y1+s*cos(a1+angle), a1+angle])
            if plot:
                plt.plot([x1, nodes[-2][0]], [y1, nodes[-2][1]])
                plt.plot([x1, nodes[-1][0]], [y1, nodes[-1][1]])
        d = nodes
        s *= lengths

    if plot:
        plt.savefig("tree.png")


if __name__ == "__main__":
    parser = ArgumentParser(description="Generate tree of life")
    parser.add_argument("x1", type=float)
    parser.add_argument("y1", type=float)
    parser.add_argument("lengths", type=float)
    parser.add_argument("levels", type=int)
    parser.add_argument("angle", type=float)
    parser.add_argument("-p", help="turn off plotting",
                        action="store_false")
    args = parser.parse_args()

    plotTree(args.x1, args.y1, args.lengths, args.levels, args.angle, plot=args.p)
