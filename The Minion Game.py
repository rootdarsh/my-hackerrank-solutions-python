def minion_game(string):
    kevin = 0
    stuart = 0
    vowels = {'A', 'E' , 'I' , 'O' , 'U'}

    # your code goes here
    for i in range(len(s)):   #the entire program logic lies within this 'for loop', think!
        if s[i] in vowels:
            kevin += len(s) - i
        else:
            stuart += len(s) - i
    if stuart > kevin:
        print(f"Stuart {stuart}")
    elif stuart == kevin:
        print("Draw")
    else:
        print(f"Kevin {kevin}")
            
        
                        
    
if __name__ == '__main__':
    s = input()
    minion_game(s)
