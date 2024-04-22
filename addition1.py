#13/04/24 - typecasting in python 

print ("enter a number :")
no1 = int(input())
print(type(no1)) #int

print ("enter another number :")
no2 = int(input())
print(type(no2)) #str thus we need to typecasting/typeconversion

ans = no1 + no2
print("addition is :" ,ans) 



#this could also be written as 
#no1 = int(input("Enter first number: "))
#no2 = int(input("Enter second number: "))
#ans = no1 + no2
#print (ans)