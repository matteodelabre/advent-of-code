print(sum((a:=ord(l[2])-88)*3+(ord(l[0])-63+a)%3+1for l in open(0)))
