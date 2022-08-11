#Occurences - is made from the word occur which means that how many times a certain character or word appears.
#Sample List
#Code Example
char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=97
j=122
b=[ ]
while i<=j:
    k=0
    sum=0
    c=[]
    while k<len(char_list):
        if char_list[k]==chr(i):
            e=char_list[k]
            sum=sum+1
        k=k+1
    if sum>0:
        c.append(e)
        c.append(sum)
        b.append(c)
    i=i+1
print(b)