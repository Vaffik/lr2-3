import math
print ("Введите объём шара:", end = " ")
v = int(input())
r = ((3 * v) / (4 * math.pi)) ** (1 / 3)
print (f"Радиус шара равен: {r}")