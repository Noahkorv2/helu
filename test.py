import math
radius = float(input ("Ange radien för din cirkel: "))

def area(radius):
  result = math.pi*radius**2
  return result
print(area(radius))
