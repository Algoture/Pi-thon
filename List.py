#List is an ordered collection of elements enclosed with []
#Lists are "Mutable"

#Data :
l1 = ["Peanut Butter","Moong Dal","Nirma","Harbar Dal"]
l2 = [2, 7, 9, 4,27,54,42]
l3 = [2,312,4324,324]

#Some methods of List :

#1)Adding a new element to the list
l1.append("Cinthol Soap")
l1.append("Banana")
l1.append("Samosa")
l1.append("Maggi")
print(l1)

#2)Sorting  the list
l2.sort()
print(l2)

#3)Adding a new element at specified position 
l1.insert(2, "Potato") 
print(l1)

#4)Adding a new element to the end of the current list
l1.extend("Key")
print(l1)

#5)Reversing the order of the list
l2.reverse()
print(l2)

#6)Removing the first item with the specified value
l2.remove(9)
print(l2)

#7)Pop out an element with the specified index number
#Pop function pop out the last character by default..!!
l3.pop(2)
print(l3)

#8)Returns the specified value
print(l1[0])
print(l2[2])


#list slicing
# print(vinay[::2]) #third parameter skips the characters
# print(vinay[::-2]) #negative slicing reverses the integers
# #length, maximum and minimum
"""it is recommended that do not use -2 or greater than -1 as it sometimes does not works
avoid negative slicing as much as you can..!!
 """




#Mutable - Can Change
#Immutable -  Cannot Change
#tuple values cannot be changed..!!
#list values can be changed..!!
