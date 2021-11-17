# def emod(a,b,c):
#     if b==0:
#         return 1
#     elif b%2==0:
#         d = emod(a,b/2,c)
#         return (d*d)%c
#     else:
#         return ((a%c)*emod(a,b-1,c))%c

# print(emod(3,15,7))

# import random
# x = random.randint(1,10)
# y = random.randint(1,2**1024)
# z = pow( x, y)
# print("Z",z)

import hashlib
x=5
while True:
    h_hex = hashlib.sha256(str(x).encode("utf-8")).hexdigest()
    h_bin = bin( int( h_hex, base=16 ) )[-5:]    
    x+= 1    
    print("".join(h_bin))

# x = 0
# private_key = keys.gen_private_key(curve.secp256k1)
# while True:
# r, s = ecdsa.sign(str(x).encode('utf-8'), private_key)
# h_hex = hashlib.sha256(str(r).encode('utf-8')).hexdigest()
# h_bin = bin( int( h_hex, base=16 ) )[-5:]
# x+= 1
# print("".join(h_bin))