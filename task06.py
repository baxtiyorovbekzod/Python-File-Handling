with open ("Input/numbers.txt", "r") as f:
    lines=f.readlines()

j=list(filter(
        lambda line: int(line)%2!=0, 
        lines
    ))




with open("Output/odd_numbers.txt", "w") as f:
    f.write(f"toq sonlar:{j}")
   
