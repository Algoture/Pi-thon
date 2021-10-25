#Dictionary is an unordered collection of key value pairs enclosed with {}
#You can modify Dictionary because "Dictionary is Mutable"
#We can add both strings and integers in the dictionary


#Data :
dit = {"Yogesh":"Vada Pav","Mummy":"Misal Pav","Father":"Puri Bhaji","Umesh":"Samosa"}
dit2 = {"Processor":"Intel","GPU":"NVIDIA","Cabinet":"NZXT","Keyboard":"Logitech"}
dict3 = {"Umesh","Yogesh","PC","Water"}

#Some methods of Dictionary :

#1)Extracting Keys and Values 
print(dit.keys())
print(dit.values())

#2)Adding a new element in the dictionary
dit["Adarsh"]="Bhendi"
dit["Sidhu Mama"]="Vangi"
print(dit)

#3)Extracting all items from the dictionary
print(dit.items())

#4)Deleting an item from the dictionary
del dit["Adarsh"]
print(dit)

#5)Changing an existing element from the dictionary
dit["Sidhu Mama"]="Paneer"
print(dit)

#6)Updating one ditionary's elements with another
dit.update(dit2)
print(dit)

#7)Pop out an item(also called as element) from the dictionary
dit2.pop("Cabinet")
print(dit2)

#8)Removing the last inserted key-value pair
dit.popitem()
print(dit)

#9)Removing all the items from the dictionary
dit.clear()
print(dit)

#10)Returns a copy of the dictionary
dit.copy()
print(dit)

#11)Print Specific Value
print(dict3["Umesh"])

'''
print(dit["Umesh"]["A"])
we can enter dictionaries into the dictionaries
print(dit["Umesh"])
'''


 