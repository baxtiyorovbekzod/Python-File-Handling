with open ("Input/numbers.txt", "r") as f:
    lines=f.readlines()

numbers=list(map(int, lines))


with open("Output/output01.txt", "w") as f:
    f.write(str(numbers))
