#Tuple is an ordered collection of elements enclosed within ()
#You cannot modify a tuple because "Tuples are Immutable"
#Without comma Tuples are treated as "Integers"


#Data :
a=(55,2,56,37,2)
b=(27,45,65,34)

#Some methods of Tuple :

#1)To find the length of the tuple
print(len(a))

#2)Concatenating Tuples 
print(a+b)

#3)Repeating Tuples
print(a*5)

#4)Concatenating and repeating Tuples
print(a*2+b*2)

#5)Finding minimum and maximum value 
print(min(a))
print(max(a))

#6)Counts the number of times the specified value occurs
print(a.count(2))

#7)Returns the index of first occurance of specified value
print(a.index(37))

#8)Interchange 
a=1
b=2
a,b=b,a
print(b,a)
print(a,b)
