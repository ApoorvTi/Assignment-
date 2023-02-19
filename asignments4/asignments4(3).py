#######--------->Square the Elements of a list using MAP() function ------------>########
x=[4,5,2,9]
 
print("Original list: ", x)
y = map(lambda z: z **2, x) 
print("\nSqure Of the List Elements:")
print(list(y))