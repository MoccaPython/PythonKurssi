#Ympyrän pinta-alan laskeminen

Radius_str = input('Anna ympyrän säde: ')
Radius = float(Radius_str)
import math
pi = math.pi
area = math.pi * Radius ** 2
print (f"Ympyrän ala on {area:6.2f}")