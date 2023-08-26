# if num_input has a remainder
# print, this is an odd number
# if num_input has 0 remainder
# print this is an even number

input_num = input("Which number do you want to check? ")
modulo_num = int(input_num) % 2
if modulo_num != 0:
    print("This is an odd number")
else:
    print("This is an even number")

