# default argument
# default arg should be at end of the list of input parameters
# default arg can be override



def Area(Radius, PI = 3.14):   # - default argument
    Result = PI * Radius * Radius
    return Result

ans = Area(2.4)
print("Area is :", ans)

ans = Area(2.4, 6.28)       # override of default arg
print("Area is :", ans)

ans = Area(Radius = 10)
print("Area is :", ans)