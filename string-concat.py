myname="Rahul"

#myname[0]='P' Error as immutable

myname=myname+myname
print(myname)

myname="z"
print(myname)

mynam="Hello"
myname=myname +" World"
print(myname)

a="h"
b="hi"
c="h"

#Points to the same address due to memory management
print(id(a),id(b),id(c))

