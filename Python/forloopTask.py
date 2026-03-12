# 1.Print numbers from 1 to 10 using a for loop
for i in range(1,11):
  print(i)

# 2.Print even numbers from 1 to 50
for i in range(1,51):
    if i % 2 == 0:
        print(i)

# 3.print odd numbers from 1 to 50
for i in range(1,51):
    if i % 2 != 0:
        print(i)

# 4.sum of numbers from 1 to 100
sum = 0
for i in range(1,101):
    sum = sum + i
print("Sum is", sum)

# 5.Print multiplication table of a number
num = int(input("Enter a number:"))
for i in range(1,17):
    print(num,"x",i,"=",num*i)

# 6.Program to count numbers in list
numbers = [5,10,15,20,25,30]
count = 0
for i in numbers:
    count = count + 1
print("Total numbers:", count)

# 7.Print all elements in a list using for loop
numbers = [5,10,15,20,25]
for i in numbers:
    print(i)

# 8. Count vowels in a string
text = input("Enter a string:")
count = 0
for i in text:
    if i in "aeiouAEIOU":
        count = count + 1
print("Number of vowels:", count)

# 9.Print numbers in reverse order from 10 to 1
for i in range(10,0,-1):
    print(i)

# 10.Find factorial of a number using for loop
num = int(input("Enter number:"))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print("Factorial =", fact)

# 11.Find largest number in list
numbers = [12,23,60,55,93,89]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print("Largest number:", largest)

# 12.Count the numbers of digits in a number
num = int(input("Enter number:"))
count = 0
for i in str(num):
    count = count + 1
print("Total digits:", count)

# 13.Print square of numbers from 1 to 10
for i in range(1,11):
    print(i, "square=", i*i)

# 14.Print Cube of numbers from 1 to 10
for i in range(1,11):
    print(i, "cube =", i*i*i)

# 15.Find sum of elements in a list
numbers = [23,34,45,56,78]
sum = 0
for i in numbers:
    sum = sum + i
print("Sum of elements:", sum)
























