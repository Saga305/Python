x = [1,2,3,4,5,6,7,8,9,10];
print (dir(x));
#print (help(x.remove));
print (help(del()));
print (x);
'''
remove(...) method of builtins.list instance
    L.remove(value) -> None -- remove first occurrence of value.
    Raises ValueError if the value is not present.
'''

x.remove(4);
print (x);

'''
pop(...) method of builtins.list instance
    L.pop([index]) -> item -- remove and return item at index (default last).
    Raises IndexError if list is empty or index is out of range.
'''
print (x.pop(2));
print (x);

