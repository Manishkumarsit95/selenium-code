
list1 = [11,12,13,14,15,16,17,18]
list2 = [11,12,13,14,15,16,17,18]
list3 = [11,12,16,17,18,13,14,15]

a = set(list1)
b = set(list2)
c = set(list3)
print(a)
print(b)
print(c)

if a == b & c :
    print("list1 is same as List2 and list 3")
else:
    print("all the 3 list are different")


# without set list1 is not equale to list3
#---------------------------------------------------------

# How to insert or extend the value
#1. append(elmt) - It appends the value at the end of the list.
#2. insert(index, elmt) - It inserts the value at the specified index position.
#3. extends(iterable) - It extends the list by adding the iterable object.

listValue = ["Harshita", "Manish", "Ranchi", "Patna", "Jharkhand"]

print(listValue)

New_listvalue =input("enter the new value:\n") #string
listValue.append(New_listvalue)

print("updated list value:",listValue)

print("--------------------------------------------------")
Value = [10, 20, 30, 40, 50, 60]
print(Value)

Value.insert(5,55)
print("Updated list value", Value)
New_value =int(input("enter the new value:\n")) #integer
New_index =int(input("enter the new index:\n"))

Value.insert(New_index, New_value)
print("updated list value:",Value)

print("--------------Convert list to Str-----------------------")

#-------------------------------Convert the list to Str-----------
# Creating a list with elements of string data type
a_list = ["Python", "Convert", "List", "String", "Method"]

# Converting to string
string = " ".join(a_list)  # this is read as join elements of a_list with a separator (" ")

# Printing the string
print(string)
print(type(string))

#------------------------------------------------
b_list = ["Python", "Convert", 11, "List", 12, "String", "Method"]

# Converting to string
string = " ".join(map (str, b_list))    # this is read as join elements of a_list with a separator (" ")

# Printing the string
print(string)
print(type(string))