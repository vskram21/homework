import string
msg1 = 'attack at dawn'
msg1_cipher = '6c73d5240a948c86981bc294814d'
msg2 = 'attack at dusk'
msg2_cipher = '6c73d5240a948c86981bc2808548'

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    elif len(a) < len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    

print "Xored hex :", strxor(msg1_cipher, msg2_cipher).encode('hex')
print "Xored after encoding:", strxor(msg1_cipher.decode('hex'), msg2_cipher.decode('hex')).encode('hex')
print "Xored msg:", strxor(msg1, msg2).encode('hex') 
