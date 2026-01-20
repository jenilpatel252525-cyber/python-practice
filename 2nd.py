day=str(input("enter day:"))
age=int(input("enter age:"))
#if day=="wednesday":
#    if  age >= 18:
#       print("price is 10$")
#
#    else:
#        print("price is 6$")
#
#else:
#    if  age >= 18:
#        print("price is 12$")
#
#    else:
#        print("price is 8$")
price = 12 if  age>=18 else 10

price = price - 2 if day =="wednesday" else price

print(price)
