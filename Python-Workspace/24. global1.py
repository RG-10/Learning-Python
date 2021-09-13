#Global Variable Scope
# l = 10 #Global
# def function1(n):
#     print(n, "I have printed")
# function1("This is me")
# print(l)


# l = 10 # Global
#
# def function1(n):
#     # l = 5 #Local
#     m = 8 #Local
#     global l
#     l = l + 45
#     print(l, m)
#     print(n, "I have printed")
#
# function1("This is me")
# # print(m)

x = 89


def Usama():
    x = 20

    def Raheem():
        global x
        x = 88

    # print("before calling Raheem()", x)
    Raheem()
    print("after calling Raheem()", x)


Usama()
print(x)






