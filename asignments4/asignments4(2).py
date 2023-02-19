#####--------->Triple all Numbers of a given List of Integers. Use Python MAP <-------------############

l=[1,2,3,4,5,6,7]
 
print("Original list: ", l)
a = map(lambda b: b * 3, l) 
print("\nTriple of said list numbers:")
print(list(a))