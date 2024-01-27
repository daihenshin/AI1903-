#Q1
#1. Print the following pattern
for i in range(1, 6):
    for y in range(i):
        print(y + 1 , end = '')
    print()
        
   
   
#2. Calculate the sum of all numbers from 1 to a given number
n = int(input('Enter number:'))
s = 0
for i in range(1,n+1):
    s = s + i
print('Sum is: ', s)

#Q2
#1. Display numbers from a list using loop

list = [1,20,50,88,144,151,250,411,551]
for i in list:
    if i > 150:
        continue
    if i > 500:
        break
    if i % 5 == 0:
        print(i)
        
#2. Count the total number of digits in a number
number = input('Enter number: ')
count = 0
for i in number:
    count += 1
print('There are total {} digits in number {}'.format(count,number))

#3. Print list in reverse order using a loop
list1 = [10,20,30,40,50]
for i in list1[: : -1]:
    print(i)
    
#Q3
#1. Create a string made of the middle four characters.
def middle_ele(s):
    if len(s) % 2 == 0:
        middle = int( len(s)/ 2 - 1 )
    else:
        middle = int( len(s) / 2 )
    return middle
s = input('Enter a string:\n')
while len(s) < 4:
    s = input('Enter more than four chars\n')
middle = middle_ele(s)
new_string = s[middle-1] + s[middle] + s[middle+1] + s[middle+2]
print(f'Original string is {s}')
print(f'Middle four chars are: {new_string}')
#2. Append new string in the middle of a given string
def div_str1(s1,s2):
    return s1[:len(s1)//2] + s2 +s1[len(s1)//2:] 


s1 = input("s1: ")
s2 = input("s2: ")
s3 = div_str1(s1,s2)

print(s3)
#3. Create a new string made of the first, middle, and last characters of each input string
def newstr(s1,s2):
    str = s1[0] + s2[0] + s1[int(len(s1)/2)] + s2[int(len(s2)/2)] + s1[-1] + s2[-1]
    return str
s1 = str(input('s1 =: '))
s2 = str(input('s2 =: '))
s3 = newstr(s1,s2)
print(s3)

#4. Arrange string characters such that lowercase letters should come first
s = input('Enter a string:')
output = ''.join( str(i) for i in s if i.islower() )
upper = [str(i) for i in s if i.isupper()]
for i in upper:
    output += i
print(output + '\n')

#5. Count all letters, digits, and special symbols from a given string
str = input("String: ")

Chars = 0
Digits = 0
Symbols = 0

for i in range(len(str)):
    if('0' <= str[i] and str[i] <= '9') : Digits += 1
    elif (('a' <= str[i] and str[i] <= 'z') or ('A' <= str[i] and str[i] <= 'Z')) : Chars += 1
    else : Symbols +=1
    
print(Chars)
print(Digits)
print(Symbols)

#Q4
#1. Removal all characters from a string except integers
s = input('Enter a string:')
output = ''
for i in s:
    if i.isdigit():
        output += i
print(output)

#2. Remove special symbols / punctuation from a string
s = input('Enter a string:')
output = ''
for i in s:
    if i.isalnum():
        output += i
print(output)

#3. Remove empty strings from a list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print("Original list: ")
print(str_list)
str_list = [string for string in str_list if string and string.strip()]
print("Filtered list: ")
print(str_list)

#4. Split a string on hyphens
str1 = "Emma-is-a-data-scientist"
str1 = str1.split('-')
print('Display each substring:')
for i in str1:
   print(i)
