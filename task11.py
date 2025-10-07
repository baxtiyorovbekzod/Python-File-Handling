with open ("Input/students.txt", "r") as f:
    lines=f.readlines()

j=list(map(str, lines))
print(j)




with open("Output/output11.txt", "w") as f:
    f.write(''.join(j))
   
