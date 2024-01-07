
greeting = "Good Morning"

if greeting == "Morning":
    print("Condition Matching")
    print("Second line")
else:
    print("Condition do not Match")
print("if else condition code is completed")


greeting = "Good Morning"

if greeting == "Good Morning":
    print("Condition Matching")
    print("Second line")
else:
    print("Condition do not Match")
print("if else condition code is completed")


a = 4

if a > 2:
    print("a is greater than 2")
    print("Second line")
else:
    print("Condition False")
print("if else condition code is completed")


# For Loop

obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i)
print("----------")
# I want to print multiple of 2 of the obj value
obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i*2)

print("New Program")
# Sum of First 5 Natural Number 1+2+3+4+5=15
# Range (i, j)--- i to j-1
Summation = 0
for i in range(1, 6):
    Summation = Summation + i
    print(i)
print(Summation)

print("-------------------------------------------------------")

for k in range(1, 10, 2): # 2 is index increased
    print(k)
    print("---------SKIPPING FIRST INDEX------------------")

for L in range(10):
    print(L)
