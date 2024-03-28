def string_pangram(s3):
    s4=set(s3)
    if len(s4)==26:
        print("string is pangram")
    else:
        print("string is not pangram")
    


s1="The quick brown fox jumps over the lazy dog"
s2=s1.replace(" ","")
s3=s2.lower()
string_pangram(s3)