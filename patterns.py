#1
# n=int(input("enter a number: "))
# for i in range(1,n+1):
#   print("*"*n)


# n=int(input("enter a number: "))
# i=1
# while i<=n:
#   print("*"*n)
#   i+=1




# 2
# n=int(input("enter a number: "))
# for i in range(1,n+1):
#     print("*"*i,end="")
#     print(" ")



#2
# n=int(input("enter a number: "))
# i=1
# while i<=n:
#   print("*"*(n-(n-i)))
#   i+=1



#3
# n=int(input("enter a number: "))
# for i in range(1,n+1):
#   print("*"*(n-i+1))






#5
# n=int(input("enter a number: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*i)


#4
# n=int(input("enter a number: "))
# for i in range(1,n+1):
#   for j in range(1,i+1):#this loop prints numbers from i to 1
#     print(j,end="")
#   print("")





# n=int(input("enter a number: "))
# for i in range(1,n+1):
#   for j in range(1,i+1):
#     print(i,end='')
#   print()  



# n=int(input("enter a number: "))
# num=1
# for i in range(1,n+1):
#   for j in range(1,i+1):
#     print(num,end="")
#     num+=1
#   print()  



# n=int(input("enter a number: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#      print(i,end="")
#     print()


# n=int(input("enter a number: "))
# num=1
# for i in range(1,n+1):
#   for j in range(1,n+1):
#    print(num,end="")
#    num+=1
#   print()



"""
    1
   121
  12321
 1234321  
"""
n=int(input("enter a number: "))
for i in range(1,n+1):
  for j in range(1,i+1):
    print(' ',end="")
    print(j,end="")
  print()

