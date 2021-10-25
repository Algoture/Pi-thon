#Idea 1
d ={"Yogesh":"Vada Pav","Mummy":"Misal Pav","Father":"Kharbeli","Umesh":"Annapurna Samosa"}
d2 = input("Enter The Name Here\n")
print(d[d2])


#Idea 2
s = {"Vada Pav":15,"Samosa":10,"Pav Bhaji":30,"Bread":20}
t=input("Enter The Dish Name\n")
print(s[t])


#Idea 3
Dict = {"ignore":"refuse to take notice of or acknowledge", "abandon":"cease to support or look after",
        "exaggerate":"enlarged or altered beyond normal proportions", "prejudice":"preconceived opinion that is not based on reason or actual experience", "programming":"the process of writing computer programs"}
print("Enter the Word")
Data1 = input()
print(Data1, "means", Dict[Data1])



#Idea 4
daru = {"Mirror":"Kannadi","Egg":"Motte","Banana":"Baale Hannu","One":"Ondu"}
print("Enter Any Word From The Following:")
print("Mirror")
print("Egg")
print("Banana")
print("One")
user = input()
print(daru[user],"is it's meaning")