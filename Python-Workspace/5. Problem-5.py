#key value pair = Dictorary

#print(type(d1))
d2= {"Raheem" : "Burger", "Usama": "Fish", "Sara": "roti", "Hassan": {"B": "noodles", "L": "Roti", "D": "Chicken"}}
#d2= ["Murtaza"] = "Biryani"
#d2[420]= "Kebabs"
#del d2[420]
#print(d2["Hassan"]["B"]) #keys change nai hon, number ya string rkhen
d3 = d2
del d3["Usama"]
print(d2)
#All the dictorary