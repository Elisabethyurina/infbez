import math

def mod_pow(base, exponent, mod):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exponent //= 2
    return result

p = 61
q = 53  
N = p * q  
PHI = (p - 1) * (q - 1) 
e = 17
d = 1
while (d * e) % PHI != 1:
    d += 1

message = input("Введите фразу:\n")

encrypted_message = ""
for letter in message:
    m = ord(letter)
    c = mod_pow(m, e, N)
    encrypted_message += str(c) + " "

decrypted_message = ""
encrypted_message = encrypted_message.strip()
encrypted_message_list = encrypted_message.split(" ")
for c in encrypted_message_list:
    m = mod_pow(int(c), d, N)
    decrypted_message += chr(m)

print("Оригинальное сообщение:", message)
print("Зашифрованное сообщение:", encrypted_message)
print("Дешифрованное сообщение:", decrypted_message)


