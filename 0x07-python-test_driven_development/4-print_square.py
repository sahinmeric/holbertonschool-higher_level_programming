#!/usr/bin/python3
""" 
This module contains a function
that prints a square of # with given size
"""

from typing import Type


def print_square(size):
	"""
	This function receives an integer argument
	and prints a square of size of given integer
	"""
	if size < 0 and isinstance(size, float):
		raise TypeError("size must be an integer")
	if not isinstance(size, int):
		raise TypeError("size must be an integer")
	if size < 0:
		raise ValueError("size must be >= 0")
	for i in range(size):
		for j in range(size):
			print("#", end="")
		print()