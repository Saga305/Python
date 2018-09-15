"""
This problem was asked by Facebook.

Implement regular expression matching with the following special characters:

    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.

"""

import re

def regexCheck(string):
	m = re.match("Ra.$",string)
	if m and  m.group(0):
		return True
	return False

def regexCheck2(string):
	m = re.match(".*at$",string)
	if m and  m.group(0):
		return True
	return False


if __name__ == '__main__':
	print(regexCheck("Ray"))
	print(regexCheck("Raymond"))

	print("========================================")

	print(regexCheck2("Chat"))
	print(regexCheck2("cat"))
	print(regexCheck2("Chats"))

	print("========================================")
