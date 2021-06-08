s = '''But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief
'''
lst = []
for word in s.split():
    if word not in lst:
        lst.append(word)
   # lst.extend(filter(lambda x: x not in lst,line.split()))
lst.sort()
print(lst)
	