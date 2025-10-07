with open ("Input/numbers.txt", "r") as f:
    lines=f.readlines()

j=list(map(
        lambda line:int(line)**2, 
        lines
    ))




with open("Output/output07.txt", "w") as f:
    f.write(f"kvadrat:{j}")
   
