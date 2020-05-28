import rsa

def bytes2int(array):
    n = len(array)
    d = 0
    for b in array:
        n -= 1
        d += b * 256**n
    return d

def int2bytes(num):
    num = bin(num)[2:]
    pad = len(num)%8
    if pad > 0:
        num = '0' * (8-pad) + num
    array = []
    for i in range(len(num)//8):
        array.append(int(num[i*8:i*8+8], base=2))
    return array

def bytes2publicKey(key):
    key = list(key)
    if len(key) <= 127:
        lenght = int(key[0])
        key = key[1:]
    else:
        key[0] = int(bin(key[0])[3:], base=10)
        lenght = bytes2int(key[:4])
        key = key[4:]
    n = bytes2int(key[:lenght])
    e = bytes2int(key[lenght:])
    pubKey = rsa.PublicKey(n, e)
    return pubKey

def publicKey2bytes(key):
    n = int2bytes(key.n)
    e = int2bytes(key.e)
    lenght = int2bytes(len(n))
    if len(lenght) == 2:
        lenght.insert(0, 128)
    elif len(lenght) == 3:
        lenght.insert(0, 0)
        lenght.insert(0, 128)
    elif len(lenght) == 4 and lenght[0] <= 127:
        lenght[0] += 128
    return bytes(lenght + n + e)
