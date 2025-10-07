with open ("Input/students.txt", "r") as f:
    lines=f.readlines()


sorted_names=sorted(lines, key=str)





with open("Output/output13.txt", "w") as f:
    f.write(f"sortlangan ismlar:{sorted_names}")


print(sorted_names)   
   
