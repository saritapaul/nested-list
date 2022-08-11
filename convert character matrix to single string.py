# convert character matrix to single string.
list=[['g','f','g'],['i','s'],['b','e','s','t']]
i=0
list1=" "
while i<len(list):
    j=0
    while j<len(list[i]):
        list1=list1+str(list[i][j])
        j=j+1
    i=i+1
print(list1)
    
