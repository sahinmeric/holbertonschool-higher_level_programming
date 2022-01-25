#!/usr/bin/python3
"""
This module contains a class
"""

class LockedClass():
	"""class that allows the first name
	attribute to be created only"""
	__slot__ = ["first_name"]
