#create dictonary and take input from the user and return the meaning of the
#word from the dictonary

d1={"Mutable": "Can be change", "Immutable": "cant be changed", "Silly": "Cunning"}
a = input("Please enter the word:")
b = a.capitalize()
print(b, " = ",d1[b])