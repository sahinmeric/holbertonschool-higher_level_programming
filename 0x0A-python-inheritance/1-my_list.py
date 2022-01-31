#!/usr/bin/python3
"""
MyList class module contains a class named MyList
that has a public instance function that prints
the list items
"""


class MyList(list):
	"""class MyList that inherits from list"""
	def print_sorted(self):
		"""that prints the list, but sorted (ascending sort)"""
		print(sorted(self))
