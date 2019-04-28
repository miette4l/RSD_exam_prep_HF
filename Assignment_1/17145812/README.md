alchemist - a package for any alchemist and their helper!

This is a simple library for simulating laboratory reactions.

Usage:

Invoke the tool on the command line with 'abracadabra <YourLaboratory>', where <YourLaboratory> must be a yaml file representing the contents of your alchemist's laboratory shelf-by-shelf, with the substances on each shelf written in the order they appear. Shelves must be named 'lower' and 'upper' and there must be exactly two shelves.
    
Run with the optional flag '--reactions' to display only the number of reactions produced.

The library 'Laboratory' may also be imported, which allows Laboratory objects to be instantiated and related methods to be run on them within a Python 3 environment.