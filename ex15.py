from sys import argv

script, x, y, z = argv 
x = int(x)
y = int(y)
z = int(z)
print "x= %d y= %d z= %d"  % (x,y,z) 
if x > y:
    if x > z:
        print x , "is biggest"
    else:
        print z , "is biggest"
elif y > z:
     if y > x:
        print y , "is biggest"
     else:
        print x , "is biggest"
else:
    print z , "is biggest"
    

