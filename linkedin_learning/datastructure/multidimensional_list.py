seating_chart = [
    ["Sarah", "Claire", "Ben", "Taylor"],
    ["Frankie", "George", "Lindsey", "Izzy"],
    ["Chad", "Dayle", "Matt", "Thomas"]
]

print(seating_chart[2][1])

for i, r in enumerate(seating_chart):
    for j, n in enumerate(r):
        print(f"{n} is in row {i+1} and seat {j+1}")