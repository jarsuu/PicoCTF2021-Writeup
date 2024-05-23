# PicoCTF2021 - Magikarp Ground Mission

## Description
Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `b60940ca`
Additional details will be available after launching your challenge instance.

## Solution
1. Connected to instance via `ssh ctf-player@venus.picoctf.net -p 52359` with the passsword
2. `cat 1of3.flag.txt` outputted `picoCTF{xxsh_`
3. `cd /` as instructed by file `instructions-to-2of3.txt` 
4. `cat 2of3.flag.txt` ouputted `0ut_0f_\/\/4t3r_`
5. `cd ~` as instructed by file `instructions-to-3of3.txt`
6. `cat 3of3.flag.txt` ouputted `c1754242}`
7. Combined flag fragments together to get the flag: `picoCTF{xxsh_0ut_0f_\/\/4t3r_c1754242}`

## Flag
picoCTF{xxsh_0ut_0f_\/\/4t3r_c1754242}