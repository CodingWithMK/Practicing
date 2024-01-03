import random

characteristics = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                   'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                   'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                   'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                   'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
                   '9', '0', '@', '.', '!', '$', '_', '-', '?', '*', '#', '~']

password_length = int(input("Enter the length of your desired password. (between 8 and 16 characters): "))
       
def generate_password():
    generated_password = ''.join(random.choice(characteristics) for _ in range(password_length))
    return generated_password
    
    
password = generate_password()
print("Generated password is: ", password)