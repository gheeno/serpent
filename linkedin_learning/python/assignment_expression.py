import pprint

x = 5
print(x)

# walrus operator.
print("walrus operator : ")
(x := 10)
print(x)

# Non-walrus.
# thestr = input("Value : ")
# while thestr != "exit":
#     print(thestr)
#     thestr = int("Value : ")

while (thestr := input("Value ? ")) != "exit":
    print(thestr)

values = [12,0, 10, 5, 9, 18, 41, 23, 30, 16, 9, 18, 22]
val_data = {
    "length": (l := len(values)),
    "total": (s := sum(values)),
    "average": s / l
}

pprint.pp(val_data)

(squares := [n**2 for n in range(5, 10)])
print(squares)