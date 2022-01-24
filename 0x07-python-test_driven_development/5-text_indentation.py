#!/usr/bin/python3
"""
This module contains a function that 
prints a text with 2 new lines after
each of these characters: . ? and :
"""

def text_indentation(text):
	"""
	this funtion receives a text
	and prints 2 new lines after each of these characters . ? and :
	@text: given text
	"""
	if text is not isinstance(text, str):
		raise TypeError("text must be a string")
	if text is None or len(text) <=0:
		raise TypeError("text must be a string")
	