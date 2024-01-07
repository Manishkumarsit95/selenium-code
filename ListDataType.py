
Values = [1, 2, "Rahul", 4, 5]
# list is data type that allows multiple values and can be different data types.

print(Values[0]) #1

print(Values[3]) #4
print(Values[-1]) #last value 5
print(Values[1:3]) # sub index value 2 rahul

Values.insert(3, "Sheety") # Insert value in the existing list value  o/p [1, 2, 'Rahul', 'Sheety', 4, 5]
print(Values)

Values.append(6) # append is the syntex to add the value in the last of list  o/p [1, 2, 'Rahul', 'Sheety', 4, 5, 6]
print(Values)

Values[2] = "RAHUL" # Updating the values with new values in place of old values
print(Values)

del Values[0]  # Delete the Zeroth index values
print(Values)
