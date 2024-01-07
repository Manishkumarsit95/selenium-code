# read the file and store all the line in the list
# Reverse the list
# write the list back to the line

with open('testreadwrite.txt', 'r') as reader:
    content= reader.readlines()  # [apple, ball, cat, dog, elephant]
    reversed(content)  # [elephant, dog, cat, ball, apple]
    with open('testreadwrite.txt', 'w') as writer:
        for line in reversed(content):  # for loop
            writer.write(line)