def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)#called my function
num=int(input("Enter a number:"))
if num<0:
    print("The factorial for 0 is 1")
else:
    print("The factorial for",num,"is",fact(num))
    #factorial of 5:5*4*3*2*1
    