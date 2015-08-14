# Name: Jeffrey Xiao

s = ""

""" Given a string s with all lower case characters, return the number of vowels
"""

cnt = 0
for x in s :
    if x == 'a' or x == 'e' or x == 'i' or x == 'u' or x == 'o' :
        cnt += 1
print cnt

""" Given a string s with all lower case characters, return the number of times bob occurs
"""

cnt = 0
for i in range(len(s)-2) :
    if s[i:i+3] == 'bob' :
        cnt += 1
print cnt

""" Given a string s with all lower case characters, return the longest substring of s in which all letters occur in alphabetical order
    If there is a tie, print the substring that occurs first
"""

ans = ""
for i in range(len(s)) :
    valid = True
    for j in range(i+1, len(s)) :
        if s[j] < s[j-1] :
            if j-i > len(ans) :
                ans = s[i:j]
                print ans
            valid = False
            break
    if valid and len(s) - i > len(ans) :
        ans = s[i:]
print "Longest substring in alphabetical order is:", ans