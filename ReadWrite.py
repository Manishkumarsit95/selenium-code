#file = open('testreadwrite.txt')
#print(file.read())   # Read all the content in the file

#file.close()

#file = open('testreadwrite.txt')
#print(file.read(5))  # Read n number of character by passing parameter

#file.close()

#file = open('testreadwrite.txt')
#print(file.read(7))

#file.close()

# read one single line at a time using realtime() and using it first comments the read() method
#file = open('testreadwrite.txt')
#print(file.readline())

#file.close()
"""
comment
file = open('testreadwrite.txt')
print(file.readline())
print(file.readline())
print(file.readline())
file.close()
"""
"""
file = open('testreadwrite.txt')
line = file.readline()  # first line read value is apple
while line!= "": # check condition || check condition|| check condition
    print(line)  # Print apple || print 2nd value || print 3rd value
    line=file.readline() # 2nd line read value ball || 3rd line read value cat

file.close()
"""
# 2nd Method
# readlines is the other method who print the value in list format
file = open('testreadwrite.txt')
for line in file.readlines():
    print(line)

file.close()