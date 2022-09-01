def pangrams(s):
    # Write your code here
    arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    s = set(s.replace(" ","").lower())
    if(len(s) == len(arr)):
       return("pangram")
    else:
       return("not pangram")

s = 'We promptly judged antique ivory buckles for the next prize'
pangrams(s)