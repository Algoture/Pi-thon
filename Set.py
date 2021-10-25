#A set is a collection which is both unordered and unindexed collection of elements enclosed with {}
#Duplicates are not allowed in Sets..!!

#Data :
l={1,2,3,4,4}
l2={8,7,6,5,5}
l22={"Umesh","Yogesh","Ramesh","Sandesh"}
# s=set(1)

#1)Adding an element to the set :
l.add(8)
l.add(10)
print(l)

#2)Removing all the elements from the set:
# l.clear()
# print(l)

#3)Returns a copy of the set :
l.copy()
print(l)

#4)Returns a set containing the difference between two or more sets :
t=l.difference(l2)
print(t)

#5)Removing the specified item from the list :
r=l.discard(10)
print(r)

#6)Returns a set, that is the intersection of two or more :
q=l.intersection(l2)
print(q)

#7)Removing an element from the set (Removes a random element) :
l.pop()
print(l)

#8)Removing a specified element from the set :
l22.remove("Ramesh")
print(l22)

#9)Returns a set, that is the union of two or more (Union means all the items in the set except duplicates..!!) :
w=l.union(l2)
print(w)

#10)




# s=set(l)
# print(l)
# t=set([1,2,3,4])
# t1=set([4,5,6,7,8,8,9])
# t2=set([7,9,1,2])
# print(t4,t2)
# s = set()
# print(type(s))
a=[1,1,45,45,8,9,6,7]
b=set(a)
print(type(b))

