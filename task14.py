with open ("Input/students.txt", "r") as f:
    lines=f.readlines()

reversed_names = list(reversed(lines))






with open("Output/output14.txt", "w") as f:
    f.write(''.join(reversed_names))


print(reversed_names)   
   
