# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)

def funargs(normal, *argsrohan, **kwargsbala):
    print(normal)
    for item in argsrohan:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargsbala.items():
        print(f"{key} is a {value}")


# function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

har = ["Harry", "Habib", "Ali", "Hammad",
       "Usama", "The programmer"]
normal = "I am a normal Argument and the students are:"
kw = {"Usama": "Monitor", "Hareem": "Fitness Instructor",
      "The Programmer": "Coordinator", "Ali": "Cook"}
funargs(normal, *har, **kw)

