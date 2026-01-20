n=10

def isprime(n):
    j=int(n/2)
    for i in range(2,j+1):
        if n%i==0:
            return False
    return True

def count(n):
    c=0
    for i in range(2,n):
        if isprime(i):
            c+=1
    print(c)
    
count(20)