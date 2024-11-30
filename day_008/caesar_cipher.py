import string

print(r'''
 ## ##     ##     ### ###   ## ##     ##     ### ##   
##   ##     ##     ##  ##  ##   ##     ##     ##  ##  
##        ## ##    ##      ####      ## ##    ##  ##  
##        ##  ##   ## ##    #####    ##  ##   ## ##   
##        ## ###   ##          ###   ## ###   ## ##   
##   ##   ##  ##   ##  ##  ##   ##   ##  ##   ##  ##  
 ## ##   ###  ##  ### ###   ## ##   ###  ##  #### ##  
                                                      
 ## ##     ####   ### ##   ###  ##  ### ###  ### ##   
##   ##     ##     ##  ##   ##  ##   ##  ##   ##  ##  
##          ##     ##  ##   ##  ##   ##       ##  ##  
##          ##     ##  ##   ## ###   ## ##    ## ##   
##          ##     ## ##    ##  ##   ##       ## ##   
##   ##     ##     ##       ##  ##   ##  ##   ##  ##  
 ## ##     ####   ####     ###  ##  ### ###  #### ##  
''')

def shifter(shift_num, mode):
    shift_num = shift_num % 26
    base = string.ascii_lowercase[shift_num:]+string.ascii_lowercase[:shift_num]
    if mode == 'encode':
        return {
            letter: base[index] for index, letter in enumerate(string.ascii_lowercase)
        }
    else:
        return {
            base[index]: letter for index, letter in enumerate(string.ascii_lowercase)
        }

def encode(message, shift_num):
    contract = shifter(shift_num, 'encode')
    return ''.join(
        contract[letter] for letter in message
    )

def decode(encoded_message, shift_num):
    contract = shifter(shift_num, 'decode')
    return ''.join(
        contract[letter] for letter in encoded_message
    )

option = 'yes'
while option == 'yes':
    crypt_opt = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message (no space):\n").lower()
    while message.isspace() or any(l.isnumeric() for l in message):
        message = input("Your message is in the wrong format. Do it again:\n").lower()
    shift_num = int(input("Type the shift number:\n"))
    if crypt_opt == 'encode':
        encoded_message = encode(message, shift_num)
        print(f"Here's the encoded result: {encoded_message}")
    else:
        decoded_message = decode(message, shift_num)
        print(f"Here's the decoded result: {decoded_message}")
    option = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
