import random

attributes_list = {}

with open("testFile.txt", "r") as file:
    lines = file.readlines()
    for attribute in lines:
        attributes = attribute.split()
        attributes_list.update({attributes[0]: attributes[1]})

print(attributes_list)

def fileReadLoop(size_to_read: int):
    with open("numbers.txt", "r") as file2:
        if size_to_read <= len(file2.read()):
            random_num = random.randint(1, 5)
            print(random_num)
            for i in range(random_num):
                print(file2.read(size_to_read))
                file2.seek(0)
                size_to_read -= 1
        else:
            print("File size exceeded")

