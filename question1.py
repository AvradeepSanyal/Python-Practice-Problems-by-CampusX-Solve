# 1. User will input three ages. Find the oldest ones
person1 = int(input("Whats the age 1st person?"))
person2 = int(input("Whats the age 2nd person?"))
person3 = int(input("Whats the age 3rd person?"))

oldest = max(person1, person2, person3)
print("The oldest person age is", oldest)

#We could have also used if,elif and else to compare between ages.
#And we could have also stored inputs in list