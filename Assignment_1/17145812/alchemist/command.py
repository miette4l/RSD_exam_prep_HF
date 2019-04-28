#!/usr/bin/env python
"""
Command-line script which takes a .yml Laboratory input file
and returns the final state of shelves.
Can be run with '--reactions' to display only the number of reactions.
"""

from argparse import ArgumentParser
import os

import yaml

from alchemist.laboratory import Laboratory


def check_ext(filepath):
    ext = os.path.splitext(filepath)[1]
    if not (ext == '.yml' or ext == '.yaml'):
        raise TypeError("Laboratory input file must be in yaml format.")


def check_dict(labdict):
    if not isinstance(labdict, dict):
        raise TypeError("Laboratory input file must be in yaml format.")


def check_keys(labdict):
    if len(labdict.keys()) != 2:
        raise TypeError("Laboratory input file must have exactly two shelves.")


def process():
    """Active code referred to via entry_points function"""
    parser = ArgumentParser(description="Display final state of shelves.")
    parser.add_argument('--reactions', '-r', action="store_true",
                        help="Display only the number of reactions.")
    parser.add_argument('filepath',
                        help="Input two-shelf laboratory file in yaml format.")
    args = parser.parse_args()

    check_ext(args.filepath)

    with open(args.filepath) as file:
        labdict = yaml.load(file)

    check_dict(labdict)

    check_keys(labdict)

    lab = Laboratory(labdict['lower'], labdict['upper'])
    count, final_shelves = lab.all_reactions()
    if args.reactions:
        print("{}".format(count))
    else:
        print("lower: {}\nupper: {}".format(*final_shelves))


if __name__ == "__main__":
    process()
