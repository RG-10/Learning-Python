f = open("Usama.txt")
# print(f.tell())
print(f.readline())
# print(f.tell())
print(f.seek(0))
# print(f.tell())
f.close()


f = open("Usama.txt", "r")
print(f.readline() )
print(f.tell())



f = open("Usama.txt", "r")
f.seek(5)
print( f.readline() )

f = open("Usama.txt")
f.seek(11)
print(f.tell())
print(f.readline())
# print(f.tell())

print(f.readline())
# print(f.tell())
f.close()

#Seek and Tell Function
