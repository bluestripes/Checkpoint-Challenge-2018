PATH = 'encrypted.png'
OUTPUT = 'decrypted.png'
key_length = 4
key = b'\x46\x59\x43\x43'

def xor(s1, s2):
    res = [0]*key_length
    for i in range(len(res)):
        q = s1[i]
        d = s2[i]
        k = q ^ d
        res[i] = k
    res = bytearray(res)
    return res


class key_transformator(object):
    def transform(key):
        new_key = [k for k in key]
        for i in range(0, key_length):
            new_key[i] = (new_key[i] + 1) % 256
        return bytearray(new_key)


with open(PATH, 'rb') as f:
    img = f.read()

enc_data = bytearray()
for i in range(0, len(img), key_length):
    enc = xor(img[i:i + key_length], key)
    key = key_transformator.transform(key)
    enc_data += enc

enc_data = enc_data[:-1 * enc_data[-1]]
with open(OUTPUT, 'wb') as f:
    f.write(enc_data)
