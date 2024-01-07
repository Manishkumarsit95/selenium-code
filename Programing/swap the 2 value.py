
# Python program to swap two variables

x = 5
y = 10

# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

a = 5
b = 15

temp1 = b
b = a
a = temp1

print("{}{}".format("value of a after swap: ", a))
print("{}{}".format("value of b after swap: ", b))

#Swap the value without using 3rd variable

P = "JavaTpoint"
Q = "Tutorial"

print("Variables Value Before Swapping: ")
print("Value of P: ", P)
print("Value of Q: ", Q)

# Method to swap 'P' and 'Q'
P, Q = Q, P

print("Variables Value After Swapping: ")
print("Value of P: ", P)
print("Value of Q: ", Q)