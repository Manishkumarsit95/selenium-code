# Enter the value
num = int(input("Enter the number"))

# Intialized the anoyher variable
factorial = 1

# start the condition to be satisfyied
if  num < 0:
    print("for negative value factorial does not exits")
elif num==0:
    print("factorial is 0 or 1")
else:
    for i in range(1, num+1):
        factorial = factorial * i
    print(factorial)





