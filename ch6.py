#conditionals
a=int(input("enter your age: "))
if(a>18):
  print("eligible")#space is called as intentation
elif(a==13):
  print("oooo..")   
else:
  print("not eligible")
match a:
  case 1:
    print("you are one")
  case 2:
    print("you are 2")
  case _:
    print("invalid") 