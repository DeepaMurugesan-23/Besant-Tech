# 1.Function to add two numbers
def add(a,b):
 return a+b
print(add(10,5))

# 2.Function to subract two numbers
def subract(a,b):
 return a-b
print(subract(10,5))

# 3.Function to multiply two numbers
def multiply(a,b):
 return a*b
print(multiply(10,5))

# 4.Function to divide two numbers
def divide(a,b):
 return a/b
print(divide(10,5))

# 5.Function find the square of a number
a=int(input("Enter a Number:"))
def square(num):
  return num*num
print("The square of the number is:",square(a))

# 6.Function to check a number is even or odd
a=int(input("Enter a Number:"))
def even_odd(a):
 if a%2==0:
  print(a,"is even number")
 else:
  print(a,"is odd number")
even_odd(a)

# 7.Function to find the largest of two numberss
a=int(input("Enter a Number:"))
b=int(input("Enter a Number:"))
def largest(a,b):
    if a>b:
        print(a,"is the largest number")
    else:
        print(b,"is the largest number")
largest(a,b)

# 8.Function to count vowels in string
text=input("Enter a String:")
def string(text):
    count=0
    for vowel in text:
       if vowel in ("aeiouAEIOU"):
         count +=1
    return count
result= string(text)  
print("Number of vowels",result)

# 9.Function to reverse a string
text=input("Enter a String:")
reversed=text[::-1]
print(reversed)

# 10.Function to find a factorial of a number
a=int(input("Enter a Number:"))
def factorial(a):
  fact=1
  for i in range(1,a+1):
    fact=fact * i  
  print("The Factorial of a number is",fact)
factorial(a)

# 11.Function to find sum of list elements
my_list= [10, 20, 30, 40]
def sum_list(my_list):
    total = 0
    for num in myy_list:
        total = total + num
    return total

result = sum_list(my_list)
print("Sum of list elements:", result)

# 12.Function to find maximum number in the list
my_list= [24,86,12,94,33,57]
def max(my_list):
   largest = my_list[0]
   for i in my_list:
     if i > largest:
            largest = i
   return largest
print("The maximum number is:",max(my_list))

# 13.Function to check whether a number is prime
a=int(input("Enter  a Number:"))
def prime(a):
  for i in range(2,a):
    if a%i==0:
      print("Not a prime number")
      return
  print("Prime number")
prime(a)      

# 14.Function to count character in string
def count_ch(text):
  count=0
  for i in text:
       count=count+1
  return  count
print(count_ch("Besant"))

# 15.Function to return multiplication table of a number
a=int(input("Enter a Number:"))
def table(a):
 for i in range(1,17):
    print(i,"x",a,"=",a*i)
table(a)

















