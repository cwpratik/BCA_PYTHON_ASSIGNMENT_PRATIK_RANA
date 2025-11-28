# Name: Pratik Rana
# Roll No: 2501201012
# Course: BCA
# Semester: 1st
# Subject: Problem Solving with Python
# Assignment: Unit-1 Mini Project
# Title: Student Profile Console App
# Date:

# Task 1

print("   Welcome to Student Profile  ")


# Task 2
full_name = input("Enter Full Name : ")
roll_no = input("Enter Roll No : ")
program = input("Enter Program : ")
uni_name = input("Enter University Name : ")
city = input("Enter City : ")
age= int(input("Enter Age : "))
hobby = input("Enter Hobby : ")


# Task 3 & 4
n1 = float(input("Enter First Number : "))
n2 = float(input("Enter Second Number : "))
operation = input("Enter any operation(+, -, *, /, %, **, //): ")

# Arithmic operators
if operation == "+":
    print(f"{n1} + {n2} = {n1 + n2}")
elif operation == "-":
    print(f"{n1} - {n2} is equal to {n1 - n2}")
elif operation == "*":
    print(f"{n1} * {n2} is equal to {n1 * n2}")
elif operation == "/":
    print(f"{n1} / {n2} is equal to {n1 / n2}")
elif operation == "%":
    print(f"{n1} % {n2} is equal to {n1 % n2}")
elif operation == "**":
    print(f"{n1} ** {n2} is equal to {n1 ** n2}")
elif operation == "//":
    print(f"{n1} // {n2} is equal to {n1 // n2}")
else:
   print(" please choose operation from these options(+, -, *, /, %, **, //)")

# assignment operator
n1 += n2
print(f"{n1} += {n2} equal to {n1}")
n1 -= n2
print(f"{n1} -= {n2} equal to {n1}")

# Comparison operators
if n1 > n2:
    print(f"{n1} is greater than {n2}")
elif n1 < n2:
    print(f"{n2} is greater than {n1}")
else:
    print(n1, "is equal to", n2)

# Logical operators (and, or, not)
if (n1 and n2) > 0:
    print("both " + str(n1) + " and " + str(n2) + " are positive numbers")
elif n1 > 0 or n2 > 0:
    print("only one of them is positive")
elif n1 != 0:
    print(f"{n1} is non zero number")

 # Identity operators (is, is not)
print(age is roll_no)
print(age is not roll_no)

# Membership operators (in, not in)
print(n1 in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
print(n1 not in [10, 20 ,30, 40, 50, 60, 70, 80, 90, 100])

# Task 5:Final Output — Student Profile Card
print("-----------------------------------------")
print("   Welcome to Student Profile System ".upper())
print("-----------------------------------------")

print("Name:\t\t", full_name.title())
print("Roll No:\t", roll_no)
print("Program:\t", program)
print("University:\t", uni_name.upper())
print("City:\t\t", city.title())
print("Age:\t\t", age)
print("Hobby:\t\t", hobby.lower())

print("------------------------------------------")
print("welcome to python programming!".title())

save = input("Do you want to save your data? (y/n)")
if save == "y":
    with open('student_profile.txt', 'w') as file:
        file.write(f"""Name: {full_name}\nRoll No: {roll_no}\nprogram: {program}\nUniversity: {uni_name}\nCity: {city}\nAge:\t\t {age}\nHobby:\t\t {hobby}
        """)