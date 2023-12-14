point = (5,2)

x = point[0]
y = point[1]

def calculate_square_properties(side_length):
    area = side_length * side_length
    perimeter = 4 * side_length
    return (area, perimeter) #<--- tuple.

result = calculate_square_properties(5)
print("Area: ", result[0])
print("Perimeter: ",  result[1])