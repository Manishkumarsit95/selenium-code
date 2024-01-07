#program to find the second largest number of list
# declaring the list
list_val = [20, 30, 40, 25, 10]
# sorting the list
list_val.sort()
print(list_val)
#displaying the second last element of the list
print("The second largest element of the list is:", list_val[-2])


#2nd method
# program to find the second largest number of list

# declaring the list
list_val = [20, 30, 40, 25, 10]

# new_list is a set of list1
res_list = set(list_val)
print(res_list)

# removing the maximum element
res_list.remove(max(res_list))

# printing the second largest element
print(max(res_list))