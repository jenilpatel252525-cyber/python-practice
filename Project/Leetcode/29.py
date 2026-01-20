a=[3,2,1,0]

first=second=third=-1

i=0

for i in range(len(a)):
    if first==-1 or a[i]>a[first]:
        third=second
        second=first
        first=i
    elif second==-1 or a[i]>a[second]:
        third=second
        second=i
    elif third==-1 or a[i]>a[third]:
        third=i

a[first]="first"
a[second]="second"
a[third]="third"
    
print(a)
