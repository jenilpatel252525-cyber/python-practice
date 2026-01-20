a=[1,3,4,5,7]
key=12

# for i in range(len(a)):
#      for j in range(i+1,len(a)):
#          if a[i] + a[j] > key:
#              break
#          if a[i] + a[j] == key:
#              print(i,j)

i=0
j=1

while(i<5):
    
     if a[i]+a[j]==key:
         print(i,j)
         break

     if a[i]+a[j]<key:
         j+=1
    
     if j>=5 or a[i]+a[j]>key:
         i+=1
         j=i+1
    
