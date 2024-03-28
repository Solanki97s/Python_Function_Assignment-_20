def unique_list(l1):
    s1=set(l1)
    print(list(s1))
print("Enter number seperated by comma")
l1=[int(i) for i in input().split(",")]
unique_list(l1)
"""
def unique(l1):
    l2=[]
    s1=set(l1)
    for i in s1:
        l2.append(i)
    return l2
l1=[1,1,2,3,4,5,5,3]
print(unique(l1))
"""