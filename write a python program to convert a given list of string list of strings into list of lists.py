#Write a Python program to convert a given list of strings into list of lists.
#Convert the said list of strings into list of lists
[['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]
list=['Red', 'Maroon', 'Yellow', 'Olive']
i=0
b=[]
while i<len(list):
    c=[]
    j=0
    while j<len(list[i]):
        c.append(list[i][j])
        j+=1
    i=i+1
    b.append(c)
print(b)
