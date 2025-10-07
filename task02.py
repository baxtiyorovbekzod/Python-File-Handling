with open ("Input/numbers.txt", "r") as f:
    lines=f.readlines()

numbers = list(map(int, lines))
total = sum(numbers)

with open("Output/output02.txt", "w") as f:
    f.write(str(total))
