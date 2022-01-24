#!/usr/bin/python3
""" 
This module includes a function
that divides all elements of a matrix
with given divider.
"""
from decimal import DivisionByZero


def matrix_divided(matrix, div):
	"""
	divides all elements of a matrix with given div
	@matrix: given matrix that has integers or floats
	@div: given divider
	"""
	typerr_msg = "matrix must be a matrix (list of lists) of integers/floats"
	if not isinstance(matrix,list):
		raise TypeError(typerr_msg)

	if div == 0:
		raise DivisionByZero("division by zero")

	if not isinstance(div, int) and not isinstance(div, float):
		raise TypeError("div must be a number")

	new_mtx = matrix.copy()
	for i in range(len(matrix)):
		if not isinstance(matrix[i], list):
			raise TypeError(typerr_msg)
		col_matrix = len(matrix[0])
		new_mtx[i] = matrix[i].copy()
		if len(matrix[i]) != col_matrix:
			raise TypeError("Each row of the matrix must have the same size")
		for j in range(len(matrix[i])):
			if not isinstance(matrix[i][j], int) and not isinstance(matrix[i][j], float):
				raise TypeError(typerr_msg)
			new_mtx[i][j] = round(matrix[i][j] / div, 2)
	return new_mtx


		