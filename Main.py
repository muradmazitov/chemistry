from math import *

class Point:
    def __init__(self, name, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.name = str(name)

    def __repr__(self):
        return ' ' + self.name + "  " + str(self.x) + " " + str(self.y) + " " + str(self.z)

    def len(self):
        x = self.x
        y = self.y
        z = self.z
        return (x**2 + y**2 + z**2)**(1/2)

    def set_new_length(self, k):
        x = self.x
        y = self.y
        z = self.z
        return Point(self.name, x*k, y*k, z*k)

    def __add__(self, other):
        return Point(self.name, self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point(self.name, self.x - other.x, self.y - other.y, self.z - other.z)

def turn(a, V, alpha):
    x, y, z  = V.x, V.y, V.z
    x, y, z  = float(x), float(y), float(z)
    c, s = cos(alpha*pi/180), sin(pi*alpha/180)
    newx = a.x*(c + (1 - c)*(x**2)) + a.y*((1 - c)*x*y - s*z) + a.z*((1 - c)*x*z + s*y)
    newy = a.x*((1 - c)*y*x + s*z) + a.y*(c + (1 - c)*(y**2)) + a.z*((1 - c)*y*z - s*x)
    newz = a.x*((1 - c)*z*x - s*y) + a.y*((1 - c)*z*y + s*x) + a.z*(c + (1 - c)*(z**2))
    return Point(a.name, newx, newy, newz)

def dosmth(a, alpha, i, j, goalpoints):
    alpha = float(alpha)
    v = a[int(i) - 1] - a[int(j) - 1]
    v = v.set_new_length(1/v.len())
    T = a[int(j) - 1]
    a = [el - T for el in a]
    for k in goalpoints:
            a[k] = turn(a[k], v, alpha)
    a = [el + T for el in a]
    return a

begin = open("begin.txt", "r")
B = "".join(begin.readlines())
begin.close()

file = open("DATA.txt", "r")
data = [el.strip().split(" ") for el in file.readlines()]
points = [Point(el[0], float(el[2]), float(el[3]), float(el[4])) for el in data]
file.close()

end = open("end.txt", "r")
E = "".join(end.readlines())
end.close()

print("enter first axis and first angle")
x1, x2, alpha = input().split(" ")

print("enter another axis and angle")
y1, y2, beta = input().split(" ")

print("enter indexes of points that I need to turn round first axis")
goalpointsfirst = [int(el) - 1 for el in input().split(" ")]

print("enter indexes of points that I need to turn round second axis")
goalpointssecond = [int(el) - 1 for el in input().split(" ")]

for i in range(0, 360, int(alpha)):
    for j in range(0, 360, int(beta)):
        t = "turnon" + str(i) + "a" + str(j) + "b" + ".txt"
        somefile = open(t, 'tw', encoding='utf-8')
        somefile.write(B)
        somefile.write("\n".join([str(el) for el in dosmth(dosmth(points, i, x1, x2, goalpointsfirst), j, y1, y2, goalpointssecond)]))
        somefile.write("\n")
        somefile.write(E)
        somefile.close()