def permutations(mystr):
    if len(mystr) == 1:  
        return mystr
 
#recurssive call 
    perms = permutations(mystr[1:])  
#first letter  
    char = mystr[0] 
    ans=[] 
 
    for perm in perms: 
        for i in range(len(perm) +1): 
#keeps the char in all the possible positions 
            ans.append(perm[:i] + char + perm[i:]) 
    return ans 

    
print(permutations('sat'))