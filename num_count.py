'''
Define a function find occurance of given number into square of given number range starts from 1.
'''

def ng_digit(n,d):
        count =0
        for i in range(n+1):
                res = i * i
                count += str(res).count(str(d))
        return count

print(ng_digit(10,1))
