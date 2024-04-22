print ("enter a number :")
no1 = input()
print(type(no1)) #str - default input type

print ("enter another number :")
no2 = input()
print(type(no2)) #str thus we need to typecasting/typeconversion

ans = no1 + no2
print("addition is :"+ans)   #'+' is used because type of ans is str