# # # print("sandip")
# # # print(2+3)

# recursion...............
# # def recursion_1(k):
# #     if(k > 0):
# #         result = k + recursion_1(k -1)
# #         print(result)
# #     else:
# #         result = 0
# #     return result
# # print(recursion_1(6))


# i = 1
# while i < 9 :
#     print(i)
#     i += 1
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1 

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
  
# for x in "banana":
#       print(x) 
      
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
    # break

# for x in range(6):
    #   print(x)
      
# for x in range(2, 30, 3):
    #   print(x)
    
# for x in range(6):
#       print(x)
# else:
#   print("Finally finished!") 

# for x in range(6):
    #  if x == 3:  break
    #  print(x)
# else:
#   print("Finally finished!") 

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y) 
  
  
# # x = lambda a  :  a +10
# # print(x(5))
# # y = lambda b , c : b ** c
# # print(y(2 ,3))
# def fun_1(n):
#     return lambda a : a * n
# double = fun_1(2)
# print(double(11))
# class Myclass:
#     age = 35
#     name = "sandip"
#     surname = "das"
# obj_1 = Myclass()
# obj_2 = Myclass()
# print(obj_1.age)
# print(obj_1.name)
# print(obj_1.surname)
    

# class Person:
#     def __init__(self , name , age) :
#          self.name = name
#          self.age = age
    
#     def fun_1(self):
#         print("hello I am " + self.name)
# # p1 = Person()
        
# p1 = Person("john" , 36)
# p1.fun_1()


# print(p1.name)
# print(p1.age)

# pyhton functions....
# parameter is variable
# Argument is value

# def fun_1() :
#     print("this is from fun_1")
# fun_1()

# def my_function(fname):
#       print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus") 

# def my_function(fname, lname):
    #   print(fname + " " + lname)

# my_function("Emil", "Refsnes") 

# def my_function(*kids):
    #   print("The youngest child is " + kids[0])
# 
# my_function("Emil", "Tobias", "Linus") 


# def my_function(child3, child2, child1):
    #   print("The youngest child is " + child3)
    #   print("The youngest child is " + child1)
    #   print("The youngest child is " + child2)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 


# def my_function(**kid):
    #   print("His last name is " + kid["lname"])
# 
# my_function(fname = "Tobias", lname = "Refsnes") 


# def my_function(country = "Norway"):
    #   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function() 


# def my_function(food):
    #   for x in food:
        #  print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)


# return values....

# def my_function(x):
#       return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9)) 
# cars = ["Ford", "Volvo", "BMW"]
# x = len(cars) 
# print(x)

# for x in cars:
    # print(x)


# class Myclas:
#     x = 5
#     name = "sandip"
#     surname = "das"
# obj_1 = Myclas()
# print(obj_1.x , obj_1.name , obj_1.surname)

#  CLASS NAME STARTING WITH LOWERCASE LETTER............
# class myclass_1:
#     name = "satabdi"
#     surname  = "moondal"
# obj_2 = myclass_1()
# print(obj_2.name  ,  obj_2.surname)

# mysillyobject is self parameter and it is a 
# reference to the current instance of the class...
# 
#  INHERITENCE IN PYTHON..................

# PARENT CLASS AND CHILD CLASS CONCENT

class person:
    def __init__(self , fname , lname) :
        self.firstname = fname
        self.lastname = lname
    def printname(self) :
        print(self.firstname , self.lastname)
        
x = person("john" , "doe")
x.printname()
        
class childclass(person):
    # pass
    def _init_(self , fname , lname):
        print("seconed is here")
x = childclass("mike" , "shon")
x.printname()

class Student(person):
      def __init__(self, fname, lname):
        super().__init__(fname, lname) 
        
class Student(person):
      def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019
        
        # add methods.............
        # add a method called "welcome" to the "student class"

class Student(person):
      def __init__(self, fname, lname, year):
         super().__init__(fname, lname)
         self.graduationyear = year

      def welcome(self):
         print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear) 
         
x = Student("mike" , "olson" , 2019)
x.welcome()