a=1234
re=0
while a!=0:
    n=a%10
    re=re*10+n
    a//=10
print(re)