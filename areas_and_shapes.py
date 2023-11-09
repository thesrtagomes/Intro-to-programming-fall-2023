#square
square_side = float(input('What is the length of a side of the square in cm? '))
area_square = square_side ** 2
print(f'The area of the square is: {area_square:.1f} in m².')
print(f'The area of the square is: {area_square / 10000:.1f} in cm².')
print('')

#Rectangle
rectangle_length = float(input('What is the length of rectangle in cm? '))
rectangle_width = float(input('What is the width of rectangle in cm? '))
area_rectangle = rectangle_length * rectangle_width
print(f'The area of the rectangle is: {area_rectangle:.1f} in cm².')
print(f'The area of the rectangle is: {area_rectangle / 10000:.1f} in m².')
print('')

#Circle
import math
circle_radius = float(input(' What is the radius of the circle in cm? '))
area_circle = math.pi * (circle_radius ** 2)
print(f'The area of the circle is: {area_circle} in cm².')
print(f'The area of the circle is: {area_circle / 10000} in m².')

#Challenge
import math
value = float(input('Please inform a length value: '))
square_challenge = value ** 2
circle_radius_challenge = math.pi * (value ** 2)
cube_volume_challenge = value ** 3
sphere_volume_challenge = (4/3) * math.pi * (value **3)
print('') #the round below serves as a "rounder" for very large numbers
print(f'The area of a square is: {round(square_challenge)}.')
print(f'The area os a circle is: {round(circle_radius_challenge)}.')
print(f'The volume of a cube is: {round(cube_volume_challenge)}.')
print(f'The volume of a sphere is: {round(sphere_volume_challenge)}.')



