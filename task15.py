with open("Input/students.txt", "r") as f:
    lines = f.readlines()

    names = list(map(lambda n: f"{len(n.strip())} ta harfdan iborat", lines))


with open("Output/output15.txt", "w") as f:
    f.writelines(str(names))