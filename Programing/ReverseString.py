def value1(str):
    str1 = ""  # Declaring empty string to store the reversed string
    for i in str:
        str1 = i + str1

    #return str1  # It will return the reverse string to the caller function

    print(str1)
value1(str = "JavaTpoint")  # Given String
#print("The original string is: ", str)
#print("The reverse string is", reverse_string(str))  # Function call