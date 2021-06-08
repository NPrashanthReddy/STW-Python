import re
n = int(input())
numbers = [(input()) for i in range(n)]
responses = list(map(lambda x: re.search('(^[789][0-9]{9}$)',x) ,numbers))
for i in responses:
    val = "YES" if i else "NO"
    print(val)