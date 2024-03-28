def palindrome(s1):
   s2=s1[::-1]
   if s1==s2:
     print("string is palindrome")
   else:
      print("string is not palindrome")
s1=input("Enter a string-").lower()
print(s1)
palindrome(s1)