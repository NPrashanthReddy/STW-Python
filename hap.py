# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import pdb
n = int(input())
lst = [tuple(input().split()) for i in range(n)]
phoneBook = dict(lst)

while(True):
    
        v = phoneBook.get(q,0)
        if v:
            print(q+"="+v)
        else:
            print("Not found")

a = {1,2,3}
b = {2,3,5}
s = "a"
s.