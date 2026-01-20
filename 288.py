num1 = "-1+1i"

num2 = "1+1i"

def real1(num):
    i=0
    s={"+","-"}
    while num[i] not in s or i==0:
        i+=1
    return num[:i],num[i+1:len(num)-1],i

def mul(num1,num2):
    r1,i1,sym1=real1(num1)
    r2,i2,sym2=real1(num2)
    a1=int(r1)*int(r2)
    a2=int(r1)*int(num2[sym2]+"1")*int(i2)
    a3=int(num1[sym1]+"1")*int(i1)*int(r2)
    a4=int(num1[sym1]+"1")*int(i1)*int(num2[sym2]+"1")*int(i2)*-1
    print(f"{a1+a4}+{a2+a3}i")
    
mul(num1,num2)