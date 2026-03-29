#5. Write a program that will reverse a four digit number. Also it checks whether the reverse is true
numtoberev = (input("Enter a 4 digit number:"))
num_rev = numtoberev[::-1]
print("The reverse number is", num_rev)

if numtoberev == num_rev:
    print("Number is not reversed")
else:
    print("Number is reversed")