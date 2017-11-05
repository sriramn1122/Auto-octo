#Program to solve the Josephus Problem

n = int(input("Enter Number of Sodiers "))
l = [int (x) for x in bin(n)[2:]]
l.append(l[0])
l.pop(0)
",".join(str(x) for x in l)
str_new = ''
for i in range(len(l)):
    str_new = str_new + str(l[i])
print("Safe Position is ",'=',int((str_new),2))
