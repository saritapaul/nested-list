#Find the sum of number digits in List.
#List Integer Summation : [3, 13, 17, 7]
#Explanation: 1+2 = 3, 6+7=13, 9+8=17, 3+4=7
#list2=[15, 81, 11, 234]
list= [12, 67, 98, 34]
a=[ ]
i=0
while i<len(list):
    j=0
    b=str(list[i])
    while j<len(b):
        d=str(b)
        e=0
        c=0
        while e<len(d):
            c=int(d[e])+c
            e+=1
        j+=1
    a.append(c)
    i+=1
print(a,end=" ")
