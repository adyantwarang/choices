def ab(a, b):

    if a == 1: 
        student = 0.3
        if b == 1: 
            dining = 0.75
        else: 
            dining = 0.25
        print("Probability of a given b: ", dining)

    if a == 2: 
        student = 0.7
        if b == 1: 
            dining = 0.6
        else: 
            dining = 0.4
        print("Probability of a given b: ", dining)

    probab = student * dining
    return round(probab, 3)

print("Check the probability of any event occuring\n")
print("Is the student a freshman?\n")
print("1. Yes")
print("2. No\n")

a = int(input("Enter your choice (1/2): "))

print("Is the student eating in your dining hall?\n")
print("1. Yes")
print("2. No\n")

b = int(input("Enter your choice (1/2): \n"))

print("Heres the probability of both the events occuring: ", ab(a, b))