#!/usr/bin/env python

from argparse import ArgumentParser
from timeit import timeit
from matplotlib import pyplot as plt


parser = ArgumentParser(description="Generate performance plot")
parser.add_argument("levels", type=int)
parser.add_argument("-np", help="run NumPy solution",
                    action="store_true")
args = parser.parse_args()


def time_to_plot(count, np=False):
    if np is False:
        return timeit("plotTree(0, 0, 0.6, b, 0.1, plot=False)",
                      f"from tree import plotTree; b = {count}",
                      number=10000)
    if np is True:
        return timeit("plotTree(0, 0, 0.6, b, 0.1, plot=False)",
                      f"from tree_np import plotTree; b = {count}",
                      number=10000)


def get_times(levels, np):
    times = []
    for branch_level in range(levels+1):
        t = time_to_plot(branch_level, np) * 100  # for time units
        times.append(t)
    return times


def make_graph(levels, np):
    plt.plot(range(levels+1), get_times(levels, np))
    plt.ylabel("time (μs)")
    plt.xlabel("branch level")
    plt.savefig("perf_plot.png")


if __name__ == "__main__":
    make_graph(args.levels, args.np)
