# PicoCTF2021 - Nice netcat...

## Description
There is a nice program that you can talk to by using this command in a shell: ```$ nc mercury.picoctf.net 35652```, but it doesn't speak English...

## Solution
1. When running ```nc mercury.picoctf.net 35652```, it dumped out a bunch of numbers. Suspected it was an ASCII message in decimal format
2. Used ```awk``` to convert decimal to ASCII text by running ```nc mercury.picoctf.net 35652 | awk '{printf("%c", $1)}'```
3. Alternatively, used [Coder's Tool](https://www.coderstool.com/decimal-to-ascii) to decode the decimal dump to ASCII text

## Flag
picoCTF{g00d_k1tty!_n1c3_k1tty!_9b3b7392}
