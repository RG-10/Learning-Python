f = open("Usama.txt", "rt")
content = f.read()
print("1", content)
content = f.read()
f.close()
f = open("Usama.txt", "rt")
print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# content = f.read()
#
# for line in f:
#     print(line, end="")
# print(content)
# content = f.read(34455)
# print("1", content)
#
# content = f.read(34455)
# print("2", content)
# f.close()