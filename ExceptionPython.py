# How to create the Exception in python

# 1st method
"""
ItemInCart = 0
# 2 item will be added to the cart
if ItemInCart != 2:
    raise Exception("Product cart count Not Matching")
"""
# 2nd Method
"""
ItemInCart = 0
# 2 item will be added to the cart
assert (ItemInCart == 2)
"""
ItemInCart = 0
# 2 item will be added to the cart
assert (ItemInCart == 0)

# ____Try-Catch______

try:
    with open('testreadwrite.txt', 'r') as reader:
        reader.read()
except:
    print("some how I reached to this block because there is failure in try block")


try:
    with open('testwriteread.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
# Finally is always executed in the code no matter that try block is failed or not but for "except" block not
#executed when the try code is pass.
finally:
    print("cleaning the value")
