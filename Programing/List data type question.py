# 1. Check if a list contains an element

x = [1]
print(x) #=> 4501046920 : [1]
x.append(5)
print(x)
x.extend([6,7])
print(x) #=> 4501046920 : [1, 5, 6, 7]


a = [1,2,3]
a.append(4)
print(a)
a.append([5,6])
print(a)

b = [1,2,3]
b.extend([5,6])
print(b)
# remove duplicate
list = [1, 2, 4, 2, 1, 4, 5]
print("Original List: ", list)
res_list = [*set(list)]
print("List after removing duplicate elements: ", res_list)

#
list1 = [100, 200, 300, 300, 100]

# Convert again to list
list1_unique = (set(list1))
print(list1_unique)
ans = [unique for unique in list1_unique if list1.count(unique) == 1]
print(ans)
# uniques

listdup = [10,20,30,20,40,50,60,50]
print(listdup)
listdup_uni = (set(listdup))
print(listdup_uni)
newans =[unique for unique in listdup if listdup.count(unique) ==1]

print(newans)

# renove duplicate
list2 = [5,2,4,8,3,5,4,7,8,5,7,9,7,4]

new_list2= [*set(list2)]

print(new_list2)
