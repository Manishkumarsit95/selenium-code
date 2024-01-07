Val = (1, 2, "Rahul", 4.5)
print(Val[1])

#Val[2] = "RAHUL" # Doest not support item assignment
# Updating the data value not supported

print(Val[-1]) # Last value index is counting start
print(Val[0:3]) # goup of value
#Val.insert(3, shetty) # 'tuple' object has no attribute 'insert'

#Val.append(7) # 'tuple' object has no attribute 'append'

#  Dictionary data Type
dic = {"a":4, 2:"Ram", "c":"Hello Ram"}
print(dic["a"])
print(dic[2])

# How to create the dictionary at run time
dict = {}
dict["First Name"] = "Manish"
dict["Last Name"] = "Kumar"
dict["Gender"] = "Male"
dict["age"] = 21
print(dict)
print(dict["Last Name"])