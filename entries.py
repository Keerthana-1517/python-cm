n=int(input("enter the no of entries you want to enter:"))
dict={}
for i in range(n):
  key=int(input("enter the key:"))
  value=input("enter the value:")
  dict[key]=value
print(dict)
newdict={}
for pair in dict.items():
 newdict[pair[1]]=pair[0]
print(newdict)
