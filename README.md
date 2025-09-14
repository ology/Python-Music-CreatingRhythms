# Music CreatingRhythms
Combinatorial algorithms to generate rhythms

## DESCRIPTION

This package provides most of the the combinatorial algorithms described in the book, "Creating Rhythms", by Hollos. Many of these algorithms are ported directly from the C, and are pretty fast. Please see the links below for more information.

NB: Arguments are sometimes switched between book and software.

Additionally, this module provides utilities that are not part of the book but are handy nonetheless.

## METHODS

### b2int
This method takes a set of binary sequences and converts them into intervals.

That is, it converts binary sequences of the form `[[1],[1,0],[1,0,0]]` into a set of intervals of the form `[[1],[2],[3]]`.

This basically is the number of zeros following a one.