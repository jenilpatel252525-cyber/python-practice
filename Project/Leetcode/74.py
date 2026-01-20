a=[1,1,2]
b=[]


def next(a,b):
        i=len(a)-2
        while i>=0 and a[i]>=a[i+1]:
            i-=1
        if i>=0:
            j=len(a)-1
            while a[j]<=a[i]:
                j-=1
        a[i], a[j] = a[j], a[i]
        left=i+1
        right=len(a)-1
        while left < right:
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1
        b.append(a)
        return b


print(next(a,b))