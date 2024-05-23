# PicoCTF2021 - 

## Description


## Solution
1. Analysed ```crackme.py``` and noticed it contains encrypted secret: ```bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE0g4dd`_cgN"```, a ROT47 decode function and the custom alphabet used
2. Used [dCode](https://www.dcode.fr/rot-cipher) to decode ROT ciphers, setting N = 47, ROTed text = ```A:4@r%uL`M-^M0c0AbcM-MFE0g4dd`_cgN``` and custom alphabet (case sensitive) = ```!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~```

## Alternative solution
1. In ```crackme.py```, call ```decode_secret(bezos_cc_secret)```, which should print out the flag

## Flag
picoCTF{1|\/|_4_p34|\|ut_8c551048}