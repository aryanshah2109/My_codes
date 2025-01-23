import string
alphabet = [i for i in string.ascii_lowercase]

def encrypt(s,shift):
    code = ""
    for i in s:
        shifted_index = alphabet.index(i) + shift
        shifted_index %= len(alphabet)
        code += alphabet[shifted_index]
    return code

def decrypt(s,shift):
    # l = s.split()
    # l2 = []
    # s2 = []
    # unshifted = ""
    # for i in l:
    #     for ch in i:
    #         ascii = ord(ch)
    #         ascii -= shift
    #         ch2 = chr(ascii)
    #         l2.append(ch2)  
    #     unshifted = "".join(l2)
    #     s2.append(unshifted)
    #     l2 = []
    # decrypted = " ".join(s2)
    # return decrypted
    msg = ""
    for i in s:
        back_shift_idx = alphabet.index(i) - shift
        back_shift_idx %= len(alphabet)
        msg += alphabet[back_shift_idx]
    return msg

while(1):
    c = int(input("\nEnter your choice:\n1.Encode\n2.Decode\n3.Exit\n"))
    s = ""
    match c:
        case 1:
            s = input("Enter message to encode: ")
            shift = int(input("Enter shift number: "))
            print("Encoded message: ",encrypt(s,shift))
        case 2:            
            s = input("Enter message to decode: ")
            shift = int(input("Enter shift number: "))
            print("Decoded message: ",decrypt(s,shift))
        case 3:
            break
        case _:
            print("Enter valid input only!")
