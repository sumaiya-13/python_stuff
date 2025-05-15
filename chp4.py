#list are mutable 
frnds=["sumaiya","suraj","sam","suffu",0,3.45]
print(frnds)
frnds[1]="idiot suraj"#we can change this but in strings we cannot
print(frnds)
print(type(frnds[5]))
print(frnds[1:4])
frnds.append("summu")#append means inserting value at the end of the list
print(frnds)
numbers=[1,5,3,8,2,9]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.insert(0,14)#inex,insertion value
print(numbers)
numbers.pop(0)#index it is just removing not deleting
print(numbers)
numbers.remove(3)#insertion value
print(numbers)
print(numbers.count(14))
#tuple is immutable
l1=(1,2,3,4,5)
print(l1)


