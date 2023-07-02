# modules


# import os
# import flask
# import tensorflow
# and more 
# print("Hello Shubham")

# num1 = int(input("Enter the number1:\n"))
# num2 = int(input("Enter the number2:\n"))

# average = ((num1+num2)/2)

# print(average)

# calculate

# a = int(input("Enter the number:\n"))
# print("The squaring number of a is "a*a)
          
# word = "Shubham"
# print(word[1:5:3])

# name = input("Enter your name:\n")

# print("Good afternoon,"+ name)

# name = input("Enter your name:\n")
# date = input("Enter your date:\n")

# letter = ''' Dear <|Name|>,
#             you are selected
#             <|Date|>'''

# letter = letter.replace("<|Name|>",name)
# letter = letter.replace("<|Date|>",date)
# print(letter)

# st = "This is Shubham Solanki"
# st = st.replace(" ", "  ")
# print(st)

# st = " This is a string double Spaces"
# doublespaces = st.find("  ")
# # print(doublespaces)

# letter = "Dear Shubham , This Python course is nice.Thanks!"
# print("Dear Shubham ,\n This Python \tcourse is nice.\\Thanks!")



# f1 = input("Enter the fruit number1:\n")
# f2 = input("Enter the fruit number2:\n")
# f3 = input("Enter the fruit number3:\n")
# f4 = input("Enter the fruit number4:\n")
# f5 = input("Enter the fruit number5:\n")
# f6 = input("Enter the fruit number6:\n")
# f7 = input("Enter the fruit number7:\n")

# MyFruitList = [f1,f2,f3,f4,f5,f6,f7]
# print(MyFruitList)

# marks = [99,67,88,54,46,34,77]

# marks.sort()
# print(marks)

# list = [23,45,67,98]

# list = sum(list)
# print(list)

# a = ( 7,0,8,0,0,9)

# a = a.count(0)
# print(a)


# MyDict = {
#     "Pankha" : "Fan",
#     "Dabba" : "Box",
#     "Vastu": "Item"
# }
# print("Options are ",MyDict.keys())

# a = input("Enter the hindi word\n")
# # print("The meaning of your word is :",MyDict[a])

# # Below lines will not throw an error

# print("The meaning of your word is :",MyDict.get(a))

# num1 = int(input("Enter the number1:\n"))
# num2 = int(input("Enter the number2:\n"))
# num3 = int(input("Enter the number3:\n"))
# num4 = int(input("Enter the number4:\n"))
# num5 = int(input("Enter the number5:\n"))
# num6 = int(input("Enter the number6:\n"))
# num7 = int(input("Enter the number7:\n"))
# num8 = int(input("Enter the number8:\n"))

# s = {num1,num2,num3,num4,num5,num6,num7,num8}

# print(s)

# set = {"18",18}
# # type(set)
# print(type(set))


# set = {18,18}
# # type(set)
# print(set)

# s = {20,20.0,"20"}
# print(s)

# favlang = {}

# a = input("Enter your favourite language shubham:\n")
# b = input("Enter your favourite language vishal:\n")
# c = input("Enter your favourite language raju:\n")
# d = input("Enter your favourite language rohan:\n")

# favlang["shubham"]=a
# favlang["vishal"]=b
# favlang["raju"]=c
# favlang["rohan"]=d

# print(favlang)

# s = {8,7,12,"Harry"}
# s[1] = 5
# print(s)


# age = int(input("Enter the age:\n"))

# if(age>=18):
#    print("yes")

# else:
#    print("no")

# num1 = int(input("Enter the number1:\n"))
# num2 = int(input("Enter the number2:\n"))
# num3 = int(input("Enter the number3:\n"))
# num4 = int(input("Enter the number4:\n"))

# if(num1>num4):
#     f1 = num1

# else:
#     f1 = num4

# if(num2>num4):
#      f2 = num2
       
# else:
#     f2 = num4

# if(num3>num4):
#     f3 = num3

# else:
#     f3 = num4

# if(f1>f2):
#    print(str(f1)+ "is greatest")

   
# if(f2>f3):
#    print(str(f2)+ "is greatest")


# else:
#     print(str(f3)+ "is greatest")

# sub1 = int(input("Enter the number of marks1:\n"))
# sub2 = int(input("Enter the number of marks2:\n"))
# sub3 = int(input("Enter the number of marks3:\n"))
 
# if(sub1<33 or sub2<33 or sub3<33):
#                    print("You are fail because you have less  than 33% in each subject")

# elif(sub1+sub2+sub3)/3 <40:
#         print("you are fail due to  total percentage less than 40")
# else:
#         print("Congratulations! You are passed")

# text  = input("Enter the text:\n")

# if("makes a lot of money" in text):
#         spam = True

# elif("Buy now" in text):
#         spam = True

# elif("Subscribe this" in text):
#         spam = True

# elif("click this" in text):
#         spam = True

# else:
#         spam = False

# if(spam):
#         print("This text is spam")

# else:
#         print("This text is not spam")


# List = [" Shubham " , " Vishal " , " Bhavesh " , " Rahul "]

# name = input("Enter your name to check:\n")

# if name is List:
#       print("Your name is present in the list")

# # otherwise

# else:
#       print("Your name is not present in the list")
      

# Marks = int(input("Enter the marks:\n"))

# if Marks>90:
#       print("Ex")

# elif Marks>=80:
#       print("A")


# elif Marks>=70:
#       print("B")


# elif Marks>=60:
#       print("C")


# elif Marks>=50:
#       print("D")


# else:
#       print("F")

# i = 0
      
# while ( i < 5 ):
#      print("Shubham")
#      i = i + 1

# l = [1,3,4]

# for item in l:
#     print(item)
# else:
#     print("done")

# The break statement

# for i in range(0,76):
#      print(i)
#      if (i==7):
#          break 
    
# for i in range(4):
#       print("Printing")
#       if(i==2):
#          continue

# l = [1,2,4]
# for item in l:
#     pass
# print(l) 

# # For loop
# num = int(input("Enter the number:\n"))
# for i in range(1,11):
#     print(f"{num}*{i}={num*i}")
    
# l1 = ["Harry","Shubham","Vishal","Sonu"]
# for name in l1:
#     if(name.startswith("S")):
#           print(" Hello " + name)

# num = int(input("Enter the number:\n"))
# prime = True

# for i in range (2,num):


#        if(num%i == 0):
#                prime = False 
#                break
# if prime:
#     print("This number is prime")
# else:
#     print("This number is not prime ")

# i = 1
# num = int(input("Enter the natural number:\n"))
# while i in range(1,num):
#  natural = True
#  if(i+1):
#     print("This number is natural")
#     natural = False
#     break
# else:
#   print("This number is not natural")

# program of factorial


# num =  int(input("Enter the number:\n"))
# factorial = 1

# for i in range(1,num+1):
#       factorial = factorial * i
        
# print(f"This factorial of {num} is {factorial}")

# it's wrong:

# for i in range(3):
#     print("*")
#     print("*"  "*")
#     print("*"  "*" * "*")


# it's right

# for i in range(3):
#          print("*" * (i+1))

# def func1():
#     print("Hello Shubham")


# def greet(name):
#       print("Good day , " + name)
      
#       greet("Shubham")

# def greet(name="Shubham"):
#      print("Good Morning ", name)

def numbers