"""
This module contains the Laboratory class, and its associated
methods, for simulating alchemists' lab reactions.
It also includes the can_react and update_shelves functions
which can be imported.
"""

import random


def update_shelves(shelf1, shelf2, substance1, substance2_i):
    """Updates shelves by removing two presumably reacted substances."""
    if (not isinstance(shelf1, list) or not isinstance(shelf2, list)):
        raise TypeError("Shelf inputs must be in list format.")
    index1 = shelf1.index(substance1)
    shelf1 = shelf1[:index1] + shelf1[index1+1:]
    shelf2 = shelf2[:substance2_i] + shelf2[substance2_i+1:]
    return shelf1, shelf2


def can_react(substance1, substance2):
    """Checks if two substances are reactive.
    In this case, substances react with 'anti'-substances.
    This function can be modified for different types of reactions."""
    for substance in [substance1, substance2]:
        if (substance == '' or substance == 'anti'):
            raise ValueError("Empty string not allowed!")
        if 'antianti' in substance:
            raise ValueError(
                "'antiantix' substances must be renamed to 'x'")
    sub1, sub2 = substance1, substance2
    return sub1 == "anti" + sub2 or sub2 == "anti" + sub1


class Laboratory(object):
    """
    This class allows the instantiation of a Laboratory object,
    with which laboratory reactions can be simulated by associated methods.
    """
    def __init__(self, lower_shelf, upper_shelf):
        """Instantiates a Laboratory object."""
        self.lower_shelf = lower_shelf
        self.upper_shelf = upper_shelf
        for shelf in [lower_shelf, upper_shelf]:
            if (not shelf):
                print("One or more of your shelves is empty!")
            if (not isinstance(shelf, list)):
                raise TypeError("Shelf inputs must be in list format.")
        for substance in list(set(lower_shelf) | set(upper_shelf)):
            if (substance == '' or substance == 'anti'):
                raise ValueError("Empty string not allowed!")
            if 'antianti' in substance:
                raise ValueError(
                    "'antiantix' substances must be renamed to 'x'")

    def do_a_reaction(self, shelf1=None, shelf2=None):
        """Performs one reaction on the laboratory."""
        if (not isinstance(shelf1, list) or not isinstance(shelf2, list)):
            if shelf1 is None and shelf2 is None:
                shelf1 = self.lower_shelf
                shelf2 = self.upper_shelf
            else:
                raise TypeError("Shelf inputs must be in list format.")
        for substance1 in shelf1:
            possible_targets = [i for i, target in enumerate(shelf2)
                                if can_react(substance1, target)]
            if not possible_targets:
                continue
            else:
                substance2_i = random.choice(possible_targets)
                return update_shelves(shelf1, shelf2, substance1, substance2_i)
        return shelf1, shelf2

    def all_reactions(self):
        """Simulates all possible reactions.
        Returns a tuple of number of reactions, and final state of shelves."""
        shelf1 = self.lower_shelf
        shelf2 = self.upper_shelf
        count = 0
        ended = False
        while not ended:
            shelf1_new, shelf2_new = self.do_a_reaction(shelf1, shelf2)
            if shelf1_new != shelf1:
                count += 1
            ended = (shelf1_new == shelf1) and (shelf2_new == shelf2)
            shelf1, shelf2 = shelf1_new, shelf2_new
        final_shelves = [shelf1, shelf2]
        return count, final_shelves

    def run_full_experiment(self):
        """Simulates all possible reactions,
        and prints the count and final state of shelves in a verbose way."""
        count, final_shelves = self.all_reactions()
        f_s = final_shelves
        print("Total number of reactions: {}".format(count))
        print("Final contents\n\t - lower:{}\n\t - upper:{}".format(*f_s))
