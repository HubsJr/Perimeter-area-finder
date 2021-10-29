#perimeter and area calculator of square,rectangle,e.triangle,circle
import math
userinput=input("input which quadrilateral's perimeter you want:")
modifiedinput=userinput.lower()
if modifiedinput=='square':
    s=input("input the square's side in cm:")
    ps=int(s)*4
    ss=int(s)*int(s)
    print("Perimeter: "+str(ps))
    print("Area: "+str(ss))
elif modifiedinput=='rectangle':
    rl=input("input rectangle length in cm:")
    rw=input("input rectangle width/breadth in cm:")
    pr=2*(int(rl)+int(rw))
    ar=int(rl)*int(rw)
    print("perimeter: "+str(pr))
    print("area: "+str(ar))
elif modifiedinput=='triangle':
    ts=input("triangle's side in cm:")
    pt=int(ts)*3
    at=math.sqrt(3)/4*(int(ts)*int(ts))
    print("perimeter: "+str(pt))
    print("area: "+str(at))
elif modifiedinput=='circle':
    cd=int(input("input circle's radius in cm:"))
    cp=2*(3.14159*cd)
    ca=3.14159*(cd*cd)
    print("perimeter: "+str(cp))
    print("area: "+str(ca))