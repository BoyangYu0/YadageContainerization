#!/usr/bin/env python
import numpy
import sys

input_file = str(sys.argv[1])
number_of_randoms = int(sys.argv[2])
output_file = str(sys.argv[3])

with open(input_file, "r") as input:
    numpy.random.seed(int(input.readlines()[0]))
with open(output_file, "w") as output:
    for i in range(number_of_randoms):
        output.write(str(numpy.random.random())+'\n')
