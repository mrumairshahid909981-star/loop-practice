num = (1,4,916,25,36,72,100)
x = int (input("Enter a number to find in tuple: "))
i = 0

while i < len(num):
    if (num[i] == x):
        print("found no in tuple", i)
    else:
        print("not found")   
    i += 1