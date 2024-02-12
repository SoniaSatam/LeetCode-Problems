digits=[1,2,3]
s=''
for i in digits:
    s=s+str(i)
s=str(int(s)+1)
digits=[]
for j in s:
    digits.append(int(j))
print(digits)