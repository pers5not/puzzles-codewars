def digital_root(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    if len(str(sum)) > 1:
        sum = digital_root(sum)  
    return sum 
        
    

       
    
    
    
    
    
    
    

print(digital_root(15))