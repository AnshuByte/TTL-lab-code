#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("HELLO KIIT")


# In[2]:


a= 4
b= 5
c= a+b
print(c)


# In[3]:


#find the sum of given input
a= int (input("input the value of a :"))
b = int (input ("value of  b :"))
c= a+b
print("sum :")
print (c)
d= a-b
print("sub :")
print (d)


# In[4]:


#Area of rectangle,circle.............

length =int (input ("Length : ")) 
bredth =int (input ("bredth : "))
radius =int (input ("radius : "))
height =int (input ("Height : "))
base =int (input ("Base : "))

print ("Area of rectangle :")
area_of_rect = length * bredth
print (area_of_rect)
print ("Area of circle :")
area_of_circle = 3.14 * radius*radius
print(area_of_circle)
print("Area of Square :") 
area_of_square = length * length
print(area_of_square)
print("Area of cuboid") 
area_of_cuboid = 2* (length* bredth + height*bredth + height*length)
print(area_of_cuboid) 
print("TSA of Cone :") 
area_of_cone = 3.14*(radius + length)
print(area_of_cone) 
print("TSA of cylinder :") 
area_of_cylinder = 2 * 3.14*radius*(height + radius)
print("Area of Triangle :")
area_of_triangle = 1/2 * base * height
print(area_of_triangle)


# In[5]:


#find if the value is even or odd

val = int (input ("Input the value :"))
if val%2 == 0:
    print("Even")
else:
    print ("ODD")


# In[6]:


#check for the goven no is Prime or not


num = int (input("Enter the value to check for prime No. :"))
#bool
flag = False
if num == 1:
    print("Not a prime No.")
elif num > 1:
    for i in range(2,num):
        if num%i == 0:
            flag = True
            break
    if flag :
        print(num,"is not a prime")
    else:
        print(num,"is Prime")
            


# In[11]:


#check for armstrong no. 

armno = int (input("Enter the no to check for Armstrong No :"))

#str
arm_length = len(str(armno))
sum = 0
temp = num
while temp >0:
    digit = temp % 10
    sum += digit ** arm_length
#// 
    temp //= 10
if num == sum:
    print(armno,"is an Armstrong No.")
else:
    print(armno,"not an Armstrong No.")


# In[12]:


#palinnndrome 
palinNo =input("Enter the Value to check :")

def isPalindrome(palinNo):
    for i in range (0,int(len(palinNo)/2)):
        if palinNo[i] != palinNo[len(str)-i-1]
        



# In[ ]:




