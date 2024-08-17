
bicycles: list[str] = ["Trek", "Specialized", "cannondale"]
print(bicycles)


bicycles2: list[str] = ["Trek", "Specialized", "cannondale"]
bicycles2.insert(0, "Nakamura")
print(bicycles2)


coworkers: list[str] = ["Syed", "Christian", "David"]
for coworker in coworkers:
    print(coworker)


coworker_copy: list[str] = coworkers[:]
print(coworker_copy)
