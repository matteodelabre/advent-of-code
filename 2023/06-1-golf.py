from math import*
print(prod(floor((t+(d:=sqrt(t**2-4*r-4)))/2)-ceil((t-d)/2)+1for t,r in zip(*(map(int,x.split()[1:])for x in open(0).readlines()))))
