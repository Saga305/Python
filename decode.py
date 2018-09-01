'''
>>>>> TESTING RESULTS:

Saga@Saga-Inspiron-5520:~/Practice/Python$ python3 decode.py
=======================================================================================
EncodedString:
 Vrphwklqj phdqlqjixo 

DecodedString:
 Something meaningful
=======================================================================================
EncodedString:
  Zulwh d surjudp (lq Sbwkrq, MdydVfulsw ru Uxeb) wr srsxodwh dqg wkhq vruw d
udqgrpob glvwulexwhg olvw ri 1 ploolrq lqwhjhuv, hdfk lqwhjhu kdylqj d ydoxh >= 1 dqg
<= 100 zlwkrxw xvlqj dqb exlowlq/hawhuqdo oleudub/ixqfwlrq iru vruwlqj.
Brxu surjudp vkrxog fduhixoob frqvlghu wkh lqsxw dqg frph xs zlwk wkh prvw hiilflhqw
vruwlqj vroxwlrq brx fdq wklqn ri. Surylgh wkh vsdfh dqg wlph frpsohalwb ri brxu
dojrulwkp  

DecodedString:
  Write a program (in Python, JavaScript or Ruby) to populate and then sort a
randomly distributed list of 1 million integers, each integer having a value >= 1 and
<= 100 without using any builtin/external library/function for sorting.
Your program should carefully consider the input and come up with the most efficient
sorting solution you can think of. Provide the space and time complexity of your
algorithm 
=======================================================================================
'''

import string


def exchangeKV(d):
	return dict((v,k) for k,v in d.items())

def createDictMappings(line):
	d = dict()
	for i in range(len(line)):
		j = (i+3) % len(line)
		d[line[i]] = line[j]
	return d

def getDictMappings():

	lower = string.ascii_lowercase
	upper = string.ascii_uppercase

	d = createDictMappings(lower)   
	d.update(createDictMappings(upper))

	return exchangeKV(d)


def decode(source_string):
	dest_string = ""
	d=getDictMappings() 

	for i in source_string:
		if(d.get(i)):
			dest_string += d.get(i)
		else:
			dest_string += i
	return dest_string

	
print("=======================================================================================")
encodedString = "Vrphwklqj phdqlqjixo"
print("EncodedString:\n",encodedString, "\n\nDecodedString:\n",decode(encodedString))
print("=======================================================================================")

encodedString = """ Zulwh d surjudp (lq Sbwkrq, MdydVfulsw ru Uxeb) wr srsxodwh dqg wkhq vruw d
udqgrpob glvwulexwhg olvw ri 1 ploolrq lqwhjhuv, hdfk lqwhjhu kdylqj d ydoxh >= 1 dqg
<= 100 zlwkrxw xvlqj dqb exlowlq/hawhuqdo oleudub/ixqfwlrq iru vruwlqj.
Brxu surjudp vkrxog fduhixoob frqvlghu wkh lqsxw dqg frph xs zlwk wkh prvw hiilflhqw
vruwlqj vroxwlrq brx fdq wklqn ri. Surylgh wkh vsdfh dqg wlph frpsohalwb ri brxu
dojrulwkp """

print("EncodedString:\n",encodedString, "\n\nDecodedString:\n",decode(encodedString))
print("=======================================================================================")
