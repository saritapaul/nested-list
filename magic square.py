#magic square.
list= [[8,3,4],[1,5,9],[6,7,2]]
i=0
sum=0
while i<len(list):
    a=list[i][0]
    sum=sum+a
    row=sum
    j=0
    sum1=0
    while j<len(list):
        b=list[j][0]
        sum1=sum1+b
        j+=1
        col=sum1
    i+=1
print(row)
print(col)
c=0
d=0
diagonal=0
while c<len(list):
    while d<len(list[c]):
        if c==d:
           e=list[c][d]
           diagonal=diagonal+e
           break
        d+=1
    c+=1
print(diagonal)
f=0
g=0
diagonal2=0
c1=len(list)-1
while f<len(list):
    while g<len(list[f]):
        if f==g:
            c2=list[f][g]
            diagonal2=diagonal2+c2
            break
        g+=1
    f+=1
print(diagonal2)
if row==col and diagonal==diagonal2:
    print("it is a magic square")
else:
    print("it is not a magic square")
