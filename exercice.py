#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
	return [max(n) for n in numbers]

def join_integers(numbers):
	if len(numbers)==1:
		return numbers[0]
	else:
		nb = str(numbers.pop(0))
		return int(nb + str(join_integers(numbers)))

def generate_prime_numbers(limit):
	premiers =[]
	nombres = range(2,limit+1)
	while len(nombres) != 0:
		premiers.append(nombres[0])
		nombres = [nb for nb in nombres if not nb%nombres[0]==0 ]
	return premiers

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):

	if excluded_multiples is None:
		nombres= [i for i in range(1,num_combinations+1)]
	else:
		nombres = [i for i in range(1,num_combinations+1) if not (i%excluded_multiples == 0)]

	result = [lettre + str(nb) for nb in nombres for lettre in strings]

	return result

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
