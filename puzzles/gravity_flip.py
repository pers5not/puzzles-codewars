def flip(d, a):
    return sorted(a) if d == "R" else sorted(a, reverse=True)
    
    
    
    
print(flip('R', [3, 2, 1, 2]))
print(flip('L', [1, 4, 5, 3, 5]))