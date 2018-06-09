'''
Hello All,
Here i have written a robust code to create a pattern using alphabetic characters.
=====================================================================================
Test 1:

Enter a Number:3
          c
        c-b-c
      c-b-a-b-c
        c-b-c
          c
=====================================================================================
Test 2:

Enter a Number:5
                  e
                e-d-e
              e-d-c-d-e
            e-d-c-b-c-d-e
          e-d-c-b-a-b-c-d-e
            e-d-c-b-c-d-e
              e-d-c-d-e
                e-d-e
                  e
=====================================================================================
Test 3:

Enter a Number:10
                                      j
                                    j-i-j
                                  j-i-h-i-j
                                j-i-h-g-h-i-j
                              j-i-h-g-f-g-h-i-j
                            j-i-h-g-f-e-f-g-h-i-j
                          j-i-h-g-f-e-d-e-f-g-h-i-j
                        j-i-h-g-f-e-d-c-d-e-f-g-h-i-j
                      j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j
                    j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
                      j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j
                        j-i-h-g-f-e-d-c-d-e-f-g-h-i-j
                          j-i-h-g-f-e-d-e-f-g-h-i-j
                            j-i-h-g-f-e-f-g-h-i-j
                              j-i-h-g-f-g-h-i-j
                                j-i-h-g-h-i-j
                                  j-i-h-i-j
                                    j-i-j
                                      j
=====================================================================================
'''

import string
alpha= string.ascii_lowercase
n = int(input("Enter a Number:"))
L = [ (lambda x : (' '*((2*n)+(2*i)) + x[::-1]+x[1:]))('-'.join(alpha[i:n])) for i in range (n) ]  
print('\n'.join(L[::-1]+L[1:]))	
