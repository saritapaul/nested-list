# Median of list
a=[1,5,10,2,3,7,9]
a.sort( )
i=0
count=0
while i<len(a):
    count+=1
    b=len(a)//2
    c=(a[b])+a[~b]/2
    i+=1
print(c)
    