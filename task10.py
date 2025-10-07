with open ("Input/numbers.txt", "r") as f:
    lines=f.readlines()

j=sorted(lines, key=int)




with open("Output/sorted_numbers.txt", "w") as f:
    f.write(''.join(j))
   
