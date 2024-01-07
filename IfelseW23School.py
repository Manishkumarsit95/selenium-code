# If , elif, else keyword uses

a = 200
b = 30
if b>a:
    print("b is greater than a")
elif b == a:
    print("b and a value is equal")
else:
    print("a is greater than b")

print("all the line is executed")

#-------------------------------------

a = 200
b = 30
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")

# ----Short hand If---------

a = 200
b = 33
if a > b: print("a is greater than b")

#-- Short Hand If  else ____

a = 200
b = 30

print("b") if b > a else print("a")

# _____And , or logic in If else statement_____

a = 200
b = 33
c = 500
if a > b and c > a:
    print("both the condition is true")
if a > b or c < a:
    print("both the condition is true")

#____Nested If______

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# find that if enter value it is prime number or not

#num = 407

# To take input from the user
num = int(input("Enter a number: "))

if num == 1:
    print(" it is not a prime number")
elif num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print("it is not a prime number")
           break
   else:
       print("it is a prime number")

