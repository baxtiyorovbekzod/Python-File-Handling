with open ("Input/students.txt", "r") as f:
    lines=f.readlines()


count=len(lines)




with open("Output/output12.txt", "w") as f:
    f.write(f"ismlar soni:{count}")


print(count)    
   
