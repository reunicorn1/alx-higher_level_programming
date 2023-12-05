#!/usr/bin/python3
BaseGeometry = __import__('8-rectangle').BaseGeometry
Rectangle = __import__('8-rectangle').Rectangle

r = Rectangle(4, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(True, 5)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

print(issubclass(Rectangle, BaseGeometry))
