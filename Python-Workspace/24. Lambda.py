# #only for the Convinience
# # Lambda Functions or anonymous functions
# def add(a,b):
#     return a+b
# # minus = lambda x,y: x-y
# def minus(x,y):
#     return x-y
# print(minus(9,4))
import pstats


def a_first(a):
    return a[1]
a = [[1,4], [8,23], [8,43]]
a.sort(key=a_first)
print(a)

