#14/04/24 - special variable __name__
#__name__ lihilyavar te kuthlya module madhe aahe te sangte: use to disply module name

def Display():
    print("Inside Display function ")
    print(__name__)   #infosystem 



    # in python __name__ it will display '__main__' if the file is entry point file
    # else it will display module name