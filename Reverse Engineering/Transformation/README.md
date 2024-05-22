# PicoCTF2021 - Transformation

## Description
I wonder what this really is... [enc](./enc) ```''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])```

## Solution
1. The ```enc``` file contains the encoded flag after running the code: ```''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])```
2. Created [script.py](./script.py) to parse ```enc``` and reverse the encoding by iterating through each 16-bit character and:
    1. Split the top 8 and bottom 8 bits as ```high``` and ```low``` respectively
    1. Shift ``high`` by 8 to the right
    2. Convert ```high``` and ```low``` to characters
    3. Append the two characters to ```flag``` respectively

## Flag
picoCTF{16_bits_inst34d_of_8_0ddcd97a}