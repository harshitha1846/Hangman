from random import *
with open('sowpods.txt','r') as f:
    content=f.read().split('\n')
    i=randint(0,len(content))
    print(content[i])
        
        
        
    
