# While Loop
# With the while loop we can execute a set of statements as long as a condition is true.

# Ex - Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i = i+1

#___ Break Statement____
#With the break statement we can stop the loop even if the while condition is true:
# Ex - exit the loop when i is 3
i = 1
while i<6:
    print(i)
    if i == 3:
        break
    i = i + 1

print("Break statement working")

# _____Continue Statement_____
#With the continue statement we can stop the current iteration, and continue with the next:

# Ex- Continue to the next iteration if i is 3:
i = 1
while i<10:
    print(i)
    i = i + 1
    if i == 3:
        continue
        #or
i = 0
while i < 6:
  i =i + 1
  if i == 3:
    continue
  print(i)

#_____Else Statement_____
# With the else statement we can run a block of code once when the condition no longer is true:

# Ex - Print a message once the condition is false:
i = 1
while i < 6:
  print(i)
  i = i + 1
else:
  print("i is no longer less than 6")







