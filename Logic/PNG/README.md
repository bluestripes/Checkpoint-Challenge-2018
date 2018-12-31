> png++  
> [This](http://35.194.63.219/csa_2018/png++/_ykotvwaiqnlj/encrypted.png) image was encrypted using a custom cipher.
> We managed to get most of its code [here](http://35.194.63.219/csa_2018/png++/encrypt.py)  
> Unfortunately, while moving things around, someone spilled coffee all over key_transformator.py.  
> Can you help us decrypt the image? 

An image challenge with a not-completed python script. Well lets take a look at the script. 
The first function is generate_initial_key:  
> def generate_initial_key():  
> &nbsp;&nbsp;&nbsp;&nbsp;return ''.join(random.choice(string.ascii_uppercase) for _ in range(4))
As the name implies, it generates the initial key. It randomized. Well that sucks.

The second function is xor. Pretty straight forward:
```python
def xor(s1, s2):
  res = [chr(0)]*key_length 
  for i in range(len(res)): 
    q = ord(s1[i])  
    d = ord(s2[i]) 
    k = q ^ d  
    res[i] = chr(k)  
  res = ''.join(res)  
  return res
```

And the last function is add_padding:
```python
def add_padding(img):
  l = key_length - len(img)%key_length
  img += chr(l)*l
  return img  
```

So it looks like the flag is xored with a randomized key and got padded with PKCS#5 kind of pad.
Now it's time to find out what the script actually does. 
It looks like first the image's data get xored with the key, and then the key get a transformation at an unknown function (who spills coffee on a python function?!).  
So first thing first, let's find out what is the inital key was.  
Because the encrypted image is PNG, we can be sure that the first four bytes should be 0x89 0x50 0x4E 0x47 ("\x89PNG").  
So if we'll try to xor the first four bytes in the encrypted image with those bytes we should get the initial key (xor magic!):<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0xCF xor 0x89 = **0x46**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0x09 xor 0x50 = **0x59**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0x0D xor 0x4E = **0x43**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0x04 xor 0x47 = **0x43**  

We got the initial key. Well that's nice but we still need to find out what is the tranformation function.  
According to [Wikipedia](https://en.wikipedia.org/wiki/Portable_Network_Graphics) the next four bytes should be 0x0D 0x0A 0x1A 0x0A ("\r\n\x1a\n").  
So again we'll try to xor the second four bytes in the encrypted image with those bytes:  <br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0x4A xor 0x0D = **0x47**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0x50 xor 0x0A = **0x5A**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0x5e xor 0x1A = **0x44**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0x4e xor 0x0A = **0x44**  

Ok, I see a pattern here. 1 was added to each byte of the initial key. So I wrote a python script which will xor the key for all the 4 bytes groups in the image, and each time will add 1 to each of the key's bytes (in the repository).  
Well after a few seconds, the decrypted image created. A tiger with a transparent background. Wait! there is something above the tigar!!  
In pink, the flag **flag{r0llin9_my_0wn_crypt0}** is written. Nice another 30 points :smile:
