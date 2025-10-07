with open ("Input/numbers.txt", "r") as f:
    lines=f.readlines()
    j=list(filter(
        lambda line: int(line)%2==0, 
        lines
    ))
    print(j)
