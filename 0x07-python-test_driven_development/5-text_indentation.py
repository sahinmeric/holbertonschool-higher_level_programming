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
	if not isinstance(text, str):
		raise TypeError("text must be a string")
	flag = 0
	for c in text:
		if flag == 0:
			if c == '.' or c == ':' or c == '?':
				print("{}\n".format(c))
				flag = 1
			else:
				print(c, end="")
				flag = 0
				continue
		if flag == 1:
			if c == '.' or c == ':' or c == '?' or c == ' ':
				continue	
			else:
				print(c, end="")
				flag = 0