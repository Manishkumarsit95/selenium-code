# In Python function is a group of related statement that perform a specific task.
# Keyword to know function def
# Function declration

def GreetMe():
    print("Good Morning")

# Function Calling

GreetMe()

# If I want to call some parameter from function
def GreetMe(Name):
    print("Good Morning" +Name) # + sign Concanated the value

# Function Calling

GreetMe("Manish Kumar")

# Add two integer

def AddInteger(a, b):
    print(a+b)


AddInteger(2, 3)

# Add integer in same function with early
# Function Declration
def GreetMe(Name):
    print("Good Morning" +Name) # + sign Concanated the value

def AddInteger(c, d):
    print(c+d)
# Function Calling
GreetMe("Manish Kumar")

AddInteger(5, 8)

# Other method to add the two integer
def GreetMe(Name):
    print("Good Morning" +Name) # + sign Concanated the value


def AddInteger(c, d):
    return(c+d)
# Function Calling
GreetMe("Manish Kumar")

print(AddInteger(7, 8))
