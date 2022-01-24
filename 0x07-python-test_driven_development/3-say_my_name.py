#!/usr/bin/python3
"""
this module includes a function that prints given arguments
"""


def say_my_name(first_name, last_name=""):
	"""
	this function receives two strings and prints them
	@first_name: first argument which is name
	@last_name: second argument which is last name, default value is ""
	"""
	if first_name == "":
		print("first name can't be empty")
		return
	if not isinstance(first_name, str):
		raise TypeError("first_name must be a string")
	if not isinstance(last_name, str):
		raise TypeError("last_name must be a string")
	if any(char.isdigit() for char in first_name):
		print("first name can't contiene digits")
		return
	if any(char.isdigit() for char in last_name):
		print("last name can't contiene digits")
		return
	if first_name is None:
		raise SyntaxError("invalid syntax")
	print("My name is {} {}".format(first_name,last_name))