import string
import random

length = int(input("Enter the length of your password! "))  # Convert to int
# you can customize your password to has uppercase, lowercase letters or digits or symbols or all or some of them
def PasswordGen( length = 12, has_upper = True , has_digit = True , has_symbols = True):

    allCharacters = string.ascii_lowercase          # allCharacters = gQ4& and is generated randomly each iteration
    if has_upper:
        allCharacters += string.ascii_uppercase
    if has_digit:
        allCharacters += string.digits
    if has_symbols:
        allCharacters+= string.punctuation
    password = "".join(random.choice(allCharacters) for chara in range (length)) # keeps taking random choice from allCharacters for example 4 then % 
    while (True):
        conditions = []
        conditions.append(any(chara.islower() for chara in password))
        if (has_upper):
            conditions.append(any(chara.isupper() for chara in password ))
        if (has_digit):
            conditions.append(any(chara.isdigit() for chara in password ))
        if (has_symbols):
            conditions.append(any(chara in string.punctuation for chara in password ))
        if all(conditions):
            break
        else:
            password = "".join(random.choice(allCharacters) for chara in range (length))
    
    return password 
            
if __name__ == "__main__":
    password = PasswordGen(length)  
    print(f'Generated password: {password}')

        
    

