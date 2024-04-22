# Types of Fuction argments in python
# 1: Positional Arguments
# 2: Keyword Argument
# 3: Default Arguments
# 4: Variable numbers of arugments 

#                 1    2    3       #positional arguments - position matters
def Information(name, age, salary):  
    print(" name is : ", name)
    print(" age is : ", age)
    print(" salary is : ", salary)

#             1     2      3 
Information("amit", 32, 300000)
Information("puja", 30, 3000)

Information(age = 32, salary = 102000, name = om)  #keyword arguments - variable name must be same - position doesn't matters



