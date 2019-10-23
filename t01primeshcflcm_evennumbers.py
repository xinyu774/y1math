# What are the even numbers from 1 to num?

num = 123
for i in range(1, num+1):
  if i % 2 == 0:
    print(i, end=' ')
# Python program to print Even Numbers in a List 
  
# list of numbers 
list1 = [10, 21, 4, 45, 66, 93] 
num = 0
  
# using while loop         
while(num < len(list1)): 
      
    # checking condition 
    if num % 2 == 0: 
       print(list1[num], end = " ") 
      
    # increment num   
    num += 1
