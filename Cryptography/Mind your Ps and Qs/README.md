# PicoCTF2021 - Mind your Ps and Qs

## Description
In RSA, a small e value can be problematic, but what about N? Can you decrypt this? [values](./values)

## Solution
1. Analysed contents of [values] file and saw values for 'c', 'n' and 'e' which was related to RSA encryption
2. Used [dCode](https://www.dcode.fr/rsa-cipher) and input each value correspondingly and decrypted the message to obtain the flag

## Flag
picoCTF{sma11_N_n0_g0od_45369387}