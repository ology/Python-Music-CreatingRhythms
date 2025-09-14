# Music Creating-Rhythms
Combinatorial algorithms to generate rhythms

## DESCRIPTION

This package provides most of the the combinatorial algorithms described in the book, "Creating Rhythms", by Hollos.

Additionally, this module provides utilities that are not part of the book but are handy nonetheless.

The `comp*` methods are used to generate compositions of numbers, which are ways to partition an integer into smaller parts. The arguments passed to these functions determine the specific composition that is generated.

The `neck*` methods generate binary necklaces of a certain length with or without specific constraints on their intervals.

The `part*` methods are used to generate all possible partitions of an integer into smaller parts, either with or without specific constraints on the lengths of those parts.

NB: Arguments are sometimes switched between book and software.

## EXAMPLE
```python
from music_creatingrhythms import Rhythms
r = Rhythms()
e = r.euclid(6,16) # => [1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0]
```

## METHODS

### b2int
This method takes a set of binary sequences and converts them into intervals.

That is, it converts binary sequences of the form `110100` into a set of intervals of the form `[1,2,3]`.

### cfcv
This method calculates the continued fraction convergent given a set of terms. It is used to find the best rational approximations to real numbers by using their continued fraction expansions.

### cfsqrt
Calculate the continued fraction for `sqrt(n)` to `m` digits, where `n` and `m` are integers.

## chsequl
Generate the upper or lower Christoffel word for `p` and `q`.

Arguments:
```
t: required type of word (u: upper, l: lower)
p: required numerator of slope
q: required denominator of slope
n: optional number of terms to generate, default: p+q
```

### comp
Generate all compositions of `n`.

A "composition" is the set of combinatorial "variations" of the partitions of `n` with the duplicates removed.

### compa
Generate compositions of n with allowed intervals `p1, p2, ... pn`.

Here, the "intervals" are the terms of the partition.

### compam
Generate compositions of n with m parts and allowed intervals `p1, p2, ... pn`.

Here, the "parts" are the number of elements of each interval set.

### compm
Generate all compositions of `n` into `m` parts.

Again, the "parts" are the number of elements of each interval set.

### compmrnd
Generate a random composition of `n`.

### comprnd
Generate a random composition of `n`.

### count_digits
Count the number of a given digit in a string or vector.

### count_ones
Count the number of `1`s in a string or vector.

### count_zeros
Count the number of `0`s in a string or vector.

### de_bruijn
This method generates the largest de Bruijn sequence of order `n`, which is a cyclic sequence containing all possible combinations of length `n` with no repeating subsequences.

### euclid
Generate a Euclidean rhythm given `n` onsets distributed over `m` beats.

### int2b
Convert intervals of the form `[2,3]` into a set of binary sequences.

### invert_at
Invert a section of a `parts` binary sequence at `n`.

### neck
Generate all binary necklaces of length `n`.

### necka
Generate binary necklaces of length `n` with allowed intervals `p1, p2, ... pn`. For these "necklace" class of methods, the word "intervals" refers to the size of a number given trailing zeros. So intervals `1`, `2`, and `3` are represented as `1`, `1,0`, and `1,0,0`, respectively.

### neckam
Generate binary necklaces of length `n` with `m` ones, and allowed intervals `p1, p2, ... pn`.

### neckm
Generate all binary necklaces of length `n` with `m` ones.

### part
Generate all partitions of `n`.

### parta
Generate all partitions of `n` with allowed intervals `p1, p2, ... pn`.

### partam
Generate all partitions of `n` with `m` parts from the intervals `p1, p2, ... pn`.

### partm
Generate all partitions of `n` into `m` parts.

### permi
Return all permutations of the given parts list.

### pfold
Generate "paper folding" sequences, where `n` is the number of terms to calculate, `m` is the size of the binary representation of the folding function, and `f` is the folding function number, which can range from `0` to `2^m - 1`.

This method generates "paper folding" sequences, which are binary sequences that represent the creases on a piece of paper after it has been folded multiple times in different directions. The arguments passed to this function determine the specific sequence that is generated.

To quote the book, "Put a rectangular strip of paper on a flat surface in front of you, with the long dimension going left to right. Now pick up the right end of the paper and fold it over onto the left end. Repeat this process a few times and unfold the paper. [There will be] a sequence of creases in the paper, some will look like valleys and some will look like ridges... Let valley creases be symbolized by the number 1 and ridge creases by the number 0..."

### reverse_at
Reverse a section of a `parts` sequence at `n`.

### rotate_n
Rotate a necklace of the given `parts`, `n` times.

## SEE ALSO
https://abrazol.com/books/rhythm1/ - "Creating Rhythms", the book.

Please see the tests.py program in this distribution for method usage.
