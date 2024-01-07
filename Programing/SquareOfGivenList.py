
# Square if Given lit value
my_list = [1, 3, 5, 7]
for v in my_list:

    print (v**2)
# Find the even no list value only
my_list = [1, 3, 5, 7, 8, 6, 2]
for v in my_list:
    if v%2 ==0:
        #print(v)
        print(v, end = " ")
print("done")


# Lambda
x = lambda a, b : a + b
print(x(5, 3))

# Find the odd no list value only

list_value = [22,45,67,33,45,22,44,80,34]

for k in list_value:
    if k % 2 !=0:
        print(k)
print("done")

# even no find
for num in range (10,29):
    if num % 2 == 0:
        print(num)