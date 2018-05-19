''' string format method'''
age = 25
print("i am " + str(age) + " years old.")
print("i am {} years old".format(age))
print("i am {age} years old, Are you {age} years old too?".format(age=age))
print("i am {} years old, Are you {} years old?".format(age,30))
seconds = age * 365 * 24 * 3600
print("i have lived  for {} seconds.".format(seconds))