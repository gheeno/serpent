# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
def return_input_column_num(position):
    column = str(position)
    return column[0]

def return_input_row_num(position):
    row = str(position)
    return row[1]

adjusted_index_row = int(return_input_row_num(position)) - 1
adjusted_index_column = int(return_input_column_num(position)) - 1

def x_mark_the_spot(map_column, row):
    map_column[row] = "X"
    return map_column

x_mark_the_spot(map[adjusted_index_row], adjusted_index_column)
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

