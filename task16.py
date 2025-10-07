with open ("Input/students.txt", "r") as f:
    lines=f.readlines()


j = list(filter(lambda line: len(line.strip()) > 5, lines))






with open("Output/output16.txt", "w") as f:
    f.write(''.join(j))


print(j)   
   
