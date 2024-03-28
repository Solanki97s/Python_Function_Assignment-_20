def count_lowercase_uppercase_letter(s2):
    lowercase_count=0
    upper_case_count=0
    for i in s2:
       if i.islower():
           lowercase_count+=1
       else:
        upper_case_count+=1
    print("lowercase_count",lowercase_count,"upper_case_count",upper_case_count)
s1=input("Enter a string-")
s2=s1.replace(" ","")
count_lowercase_uppercase_letter(s2)