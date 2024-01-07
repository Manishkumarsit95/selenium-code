#Python For Loops

# A for loop is used for iterating over a sequence(that is either a list, a tuple, a dictionary, a set, or a string)
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
# Ex - Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# ____Looping Through a String___
# Even strings are iterable objects, they contain a sequence of characters:
# Ex- Loop through the letters in the word "banana":
for x in "banana":
    print(x)

# Factorial 5
x =1
for i in range (1,6):
    if i < 6:
        x= x*i
        print(i)
print(x)
# find summation of prime no from 1 to 50
sum = 0

for num in range(2, 11):

    i = 2

    for i in range(2, num):
        if (int(num % i) == 0):
            i = num
            break;

    # If the number is prime then add it.
    if i is not num:
        sum += num

print("Sum of all prime numbers upto", ":", sum)


