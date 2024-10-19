#Q 1.wap to calculate bitwise and of two integer without using the & operator
#2 Wap to find those numbers which are divisible by 7 and multiples of 5 between 1500 to 2700
"""
Ans 1.num1=int(input("enter first number:"))
      temp=num1
	  remainder=0
	  while temp>0:
	       remainder = remainder+str(temp%2)
           temp = temp//2		   
	   num2=int(input("Enter second number:"))
	  

Ans 2. start=1500
       end = 2700
	   print("The numbers divisible by 7 and multiples of 5 between 1500 and 2700 are :")
	   for i in range(start,end+1):
	       if i%7==0 and i%5==0:
		       print(i)

"""

