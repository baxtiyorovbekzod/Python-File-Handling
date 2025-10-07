with open ("Input/students.txt", "r") as f:
    lines=f.readlines()
    j=list(filter(
        lambda line:str(line).startswith("A"), 
        lines
    ))
    with open("Output/output17.txt", "w") as f:
        f.write(''.join(j))