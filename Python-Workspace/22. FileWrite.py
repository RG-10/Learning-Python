# f = open("Usama.txt", "w")
# a = f.write("Usama bhai achhe hain\n")
# print(a)
# f.close()

f = open("Usama.txt", "a")
a = f.write("Usama bhai achhe hain\n")
print(a)
f.close()

# Handle read and Write both
f = open("Usama.txt", "r+")
print(f.read())
f.write("Thankyou Usama Bhai\n")