'''

name = "Praveen Kumar"
name1 = "Mannavaram"
print(name + name1)
print(name +" "+ name1)

#output
#Praveen KumarMannavaram

#Sliceing
name = "praveen kumar mannavaram"
print(name[2])
print(name[7])
print(name[12])
print(name[-1])
print(name[-10])
print(name[-12])
print(name[0:7])
print(name[7:13])
print(name[13:])
print(name[::-1])
print(name[::1])
print(name[0:7:-1])

#output:-
##a
## 
##r
##m
##m
##r
##praveen
## kumar
## mannavaram
##maravannam ramuk neevarp
##praveen kumar mannavaram



name = "praveen kumar mannavaram"
names = name.upper()
names = name.lower()
print(names)
print(name.center(50,'*'))
print(name.ljust(50,'*'))
print(name.rjust(50,'*'))
print("2123".zfill(6))
print("12".zfill(6))
print("212345".zfill(6))

#output:-
##praveen kumar mannavaram
##*************praveen kumar mannavaram*************
##praveen kumar mannavaram**************************
##**************************praveen kumar mannavaram
##002123
##000012
##212345

'''
s = "python programming language"
print(s.split())
print(s.split(p))
print(s.split(m))
print(s.split(g))
