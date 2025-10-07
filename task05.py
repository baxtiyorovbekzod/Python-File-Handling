with open ("Input/numbers.txt", "r") as f:
    lines=f.readlines()
 
 
numbers = list(map(int, lines))    
total = sum(numbers)/len(numbers)
print(total)

    
