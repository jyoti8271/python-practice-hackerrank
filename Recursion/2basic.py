def printnum(num):
    print(num)
    if(num==3):
        return
    
    printnum(num-1)
    
def printnumfour(num):
    print(num)
    printnumthree(num-1)
    
def printnumthree(num):
    print(num)
    printnumtwo(num-1)
    
def printnumtwo(num):
    print(num)
    printnumone(num-1)
    
def printnumone(num):
    print(num)
    printnum(num-1)
    
    
    

    
    
    
printnum(5)
print("hello world")
    
    
    