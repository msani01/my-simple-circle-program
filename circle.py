print('Simple Circle Calculator!!')
user_radius = float(input('Enter the radius of the circle: '))
option = int(input('Enter 1 to calculate the area or 2 to calculate to perimeter: '))
if option == 1:
    print('The area of a cirlce is :', 2 * 3.142 * user_radius)
elif option == 2:
    print('The perimeter of a cirlce is :', 3.142 * user_radius * user_radius)
else:
    print('Option is invalid!!')
