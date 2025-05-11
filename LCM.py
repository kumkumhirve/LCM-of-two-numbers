'''Q20. Write a program to find LCM of two numbers.'''

n1 = int(input("n1:"))
n2 = int (input('n2:'))

if n1>n2:
    greater = n1

else :
    greater = n2

while (True):
    if greater %n1==0 and greater %n2 == 0:
        lcm = greater
        break
    greater +=1

print(lcm)

