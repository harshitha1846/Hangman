from random import *
import string
def word():
    with open('sowpods.txt','r') as f:
        content=f.read().split('\n')
        i=randint(0,len(content))
        return content[i].upper()
def intial():
    x=input('\nGuess your letter: ').upper()
    c=duplicate(x)
    d=repeat(x)
    if (x in li) and d:
        while c>0:
            xi=li.index(x)
            li[xi]=0
            #print(li)
            for i in range(len(guess)):
                if i==xi:
                    li2[i]=x
            c-=1  
        return ''.join(li2)
    else:
        global count
        count-=1
            
def repeat(x):
    if x in r:
        r[r.index(x)]=0
        return 1
    else:
        print('you already entered that letter')
        return 0
def duplicate(x):
    c=0
    for i in range(len(li)):
        if li[i]==x:
            c+=1
    return c
def main():
    a=None
    while a!=guess:
        if count>0:
            a=intial()
            display()
        else:
            break
    if a==guess:
        print("you win")
    else:
        print('you lose')

def display():
    for i in li2:
        print(i,end=' ')
    print('\nno of wrong guesses left : ',count)


        
if __name__=='__main__':
    print('WELCOME TO HANGMAN!')
    op='y'
    while(op!='quit'):
        if op=='y': 
            guess=word()
            global count
            count=6
            r=list(string.ascii_uppercase)
            li2=['_']*len(guess)
            li=list(guess)
            print(li)
            display()
            main()
        elif op=='n':
            print('thank u')
            break
        op=input('do u want to start new game : ')




        
    
        
    
    
