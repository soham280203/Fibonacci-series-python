print("FIBONACCI SERIES")
range=int(input("Enter the range of Fibonacci series: "))
print("The fibonacci series is")
x=0
y=1
sum=0
while (x<=range):
    print("%d"%x)
    sum=sum+x
    c=x+y
    x=y
    y=c
