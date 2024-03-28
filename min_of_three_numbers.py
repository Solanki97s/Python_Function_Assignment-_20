"""
def min_of_three_numbers(l1):
    print("min of three number is",min(l1))
print("Enter three number")
n1=int(input())
n2=int(input())
n3=int(input())
l1=[n1,n2,n3]
min_of_three_numbers(l1)
"""
def min_of_three_numbers(l1):
    print("min of three number is",min(l1))
l1 = [int(input("Enter number: ")) for _ in range(3)]
min_of_three_numbers(l1)