#!/usr/bin/env python

from argparse import ArgumentParser
from matplotlib import pyplot as plt
import numpy as np


def plotTree(x1, y1, lengths, levels, angle, plot=True):

    scale = 1
    rotation = 0
    coords = np.array([[x1, y1+scale, rotation]])

    if plot:
        plt.plot([x1, x1], [y1, y1+scale])  # plot trunk

    for level in range(levels):
        next_coords = np.empty([len(coords)*2, 3])
        for i, fork in enumerate(coords):
            x1, y1, a1 = coords[i][0], coords[i][1], coords[i][2]
            c = np.full(3, a1)
            n = np.hstack((c-angle, c+angle))
            n = n.reshape(2, 3)
            n[:, 0] = scale*np.sin(n[:, 0])
            n[:, 1] = scale*np.cos(n[:, 1])
            pos = np.array([x1, y1, 0])
            n = n + pos
            next_coords[2*i] = n[0]
            next_coords[2*i + 1] = n[1]
            if plot:
                plt.plot([x1, n[0][0]], [y1, n[0][1]])
                plt.plot([x1, n[1][0]], [y1, n[1][1]])
        coords = next_coords
        scale *= lengths

    if plot:
        plt.savefig("tree_np.png")


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
