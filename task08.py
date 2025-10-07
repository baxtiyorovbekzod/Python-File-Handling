with open ("Input/numbers.txt", "r") as f:
    lines=f.readlines()

numbers = list(map(lambda line: int(line), lines))

j = list(filter(lambda n: n % 5 == 0, numbers))
count=len(j)




with open("Output/output08.txt", "w") as f:
    f.write(f"5ga karali:{j}\n")
    f.write(f"Ularning soni: {count}")