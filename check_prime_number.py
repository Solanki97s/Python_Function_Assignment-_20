def prime_notprime(num):
    if num<2:
       print(num,"is not prime")
    else:
       for i in range(2,num):
          if num%i==0:
            print(num,"is not prime number")
            break
       else :
        print(num,"is prime number")
num=int(input("Enter a number"))
prime_notprime(num)
