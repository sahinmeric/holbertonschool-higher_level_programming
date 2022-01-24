#!/usr/bin/python3
"""
This script includes a function that receives two arguments
and returns sum of them
"""
def add_integer(a, b=98):
	"""
	This function receives two argument and returns sum of them
	@a: integer or float 
    @b: integer or float, default is set to 98.
    Returns the result of the sum.
	"""
	if type(a) is not int and type(a) is not float:
		raise TypeError("a must be an integer")
	if type(b) is not int and type(b) is not float:
		raise TypeError("b must be an integer")
	if type(a) is float:
		a = int(a)
	if type(b) is float:
		b = int(b)
	return a + b