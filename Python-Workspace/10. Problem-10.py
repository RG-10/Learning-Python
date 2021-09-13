#Loops
#list1= ["Harem", "Usama", "Carry", "Raheem"]
# list1 = [["Usama", 1], ["Harem", 2], ["Harry", 3],["Marie", 250]]
# dict1= dict(list1)
# for item in dict1:
#     print(item)

# for item, lollypop in dict1.items():
#     print(item, "and lolly is", lollypop)

#----------Quiz-------------
items = [int,float,"Usama", 2,3,5,6,7,3,234]
for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)