marks={
  "sumaiya":80,#saved by key value so sumaiya is a key value 
  "sufiya":90,
  "sadiya":100

}


print(marks)
print(type(marks))
#print(marks[0]) not worked
print(marks["sumaiya"])#here sumaiya is work as index


#methods of dictionaries
print(marks.items()) 
print(marks.keys())
print(marks.values())
marks.update({"sumaiya":99})
print(marks)
print(marks.get("summu"))#because no key exists
#print(marks["summu"])shows error
print(marks.get("sumaiya"))

#to make an empty set
q= set()
print(type(q))
s={1,2,2,3,6,7,5,4,4,3,4}
print(s)
print(type(s))
s.add(566)
print(s)
s.remove(2)
print(s)
s1={1,2,3}
s2={2,3,4}
print(s1.union(s2))
print(s1.intersection(s2))