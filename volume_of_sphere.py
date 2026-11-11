def calculate_volume_of_sphere(radius):
  pi = 3.14
  volume = (4/3) * pi * (radius*radius*radius)
  return volume

radius1 = 20
volume1 = calculate_volume_of_sphere(radius1)
print("Volume of sphere with a radii of 20:", volume1)

radius2 = 40
volume2 = calculate_volume_of_sphere(radius2)
print("Volume of sphere with a radii of 40:", volume2)
