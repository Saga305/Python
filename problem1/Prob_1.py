"""
This problem was asked by Microsoft.
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.
For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""

import itertools

def check(wordSet, wordString):
	combination ,result = [ [] for i in range(2) ]
	for i in range(len(wordSet)+1):
		combination += itertools.permutations(wordSet, i)

	for j in combination:
		if (''.join(j) == wordString):
			result.append(list(j))
	return result

def test(wordSet,wordString):
	result = check(wordSet,wordString)
	if (len(result)):
		return result
	else:
		return None

print(test(['quick', 'brown', 'the', 'fox'],'thequickbrownfox'))
print(test(['quick', 'brown', 'the', 'fox'],'quickbrownfoxthe'))
print(test(['quick', 'brown', 'the', 'fox'],'quickbrownfox'))
print(test(['quick', 'brown', 'the', 'fox'],'quickfox'))
print(test(['quick', 'brown', 'the', 'fox'],'LazyDog'))
print(test(['bed','bath','bedbath','and','beyond'],'bedbathandbeyond'))
