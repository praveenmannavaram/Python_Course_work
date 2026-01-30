# 1. Circle Area and Circumference Using Lambda
import math

circle_geometry = lambda r: (round(math.pi * r * r, 2), round(2 * math.pi * r, 2))
print("1. Circle Geometry:")
print(circle_geometry(7))
print(circle_geometry(2.5))
print("-" * 40)