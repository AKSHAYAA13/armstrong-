x=0
a=input("enter the number to check armstrong or not")
print(type(a))
e=len(a)
for i in a:
    b=eval(i)
    c=b**e
    x=x+c
d=eval(a)
if x==d:
    print(d,"it is armstrong number")
else:
    print(d,"it is not armstrong number")
