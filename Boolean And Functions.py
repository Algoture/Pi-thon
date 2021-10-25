#Alpha numeric

#Data :
got = "I know who yoou are"
got1 = "helloUmesh"

#checks whether it is alpha numeric or not
print(got.isalnum())
print(got1.isalnum())


#checks whether it endswith or not
print(got.endswith("are"))
print(got1.endswith("H")) 


#counts the characters 
print(got.count("o"))


#capaitalize the characters
print(got1.capitalize()) #capitalizes the first character


#finds the character
print(got.find("who")) #it shows that the character starts from index no of 7


#the function to lower the characters
print(got.lower())


#the function to upper the characters
print(got.upper()) #it uppers all the characters


#the function to replace the characters
print(got.replace("yoou", "they"))