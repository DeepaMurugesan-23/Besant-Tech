# 1.Check if a number is positive or negative
a=int(input("Enter a Number"))
if a>0:
    print("The Number is Positive")
else:
    print("The Number is Negative")


# 2.Check whether a number is even or odd
a=int(input("Enter a Number:"))
if a%2==0:
    print(a,"is even number.")
else:
    print(a,"is odd number.")

# 3.Check the largest of two numbers
a=int(input("Enter a Number:"))
b=int(input("Enter a Number:"))
if a>b:
    print("The largest number is",a)
else:
    print("The largest number is",b)

# 4.Find the largest of three numbers using if condition
a=int(input("Enter a Nummber:"))
b=int(input("Enter a Nummber:"))
c=int(input("Enter a Nummber:"))
if a>b:
    if a>c:
        print("Largest number is:",a)
    else:
        print("Largest number is:",c)
else:
    if b>c:
        print("Largest number is:",b)
    else:
        print("Largest number is:",c)

# 5.Check whether a number divisible by 5 and 11
a=int(input("Enter a Number:"))
if a%5==0 and a%11==0:
    print(a,"divisible by 5 and 11")
else:
    print(a,"not divisible by 5 and 11")

# 6.Check whether a year is a  leap year
year=int(input("Enter a Year:"))
if a%400==0:
    print(year,"is leap year")
elif a%4==0:
    print(year,"is leap  year")
else:
    print(year,"is not a leap year")


# 7.Check whether a character is vowel or cconsonant
ch=input("Enter a Character:")
if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")

# 8.Cheeck whether a number is multiple by 3 and 7
num=int(input("Enter a Number"))
if num%3==0 and num%7==0:
    print(a,"is multiple by 3 and 7")
else:
    print(a,"is not multiple by 3 and 7")

# 9.check whether number is a three-digit or not
num = int(input("Enter number: "))
if num >= 100 and num <= 999:
    print("It is Three-digit Number")
else:
    print("Not three-digit Number")

# 10.check whether a number is greater than 100
num=int(input("Enter a Number:"))
if num>100:
    print("The number is greater than 100")
else:
    print("Not greater than 100")
