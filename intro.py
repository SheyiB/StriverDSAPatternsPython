# # name_of_students = ["Divine","Ify", "Mary", "Tobi",2,7,9, True, False]
# # # 
# # # print(name_of_students[4])

# # names = ["divine", "ify", "bola", "sola", "ibrahim"]

# # names.insert(0, "promise")

# # names.append("Elijah")

# # names.remove("bola")
# # names.pop(3)
# # # print(names)
# # # del names[0]
# # # print(names)

# # then = "Boy"
# # print(then)
# # for i in names:
# #     print("A user exists")

# # # print(len(names))
# # # names.clear()
# # # print(names)

# # # name = input("Enter your name\n-->")


# # # if name.lower() in names:
# # #     print("Welcome")
# # # else:
# # #     print("Not recognized")


# # for i in range(1,13):
# #     print("2 * {} = {}".format( i, i*2) )
# #     #print(" 2 * ", i+1, " = ", 2 * (i+1))

# # for i in range(1, 101):
# #     if i%3 ==0 and i%5 == 0:
# #         print("Fizzbuzz!")
# #     elif i%3 == 0:
# #         print("Fizz!")
# #     elif i%5 == 0:
# #         print("Buzz!")
# #     else:
# #         print(i)

# # x = 12

# # y = 0

# # while y < 11:
# #     print(y)
# #     y+=1

# age = 89


# def numberOfMinuites(no_of_scene, no_of_words):
#     minit = no_of_scene * 0.5 + no_of_words * 0.5

# numberOfMinuites(2, 10)
    #print("Welcome Mr/Mrs {}".format(name))

# def sayMyYear(age):
#     print("**************************************")
#     print("You were born in the year {}".format(2022-age))
#     print("**************************************")

# #sa,eyMyYear(89)

# print(sayMyName("Ola"))
# # while x > 1:
# #     print("Hahahahah!")
# #     print(x)
# #     x-=1
def sayMyName(name):
    print("Welcome ", name)


def area_of_triangle(b,h):
    area = 0.5 * (b * h)
    return area 

area = area_of_triangle(2,9)

def myApp():
    name = input("What is your name")
    sayMyName(name)

    l = int(input("What is the base of your triangle"))
    b = int(input("What is the height of your triangle"))

    area = area_of_triangle(l,b)

    print(name, "the area of your triangle is ", area)


myApp()
# print("The area is : ",area)