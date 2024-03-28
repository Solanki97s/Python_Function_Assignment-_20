def add(a):
    def num(b):
        sum=a+b
        return sum
    b=int(input("Enter second number"))
    print(num(b))
a=int(input("Enter first number"))
add(a)
