it = 4
while it >1:
    print(it)
    it = it - 1 # it is used to limlit the loop process
print('while loop completed')

# I dont want to print when it is 3
print('------------------')
it = 4
while it >1:
    if it != 3:
        print(it)
    it = it - 1
print('while loop completed')

########## Break function
print('------------------Break statement-----------')
it = 4
while it >1:
    if it == 3:
        break
    print(it)
    it = it - 1
print('while loop completed')

print('--------------new code----------------------')

# BREAK

it = 4
while it >1:
    if it == 3:
        break
    print(it)
    it = it - 1
print('while loop completed')

it = 10
while it >1:
    if it == 3:
        break
    print(it)
    it = it - 1
print('Break Completed')
# Continue
print('-----Continue----')
it = 10
while it >1:
    if it ==9:
        it = it - 1
        continue # 10 is print and program continue runing
    if it == 3:
        break
    print(it)
    it = it - 1
print('while loop completed')

