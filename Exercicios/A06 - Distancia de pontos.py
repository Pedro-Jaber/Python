import math

x1 = float(input("Px1 ="))
y1 = float(input("Py1 ="))
x2 = float(input("Qx2 ="))
y2 = float(input("Qy2 ="))

d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"distancia {d:.3f}")
print(f"P ({x1}, {y1})   Q ({x2}, {y2})")



